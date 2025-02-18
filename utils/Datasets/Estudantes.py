from pandas import read_csv, DataFrame

path_dataset_estudantes_2021 = 'utils/Datasets/data/alunosenturmados_2021_26122023.csv'
def load_data_estudantes_2021(path_to_data=path_dataset_estudantes_2021):
    return DataFrame(read_csv(path_to_data, sep=";"))

path_dataset_estudantes_2022 = 'utils/Datasets/data/alunosenturmados_2022_26122023.csv'
def load_data_estudantes_2022(path_to_data=path_dataset_estudantes_2022):
    return DataFrame(read_csv(path_to_data, sep=";"))

path_dataset_estudantes_2023 = 'utils/Datasets/data/alunosenturmados_2023_26122023.csv'
def load_data_estudantes_2023(path_to_data=path_dataset_estudantes_2023):
    return DataFrame(read_csv(path_to_data, sep=";"))

Estudantes2021 = load_data_estudantes_2021()
Estudantes2022 = load_data_estudantes_2022()
Estudantes2023 = load_data_estudantes_2023()