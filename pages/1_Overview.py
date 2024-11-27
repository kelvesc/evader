import streamlit as st
import pandas as pd

from utils.Datasets.TransporteEscolar import load_data_transporte
from utils.Datasets.Estudantes2022 import load_data_estudantes_2022
from utils.Datasets.Estudantes2023 import load_data_estudantes_2023

transporte = load_data_transporte()
estudantes22 = load_data_estudantes_2022()
estudantes23 = load_data_estudantes_2023()

t = transporte.isna().sum()
e22 = estudantes22.isna().sum()
e23 = estudantes23.isna().sum()

st.write(t, unsafe_allow_html=True)

st.write(e22, unsafe_allow_html=True)

st.write(e23, unsafe_allow_html=True)
