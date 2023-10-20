# TBD: https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats
from .sciopy_dataclasses import (
    ScioSpecMeasurementConfig,
    ScioSpecMeasurementSetup,
)
from datetime import datetime
import numpy as np
from typing import Union
import struct


def set_measurement_config(serial, ssms: ScioSpecMeasurementSetup) -> None:
    """
    set_measurement_config sets the ScioSpec device configuration depending on the ssms configuration dataclass.

    Parameters
    ----------
    serial : _type_
        serial connection
    ssms : ScioSpecMeasurementSetup
        dataclass with the measurement setup settings.
    """

    def clTbt_sp(val: Union[int, float]) -> list:
        """
        clTbt_sp converts an integer or float value to a list of single precision bytes.

        Parameters
        ----------
        val : Union[int, float]
            Value that has to be converted

        Returns
        -------
        list
            list with single precision byte respresentation
        """
        return [int(bt) for bt in struct.pack(">f", val)]

    def clTbt_dp(val: float) -> list:
        """
        clTbt_dp converts an integer or float value to a list of double precision bytes.

        Parameters
        ----------
        val : float
            value that has to be converted

        Returns
        -------
        list
            list with double precision byte respresentation
        """
        return [int(ele) for ele in struct.pack(">d", val)]

    # Set measurement setup:
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    # Set burst count: "B0 03 02 00 03 B0" = 3
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, ssms.burst_count, 0xB0]))

    # Excitation amplitude double precision
    # A_min = 100nA
    # A_max = 10mA
    if ssms.amplitude > 0.01:
        print(
            f"Amplitude {ssms.amplitude}A is out of available range.\nSet amplitude to 10mA."
        )
        ssms.amplitude = 0.01
    serial.write(
        bytearray(list(np.concatenate([[176, 9, 5], clTbt_dp(ssms.amplitude), [176]])))
    )

    # ADC range settings: [+/-1, +/-5, +/-10]
    # ADC range = +/-1  : B0 02 0D 01 B0
    # ADC range = +/-5  : B0 02 0D 02 B0
    # ADC range = +/-10 : B0 02 0D 03 B0
    if ssms.adc_range == 1:
        serial.write(bytearray([0xB0, 0x02, 0x0D, 0x01, 0xB0]))
    elif ssms.adc_range == 5:
        serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    elif ssms.adc_range == 10:
        serial.write(bytearray([0xB0, 0x02, 0x0D, 0x03, 0xB0]))

    # Gain settings:
    # Gain = 1     : B0 03 09 01 00 B0
    # Gain = 10    : B0 03 09 01 01 B0
    # Gain = 100   : B0 03 09 01 02 B0
    # Gain = 1_000 : B0 03 09 01 03 B0
    if ssms.gain == 1:
        serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    elif ssms.gain == 10:
        serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x01, 0xB0]))
    elif ssms.gain == 100:
        serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x02, 0xB0]))
    elif ssms.gain == 1_000:
        serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x03, 0xB0]))

    # Single ended mode:
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))

    # Excitation switch type:
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))

    # Set framerate:
    serial.write(
        bytearray(list(np.concatenate([[176, 5, 3], clTbt_sp(ssms.framerate), [176]])))
    )

    # Set frequencies:
    # [CT] 0C 04 [fmin] [fmax] [fcount] [ftype] [CT]
    f_min = clTbt_sp(ssms.exc_freq)
    f_max = clTbt_sp(ssms.exc_freq)
    f_count = [0, 1]
    f_type = [0]
    # bytearray
    serial.write(
        bytearray(
            list(np.concatenate([[176, 12, 4], f_min, f_max, f_count, f_type, [176]]))
        )
    )

    # Set injection config

    if type(ssms.inj_skip) == int:
        el_inj = np.arange(1, ssms.n_el + 1)
        el_gnd = np.roll(el_inj, -(ssms.inj_skip + 1))
        for v_el, g_el in zip(el_inj, el_gnd):
            serial.write(bytearray([0xB0, 0x03, 0x06, v_el, g_el, 0xB0]))

    if type(ssms.inj_skip) == list:
        for sgl_inj_skip in ssms.inj_skip:
            el_inj = np.arange(1, ssms.n_el + 1)
            el_gnd = np.roll(el_inj, -(sgl_inj_skip + 1))

            for v_el, g_el in zip(el_inj, el_gnd):
                serial.write(bytearray([0xB0, 0x03, 0x06, v_el, g_el, 0xB0]))

    # Get measurement setup
    serial.write(bytearray([0xB1, 0x01, 0x03, 0xB1]))
    # Set output configuration
    serial.write(bytearray([0xB2, 0x02, 0x01, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x03, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x02, 0x01, 0xB2]))

    ## start measurement
    # serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    # stop measurement
    # serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))


def conf_n_el_16_adjacent(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 10 (forced)
    Range 		+/-5V
    Gain 		1
    Min/Max f 	10.000	Steps 1	Scale LINEAR

    Numb of ing.16
    Skip 		0
    Channel Group 	1 (Inject+ : 1, Inject- : 1)
    Switch Type 	Reed Relays
    """

    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x0A, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x09,
                0x05,
                0x3F,
                0x50,
                0x62,
                0x4D,
                0xD2,
                0xF1,
                0xA9,
                0xFC,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x41, 0x20, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x00,
                0x01,
                0x00,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x01, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x02, 0x03, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x03, 0x04, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x04, 0x05, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x05, 0x06, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x06, 0x07, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x07, 0x08, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x08, 0x09, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x09, 0x0A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0A, 0x0B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0B, 0x0C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0C, 0x0D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0D, 0x0E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0E, 0x0F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0F, 0x10, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x10, 0x01, 0xB0]))
    serial.write(bytearray([0xB1, 0x01, 0x03, 0xB1]))
    serial.write(bytearray([0xB2, 0x02, 0x01, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x03, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x02, 0x01, 0xB2]))
    # serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    # serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        com_port=serial.name,
        burst_count=10,
        n_el=16,
        channel_group=[1],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
        size=cnf.size,
        material=cnf.material,
        saline_conductivity=cnf.saline_conductivity,
        temperature=cnf.temperature,
        water_lvl=cnf.water_lvl,
        exc_freq=10000.0,
        datetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    )


def conf_n_el_16_opposite(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 10 (forced)
    Range 		+/-5V
    Gain 		1
    Min/Max f 	10.000	Steps 1	Scale LINEAR

    Numb of ing.16
    Skip 		8
    Channel Group 	1 (Inject+ : 1, Inject- : 9)
    Switch Type 	Reed Relays
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x0A, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x09,
                0x05,
                0x3F,
                0x50,
                0x62,
                0x4D,
                0xD2,
                0xF1,
                0xA9,
                0xFC,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x41, 0x20, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x00,
                0x01,
                0x00,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x01, 0x09, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x02, 0x0A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x03, 0x0B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x04, 0x0C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x05, 0x0D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x06, 0x0E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x07, 0x0F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x08, 0x10, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x09, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0A, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0B, 0x03, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0C, 0x04, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0D, 0x05, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0E, 0x06, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0F, 0x07, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x10, 0x08, 0xB0]))
    serial.write(bytearray([0xB1, 0x01, 0x03, 0xB1]))
    serial.write(bytearray([0xB2, 0x02, 0x01, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x03, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x02, 0x01, 0xB2]))
    # serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    # serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=16,
        channel_group=[1],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
        size=cnf.size,
        material=cnf.material,
        saline_conductivity=cnf.saline_conductivity,
        temperature=cnf.temperature,
        water_lvl=cnf.water_lvl,
        exc_freq=10000.0,
        datetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    )


def conf_n_el_32_adjacent(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 1 (forced)
    Range 		+/-5V
    Gain 		1
    Min/Max f 	10.000	Steps 1	Scale LINEAR

    Numb of ing.32
    Skip 		0
    Channel Group 	1 (Inject+ : 1, Inject- : 2)
    Switch Type 	Reed Relays
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x01, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x09,
                0x05,
                0x3F,
                0x50,
                0x62,
                0x4D,
                0xD2,
                0xF1,
                0xA9,
                0xFC,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x41, 0x20, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x00,
                0x01,
                0x00,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x01, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x02, 0x03, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x03, 0x04, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x04, 0x05, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x05, 0x06, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x06, 0x07, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x07, 0x08, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x08, 0x09, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x09, 0x0A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0A, 0x0B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0B, 0x0C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0C, 0x0D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0D, 0x0E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0E, 0x0F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0F, 0x10, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x10, 0x11, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x11, 0x12, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x12, 0x13, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x13, 0x14, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x14, 0x15, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x15, 0x16, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x16, 0x17, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x17, 0x18, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x18, 0x19, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x19, 0x1A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1A, 0x1B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1B, 0x1C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1C, 0x1D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1D, 0x1E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1E, 0x1F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1F, 0x20, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x20, 0x01, 0xB0]))
    serial.write(bytearray([0xB1, 0x01, 0x03, 0xB1]))
    serial.write(bytearray([0xB2, 0x02, 0x01, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x03, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x02, 0x01, 0xB2]))
    # serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    # serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=1,
        n_el=32,
        channel_group=[1, 2],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
        size=cnf.size,
        material=cnf.material,
        saline_conductivity=cnf.saline_conductivity,
        temperature=cnf.temperature,
        water_lvl=cnf.water_lvl,
        exc_freq=10000.0,
        datetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    )


def conf_n_el_32_opposite(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 1 (forced)
    Range 		+/-5V
    Gain 		1
    Min/Max f 	10.000	Steps 1	Scale LINEAR

    Numb of ing. 	32
    Skip 		16
    Channel Group 	1 (Inject+ : 1, Inject- : 17)
    Switch Type 	Reed Relays
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x01, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x09,
                0x05,
                0x3F,
                0x50,
                0x62,
                0x4D,
                0xD2,
                0xF1,
                0xA9,
                0xFC,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x41, 0x20, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x46,
                0x1C,
                0x40,
                0x00,
                0x00,
                0x01,
                0x00,
                0xB0,
            ]
        )
    )
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x01, 0x11, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x02, 0x12, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x03, 0x13, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x04, 0x14, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x05, 0x15, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x06, 0x16, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x07, 0x17, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x08, 0x18, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x09, 0x19, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0A, 0x1A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0B, 0x1B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0C, 0x1C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0D, 0x1D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0E, 0x1E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x0F, 0x1F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x10, 0x20, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x11, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x12, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x13, 0x03, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x14, 0x04, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x15, 0x05, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x16, 0x06, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x17, 0x07, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x18, 0x08, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x19, 0x09, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1A, 0x0A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1B, 0x0B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1C, 0x0C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1D, 0x0D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1E, 0x0E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x1F, 0x0F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x20, 0x10, 0xB0]))
    serial.write(bytearray([0xB1, 0x01, 0x03, 0xB1]))
    serial.write(bytearray([0xB2, 0x02, 0x01, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x03, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x02, 0x01, 0xB2]))
    # serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    # serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=1,
        n_el=32,
        channel_group=[1, 2],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
        size=cnf.size,
        material=cnf.material,
        saline_conductivity=cnf.saline_conductivity,
        temperature=cnf.temperature,
        water_lvl=cnf.water_lvl,
        exc_freq=10000.0,
        datetime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    )
