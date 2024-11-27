from pandas import read_csv, DataFrame

path_dataset = 'utils/Datasets/data/transporte.csv'

def load_data_transporte(path_to_data=path_dataset):
    return DataFrame(read_csv(path_to_data))

