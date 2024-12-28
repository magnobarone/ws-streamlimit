import streamlit as st
import pandas as pd
import numpy as np

#Titulo da aplicação
st.title("Exemplo de aplicação Streamlit")

#Adiciona header
st.header("Introdução ao Streamlit")

#Adiciona texto
st.text("Esta é uma aplicação web com Streamlit")

#Criação de um dataframe
data = pd.DataFrame({
    'Coluna 1': [1,2,3,4],
    'Coluna 2': [10,20,30,40]
})

st.dataframe(data)

#Adiciona um gráfico de linha
st.line_chart(data)

#Adiciona um botão clicável com resposta
if st.button('Clique aqui'):
    st.write('Botão Clicado')

#Adiciona um seletor
opcao = st.selectbox('Escolha uma opção', ['Opção A', 'Opção B', 'Opção C'])
st.write('Você selecionou: ', opcao)