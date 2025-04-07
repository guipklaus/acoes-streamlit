# arquivo: acoes_streamlit.py

import streamlit as st
import matplotlib.pyplot as plt
from random import randint

st.set_page_config(page_title="Simulador de Ações", layout="wide")

# Inicializar sessão
if "dias" not in st.session_state:
    st.session_state.dias = 1
    st.session_state.acao1 = []
    st.session_state.acao2 = []
    st.session_state.acao3 = []

# Botão para atualizar o gráfico
if st.button("Próximo dia"):
    st.session_state.dias += 1

    # Simular variação de cada ação
    def nova_variacao(lista):
        variacao = randint(-10, 10)
        novo = lista[-1] + variacao if lista else randint(80, 120)
        lista.append(novo)

    nova_variacao(st.session_state.acao1)
    nova_variacao(st.session_state.acao2)
    nova_variacao(st.session_state.acao3)

# Criar gráfico
fig, ax = plt.subplots()

dias_range = list(range(1, st.session_state.dias))

ax.plot(dias_range, st.session_state.acao1, label="Ação 1", color="blue")
ax.plot(dias_range, st.session_state.acao2, label="Ação 2", color="orange")
ax.plot(dias_range, st.session_state.acao3, label="Ação 3", color="green")

ax.set_xlim(0, max(10, st.session_state.dias))

# Ajustar Y dinamicamente com margem
todos_os_valores = st.session_state.acao1 + st.session_state.acao2 + st.session_state.acao3
if todos_os_valores:
    minimo = min(todos_os_valores)
    maximo = max(todos_os_valores)
    margem = (maximo - minimo) * 0.1 + 1
    ax.set_ylim(minimo - margem, maximo + margem)
else:
    ax.set_ylim(90, 110)

ax.set_title("Variação das Ações")
ax.set_xlabel("Dias")
ax.set_ylabel("Valor")
ax.legend()

# Adicionar os valores no canto superior esquerdo do gráfico
if st.session_state.acao1:
    texto_valores = (
        f"Ação 1: {st.session_state.acao1[-1]:.2f}\n"
        f"Ação 2: {st.session_state.acao2[-1]:.2f}\n"
        f"Ação 3: {st.session_state.acao3[-1]:.2f}"
    )
    ax.text(
        0.01, 0.98, texto_valores,
        transform=ax.transAxes,
        verticalalignment='top',
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray')
    )

# Mostrar gráfico
st.pyplot(fig)
