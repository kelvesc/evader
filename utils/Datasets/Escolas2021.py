from pandas import read_csv, DataFrame

path_dataset = 'utils/Datasets/data/info_unidadesensino_2021.csv'

def load_data_escolas_2021(path_to_data=path_dataset):
    return DataFrame(read_csv(path_to_data, sep=";"))

