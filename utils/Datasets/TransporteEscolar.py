from pandas import read_csv, DataFrame

path_dataset_transporte = 'utils/Datasets/data/transporte.csv'
def load_data_transporte(path_to_data=path_dataset_transporte):
    return DataFrame(read_csv(path_to_data, sep=";"))

TransporteEscolar = load_data_transporte()