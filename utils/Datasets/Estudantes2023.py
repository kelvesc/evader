from pandas import read_csv, DataFrame

path_dataset = 'utils/Datasets/data/alunosenturmados_2023_26122023.csv'

def load_data_estudantes_2023(path_to_data=path_dataset):
    return DataFrame(read_csv(path_to_data, sep=";"))

