import streamlit as st
import pandas as pd

from utils.Datasets.TransporteEscolar import load_data_transporte

from utils.Datasets.Escolas2022 import load_data_escolas_2022
from utils.Datasets.Escolas2023 import load_data_escolas_2023

from utils.Datasets.Estudantes2022 import load_data_estudantes_2022
from utils.Datasets.Estudantes2023 import load_data_estudantes_2023


def show_data_columns(data : pd.DataFrame) -> None:
    data = list(data.columns)
    st.write(*data, unsafe_allow_html=True)
    pass


escolas22 = load_data_escolas_2022()
escolas23 = load_data_escolas_2023()

estudantes22 = load_data_estudantes_2022()
estudantes23 = load_data_estudantes_2023()

datasets = {
    "Escolas 2022": escolas22,
    "Escolas 2023": escolas23,
    "Estudantes 2022" : estudantes22,
    "Estudantes 2023" : estudantes23
    }

selected_dataset_name = st.selectbox(
    'Escolha um conjunto de dados:',
    options=list(datasets.keys())
)
if selected_dataset_name:
    selected_dataset = datasets[selected_dataset_name]

    selected_column = st.selectbox(
        f"Escolha uma coluna em {selected_dataset_name}:",
        options=list(selected_dataset.columns)
    )

    if selected_column:
        unique_values = pd.DataFrame(selected_dataset[selected_column].value_counts().reset_index())
        
        total_unique = selected_dataset[selected_column].nunique()
        st.write(f"Existem **{total_unique}** valores únicos em **{selected_column}**.")
        
        st.write(f"Valores únicos em **{selected_column}**:")
        st.table(unique_values)
