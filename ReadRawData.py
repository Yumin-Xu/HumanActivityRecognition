from pathlib import Path


def read_data_phone_accel():
    p_phone_accel = Path("/Pycharm/HumanActivityRecognition/phone/accel/")
    FileList_phone_accel = list(p_phone_accel.glob("**/*.txt"))
    return FileList_phone_accel


def read_data_phone_gyro():
    p_phone_gyro = Path("/Pycharm/HumanActivityRecognition/phone/gyro/")
    FileList_phone_gyro = list(p_phone_gyro.glob("**/*.txt"))
    return FileList_phone_gyro


def read_data_watch_accel():
    p_watch_accel = Path("/Pycharm/HumanActivityRecognition/watch/accel/")
    FileList_watch_accel = list(p_watch_accel.glob("**/*.txt"))
    return FileList_watch_accel


def read_data_watch_gyro():
    p_watch_gyro = Path("/Pycharm/HumanActivityRecognition/watch/gyro/")
    FileList_watch_gyro = list(p_watch_gyro.glob("**/*.txt"))
    return FileList_watch_gyro


def read_csv_phone_accel():
    p_phone_accel = Path("/Pycharm/HumanActivityRecognition/phone/accel/")
    csv_phone_accel = list(p_phone_accel.glob("**/*.csv"))
    return csv_phone_accel


def read_csv_phone_gyro():
    p_phone_gyro = Path("/Pycharm/HumanActivityRecognition/phone/gyro/")
    csv_phone_gyro = list(p_phone_gyro.glob("**/*.csv"))
    return csv_phone_gyro


def read_csv_watch_accel():
    p_watch_accel = Path("/Pycharm/HumanActivityRecognition/watch/accel/")
    csv_watch_accel = list(p_watch_accel.glob("**/*.csv"))
    return csv_watch_accel


def read_csv_watch_gyro():
    p_watch_gyro = Path("/Pycharm/HumanActivityRecognition/watch/gyro/")
    csv_watch_gyro = list(p_watch_gyro.glob("**/*.csv"))
    return csv_watch_gyro
