from pathlib import Path


def read_data_phone_accel():
    p_phone_accel = Path("/Pycharm/HumanActivityRecognition/phone/new_accel/")
    FileList_phone_accel = list(p_phone_accel.glob("**/*.txt"))
    return FileList_phone_accel


def read_data_phone_gyro():
    p_phone_gyro = Path("/Pycharm/HumanActivityRecognition/phone/new_gyro/")
    FileList_phone_gyro = list(p_phone_gyro.glob("**/*.txt"))
    return FileList_phone_gyro


def read_data_watch_accel():
    p_watch_accel = Path("/Pycharm/HumanActivityRecognition/watch/new_accel/")
    FileList_watch_accel = list(p_watch_accel.glob("**/*.txt"))
    return FileList_watch_accel


def read_data_watch_gyro():
    p_watch_gyro = Path("/Pycharm/HumanActivityRecognition/watch/new_gyro/")
    FileList_watch_gyro = list(p_watch_gyro.glob("**/*.txt"))
    return FileList_watch_gyro


def read_csv_phone_accel():
    p_phone_accel = Path("/Pycharm/HumanActivityRecognition/phone/new_accel/")
    csv_phone_accel = list(p_phone_accel.glob("**/*.csv"))
    return csv_phone_accel


def read_csv_phone_gyro():
    p_phone_gyro = Path("/Pycharm/HumanActivityRecognition/phone/new_gyro/")
    csv_phone_gyro = list(p_phone_gyro.glob("**/*.csv"))
    return csv_phone_gyro


def read_csv_watch_accel():
    p_watch_accel = Path("/Pycharm/HumanActivityRecognition/watch/new_accel/")
    csv_watch_accel = list(p_watch_accel.glob("**/*.csv"))
    return csv_watch_accel


def read_csv_watch_gyro():
    p_watch_gyro = Path("/Pycharm/HumanActivityRecognition/watch/new_gyro/")
    csv_watch_gyro = list(p_watch_gyro.glob("**/*.csv"))
    return csv_watch_gyro


def read_csv_label():
    p_label = Path("/Pycharm/HumanActivityRecognition/label/")
    csv_label = list(p_label.glob("**/*.csv"))
    return csv_label


def read_check_label():
    p_label = Path("/Pycharm/HumanActivityRecognition/check/")
    csv_label = list(p_label.glob("**/*.csv"))
    return csv_label
