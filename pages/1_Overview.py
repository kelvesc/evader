import streamlit as st
import pandas as pd

from utils.Datasets.TransporteEscolar import TransporteEscolar
from utils.Datasets.Escolas import Escolas2021, Escolas2022, Escolas2023
from utils.Datasets.Estudantes import Estudantes2021, Estudantes2022, Estudantes2023


def show_data_columns(data : pd.DataFrame) -> None:
    data = list(data.columns)
    st.write(*data, unsafe_allow_html=True)

datasets = {
    "Escolas 2021": Escolas2021,    
    "Escolas 2022": Escolas2022,
    "Escolas 2023": Escolas2023,
    "Estudantes 2021" : Estudantes2021,
    "Estudantes 2022" : Estudantes2022,
    "Estudantes 2023" : Estudantes2023
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
