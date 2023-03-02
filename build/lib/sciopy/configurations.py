# TBD: https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats
from .sciopy_dataclasses import ScioSpecMeasurementConfig


def conf_n_el_16_adjacent(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 10
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
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
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
    serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=16,
        channel_group=[1],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def conf_n_el_16_opposite(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 10
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
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
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
    serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=16,
        channel_group=[1],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def conf_n_el_32_adjacent(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 10
    Range 		+/-5V
    Gain 		1
    Min/Max f 	10.000	Steps 1	Scale LINEAR

    Numb of ing.32
    Skip 		0
    Channel Group 	1 (Inject+ : 1, Inject- : 2)
    Switch Type 	Reed Relays
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x0A, 0xB0]))
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
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
    serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=32,
        channel_group=[1, 2],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def conf_n_el_32_opposite(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude 	1 mA
    Framerate 	10
    Burst Count 	10
    Range 		+/-5V
    Gain 		1
    Min/Max f 	10.000	Steps 1	Scale LINEAR

    Numb of ing. 	32
    Skip 		16
    Channel Group 	1 (Inject+ : 1, Inject- : 17)
    Switch Type 	Reed Relays
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x0A, 0xB0]))
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
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
    serial.write(bytearray([0xB4, 0x01, 0x01, 0xB4]))
    serial.write(bytearray([0xB4, 0x01, 0x00, 0xB4]))
    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=32,
        channel_group=[1, 2],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def configuration_01(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Standart SioSpce configuration template.

    ->!!! TBD !!!<-

    Parameters
    ----------
    serial :
        serial connection

    Returns
    -------
    None
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x01, 0xB0]))  # Burst count
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x40, 0x00, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x44,
                0x7A,
                0x00,
                0x00,
                0x44,
                0x7A,
                0x00,
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

    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=1,
        n_el=32,
        channel_group=[1, 2],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def configuration_02(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude [mA]      1.0
    Range [V]           +/-5
    Framerate           1
    Gain                1
    Burst Count         5

    Min f [Hz]          1000
    Max f [Hz]          1000
    Steps               1
    Scale               LINEAR

    Measure Mode        Single Ended
    Switch Type         Reed Relais

    Channel Group Wizart:

    Num. of Inj.        16
    Chanel Group        Skip 0
    """
    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x05, 0xB0]))
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x3F, 0x80, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x44,
                0x7A,
                0x00,
                0x00,
                0x44,
                0x7A,
                0x00,
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

    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=5,
        n_el=16,
        channel_group=[1],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def configuration_03(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude [mA]      1.0
    Range [V]           +/-1
    Framerate           1
    Gain                1
    Burst Count         5

    Min f [Hz]          10_000
    Max f [Hz]          10_000
    Steps               1
    Scale               LINEAR

    Measure Mode        Single Ended
    Switch Type         Reed Relais

    Channel Group Wizart:

    Num. of Inj.        16
    Chanel Group        Skip 0
    """

    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x05, 0xB0]))
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x3F, 0x80, 0x00, 0x00, 0xB0]))
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

    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=5,
        n_el=16,
        channel_group=[1],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def configuration_04(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude [mA]      1.0
    Range [V]           +/-5
    Framerate           5
    Gain                1
    Burst Count         100

    Min f [Hz]          15_000
    Max f [Hz]          15_000
    Steps               1
    Scale               LINEAR

    Measure Mode        Single Ended
    Switch Type         Reed Relais

    Channel Group Wizart:

    Num. of Inj.        32
    Chanel Group        Skip 0
    """

    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x64, 0xB0]))
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x02, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x40, 0xA0, 0x00, 0x00, 0xB0]))
    serial.write(
        bytearray(
            [
                0xB0,
                0x0C,
                0x04,
                0x46,
                0x6A,
                0x60,
                0x00,
                0x46,
                0x6A,
                0x60,
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

    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=100,
        n_el=32,
        channel_group=[1, 2],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def configuration_05(
    serial, cnf: ScioSpecMeasurementConfig
) -> ScioSpecMeasurementConfig:
    """
    Amplitude [mA]      1.0
    Range [V]           +/-10
    Framerate           5
    Gain                1
    Burst Count         10

    Min f [Hz]          10_000
    Max f [Hz]          10_000
    Steps               1
    Scale               LINEAR

    Measure Mode        Single Ended
    Switch Type         Reed Relais

    Channel Group Wizart:

    Num. of Inj.        64
    Chanel Group        Skip 0
    """

    serial.write(bytearray([0xB0, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x02, 0x00, 0x0A, 0xB0]))
    serial.write(
        bytearray(
            [0xB0, 0x09, 0x05, 0x3F, 0x50, 0x62, 0x4D, 0xD2, 0xF1, 0xA9, 0xFC, 0xB0]
        )
    )
    serial.write(bytearray([0xB0, 0x02, 0x0D, 0x03, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x09, 0x01, 0x00, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x08, 0x01, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x02, 0x0C, 0x01, 0xB0]))
    serial.write(bytearray([0xB0, 0x05, 0x03, 0x40, 0xA0, 0x00, 0x00, 0xB0]))
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
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x20, 0x21, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x21, 0x22, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x22, 0x23, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x23, 0x24, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x24, 0x25, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x25, 0x26, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x26, 0x27, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x27, 0x28, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x28, 0x29, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x29, 0x2A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x2A, 0x2B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x2B, 0x2C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x2C, 0x2D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x2D, 0x2E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x2E, 0x2F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x2F, 0x30, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x30, 0x31, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x31, 0x32, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x32, 0x33, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x33, 0x34, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x34, 0x35, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x35, 0x36, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x36, 0x37, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x37, 0x38, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x38, 0x39, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x39, 0x3A, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x3A, 0x3B, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x3B, 0x3C, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x3C, 0x3D, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x3D, 0x3E, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x3E, 0x3F, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x3F, 0x40, 0xB0]))
    serial.write(bytearray([0xB0, 0x03, 0x06, 0x40, 0x01, 0xB0]))
    serial.write(bytearray([0xB1, 0x01, 0x03, 0xB1]))
    serial.write(bytearray([0xB2, 0x02, 0x01, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x03, 0x01, 0xB2]))
    serial.write(bytearray([0xB2, 0x02, 0x02, 0x01, 0xB2]))

    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=64,
        channel_group=[1, 2, 3, 4],
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )


def configure_configuration(serial, cnf: ScioSpecMeasurementConfig) -> None:
    """TBD"""
    pass

    return ScioSpecMeasurementConfig(
        serial.name,
        burst_count=10,
        n_el=64,
        channel_group=cnf.channel_group,
        actual_sample=cnf.actual_sample,
        s_path=cnf.s_path,
        object=cnf.object,
    )
