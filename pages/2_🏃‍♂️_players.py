import streamlit as st

df_data = st.session_state["data"]

clubs = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Club', clubs)

df_players = df_data[(df_data['Club'] == club)]

players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Player', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

position = player_stats['Position'].split('>')[-1]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f'**Club** {player_stats["Club"]}')

st.markdown(f'**Position** {position}')

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f'**Age** {player_stats['Age']}')
col2.markdown(f'**Height** {player_stats['Height']}')
col3.markdown(f'**Weight** {player_stats['Weight']}')
st.divider()

st.subheader(f'Overall {player_stats['Overall']}')
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Market Value', value=player_stats['Value'])
col2.metric(label='Weekly renumbering', value=player_stats['Wage']   )
col3.metric(label='Release Clause', value=player_stats['Release Clause']   )

