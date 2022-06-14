import pandas as pd


def full_file():
    f1 = pd.read_csv('/Pycharm/HumanActivityRecognition/full_data.csv')
    return pd.DataFrame(f1)


print(full_file())
