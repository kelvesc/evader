from pandas import read_csv, DataFrame

path_dataset = 'utils/Datasets/data/info_escolas_2023_27122023.csv'

def load_data_escolas_2023(path_to_data=path_dataset):
    return DataFrame(read_csv(path_to_data, sep=";"))

