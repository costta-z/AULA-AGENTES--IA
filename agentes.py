import os
import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM

# AGENTES PARA ESTUDO
st.header("Agentes para estudo")
st.header("Imforme o tema e gere material para estudar:")

tema = st.text_input("Tema de estudo: ", placeholder="Ex.: Algoritimos")
objetivo = st.text_input("Objetivo: ", placeholder="Ex.: Entender conceitos")

executar = st.button("Gerar material")
api_key = "CHAVE_API"

if executar:
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.3)



