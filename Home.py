import streamlit as st

st.set_page_config(
    page_title = "Sistema de predição de demandas escolares por região da cidade.",
    layout = "wide",
    menu_items = {
        'About': '''Este sistema foi desenvolvido originalmente para fins da disciplina de 
        Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3) do 3° período do curso de Bacharelado em Sistemas de Informação
        (BSI) da Universidade Federal Rural de Pernambuco (UFRPE).
        Dúvidas? 
            gabriel.augustos@ufrpe.br
            kelves.nunes@ufrpe.br
        Acesse: bsi.ufrpe.br
        '''
    }
)

st.markdown(f'''
    <h1>Preditor de demandas escolares por região do Recife</h1>
    <br>
    Este projeto está em desenvolvimento, durante o curso da disicplina de 
    Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3) do 3° período 
    do curso de Bacharelado em Sistemas de Informação (BSI)
    da Sede da Universidade Federal Rural de Pernambuco (UFRPE).
    <br>
    O trabalho desenvolvido aqui tem por objetivo a construção de um 
    classificador de demandas escolares por regiões (bairros) da cidade do Recife.
    Os dados utilizados nessa pesquisa foram obtidos diretamente das plataformas de 
    dados abertos do Recife e do IBGE.
    
    No decorrer do trabalho pretendemos expor:
    <ul>
            <li>Indicadores socioeconômicos do Recife.</li>
            <li>Traçar um perfil dos habitantes de cada bairro da cidade.</li>
            <li>Desenhar o perfil dos estudantes e das escolas de cada região.</li>
            <li>Analizar mudanças nos indicadores em uma janela de tempo.</li>
            <li>Visualização das analises.</li>
            <li>Utilizar algoritmos de Aprendizado de Máquina para agrupamento e classificação das demandas escolres em cada região da cidade.</li>
    </ul>
    Contato: 
            <li> gabriel.augustos@ufrpe.br</li>
            <li> kelves.nunes@ufrpe.br</li>
    Acesse: <a href="bsi.ufrpe.br">bsi.ufrpe.br</a>
''', unsafe_allow_html=True)