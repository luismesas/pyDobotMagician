from enum import Enum

class CommunicationProtocolIDs(Enum):

    GET_SET_DEVICE_SN = 0
    GET_SET_DEVICE_NAME = 1
    GET_POSE = 10
    RESET_POSE = 11
    GET_ALARMS_STATE = 20
    CLEAR_ALL_ALARMS_STATE = 21
    SET_GET_HOME_PARAMS = 30
    SET_HOME_CMD = 31
    SET_GET_HHTTRIG_MODE = 40
    SET_GET_HHTTRIG_OUTPUT_ENABLED = 41
    GET_HHTTRIG_OUTPUT = 42
    SET_GET_ARM_ORIENTATION = 50
    SET_GET_END_EFFECTOR_PARAMS = 60
    SET_GET_END_EFFECTOR_LAZER = 61
    SET_GET_END_EFFECTOR_SUCTION_CUP = 62
    SET_GET_END_EFFECTOR_GRIPPER = 63
    SET_GET_JOG_JOINT_PARAMS = 70
    SET_GET_JOG_COORDINATE_PARAMS = 71
    SET_GET_JOG_COMMON_PARAMS = 72
    SET_GET_PTP_JOINT_PARAMS = 80
    SET_GET_PTP_COORDINATE_PARAMS = 81
    SET_GET_PTP_JUMP_PARAMS = 82
    SET_GET_PTP_COMMON_PARAMS = 83
    SET_PTP_CMD = 84
    SET_CP_CMD = 91
    SET_QUEUED_CMD_START_EXEC = 240
    SET_QUEUED_CMD_STOP_EXEC = 241
    SET_QUEUED_CMD_CLEAR = 245
    GET_QUEUED_CMD_CURRENT_INDEX = 246

class ControlValues(Enum):

    ZERO = 0x00
    ONE = 0x01
    TWO = 0x02
    THREE = 0x03
    FOUR = 0x04
    FIVE = 0x05
    SIX = 0x06
    SEVEN = 0x07
    EIGHT = 0x08
    NINE = 0x09

class PTPMode(Enum):
    """
    0. JUMP_XYZ, ]
        Jump mode,
        (x,y,z,r)
        is the target point in Cartesian coordinate system
    1. MOVJ_XYZ,
        Joint movement,
        (x,y,z,r)
        is the target point in Cartesian coordinate system
    2. MOVL_XYZ,
        Linear movement,
        (x,y,z,r)
        is the target point in Cartesian coordinate system
    3. JUMP_ANGLE,
        Jump mode, (x,y,z,r)
        is the target point in Jointcoordinate system
    4. MOVJ_ANGLE,
        Joint movement,
        (x,y,z,r)
        is the target point in Joint coordinate system
    5. MOVL_ANGLE,
        Linear movement,
        (x,y,z,r)
        is the target point in Joint coordinate system
    6. MOVJ_INC,
        Joint movement increment mode,
        (x,y,z,r)
        is the angle increment in Joint coordinate system
    7. MOVL_INC,
        Linear movement increment mode,
        (x,y,z,r)
        is the Cartesian coordinate increment in Joint coordinate system
    8. MOVJ_XYZ_INC,
        Joint movement increment mode,
        (x,y,z,r)
        is the Cartesian coordinate increment in Cartesian coordinate system
    9. JUMP_MOVL_XYZ,
        Jump movement,
        (x,y,z,r)
        is the Cartesian coordinate increment in Cartesian coordinate system
    """
    JUMP_XYZ = 0x00
    MOVJ_XYZ = 0x01
    MOVL_XYZ = 0x02
    JUMP_ANGLE = 0x03
    MOVJ_ANGLE = 0x04
    MOVL_ANGLE = 0x05
    MOVJ_INC = 0x06
    MOVL_INC = 0x07
    MOVJ_XYZ_INC = 0x08
    JUMP_MOVL_XYZ = 0x09