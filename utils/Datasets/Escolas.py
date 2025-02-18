from pandas import read_csv, DataFrame

path_dataset_escolas_2021 = 'utils/Datasets/data/info_unidadesensino_2021.csv'

def load_data_escolas_2021(path_to_data=path_dataset_escolas_2021):
    return DataFrame(read_csv(path_to_data, sep=";"))


path_dataset_escolas_2022 = 'utils/Datasets/data/info_escolas_2022_27122023.csv'

def load_data_escolas_2022(path_to_data=path_dataset_escolas_2022):
    return DataFrame(read_csv(path_to_data, sep=";"))


path_dataset_escolas_2023 = 'utils/Datasets/data/info_escolas_2023_27122023.csv'

def load_data_escolas_2023(path_to_data=path_dataset_escolas_2023):
    return DataFrame(read_csv(path_to_data, sep=";"))


Escolas2021 = load_data_escolas_2021()
Escolas2022 = load_data_escolas_2022()
Escolas2023 = load_data_escolas_2023()