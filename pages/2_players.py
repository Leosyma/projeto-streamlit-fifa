#%% Bibliotecas
import streamlit as st
import pandas as pd

#%% Configuração da página
st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

#%% Leitura dos dados
df_data = st.session_state['data']

#%% Criação dos seletores
# Clubes
clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube',clubes)

# Jogadores
df_player = df_data[df_data['Club'] == club]
players = df_player['Name'].unique()
player = st.sidebar.selectbox('Jogador',players)

#%% Estatística dos jogadores
# Nome do jogador
player_stats = df_data[df_data['Name'] == player].iloc[0]

# Foto do jogador
st.image(player_stats['Photo'])

# Nome do jogador
st.title(player_stats['Name'])

# Clube do jogador
st.markdown(f'**Clube:** {player_stats["Club"]}')

# Posição do jogador
st.markdown(f'**Posição:** {player_stats["Position"]}')

# Outros dados do jogador
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Idade:** {player_stats["Age"]}')
col2.markdown(f'**Altura:** {player_stats["Height(cm.)"] / 100}')
col3.markdown(f'**Peso:** {player_stats["Weight(lbs.)"]*0.453:.2f}')
st.divider()

# Overall do jogador
st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

# Métricas do jogador
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")