import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='Mercosul Stacked Bar Graph', page_icon='📊', initial_sidebar_state='expanded', layout='wide')
st.title('Stacked Bar Graph 📊')

# Dados
data_folha_arquivos = {
    'Palavras': ['Cultura', 'Integração', 'Identidade', 'Economia', 'Comércio', 'Consumo', 'Ditadura', 'Democracia', 'Autoritarismo'],
    'Número de Arquivos': [9, 6, 33, 92, 124, 11, 25, 38, 2]
}

data_globo_arquivos = {
    'Palavras': ['Cultura', 'Integração', 'Identidade', 'Economia', 'Comércio', 'Consumo', 'Ditadura', 'Democracia', 'Autoritarismo'],
    'Número de Arquivos': [17, 18, 8, 79, 56, 19, 27, 47, 5]
}

data_estadao_arquivos = {
    'Palavras': ['Cultura', 'Integração', 'Identidade', 'Economia', 'Comércio', 'Consumo', 'Ditadura', 'Democracia', 'Autoritarismo'],
    'Número de Arquivos': [17, 42, 7, 129, 109, 31, 25, 50, 6]
}

data_folha_mencoes = {
    'Palavras': ['Cultura', 'Integração', 'Identidade', 'Economia', 'Comércio', 'Consumo', 'Ditadura', 'Democracia', 'Autoritarismo'],
    'Número de Menções': [14, 50, 7, 166, 276, 12, 34, 68, 2]
}

data_globo_mencoes = {
    'Palavras': ['Cultura', 'Integração', 'Identidade', 'Economia', 'Comércio', 'Consumo', 'Ditadura', 'Democracia', 'Autoritarismo'],
    'Número de Menções': [21, 35, 10, 191, 132, 31, 57, 71, 6]
}

data_estadao_mencoes = {
    'Palavras': ['Cultura', 'Integração', 'Identidade', 'Economia', 'Comércio', 'Consumo', 'Ditadura', 'Democracia', 'Autoritarismo'],
    'Número de Menções': [43, 80, 7, 390, 44, 113, 39, 252, 6]
}

# Transforma em df
df_folha_arquivos = pd.DataFrame(data_folha_arquivos)
df_globo_arquivos = pd.DataFrame(data_globo_arquivos)
df_estadao_arquivos = pd.DataFrame(data_estadao_arquivos)

df_folha_mencoes = pd.DataFrame(data_folha_mencoes)
df_globo_mencoes = pd.DataFrame(data_globo_mencoes)
df_estadao_mencoes = pd.DataFrame(data_estadao_mencoes)

# Renomeia coluna
df_folha_arquivos['Jornal'] = 'Folha de São Paulo'
df_globo_arquivos['Jornal'] = 'O Globo'
df_estadao_arquivos['Jornal'] = 'Estadão'

df_folha_mencoes['Jornal'] = 'Folha de São Paulo'
df_globo_mencoes['Jornal'] = 'O Globo'
df_estadao_mencoes['Jornal'] = 'Estadão'

# Unifica df
df_arquivos = pd.concat([df_folha_arquivos, df_globo_arquivos, df_estadao_arquivos])
df_mencoes = pd.concat([df_folha_mencoes, df_globo_mencoes, df_estadao_mencoes])

# Stacked Bar Chart - Arquivos (Altair)
def stacked_bar_chart_arquivos(jornais, df):
    data_filtered = df[df['Jornal'].isin(jornais)]
    
    color_scale = alt.Scale(domain=['Folha de São Paulo', 'O Globo', 'Estadão'],
                            range=['#9c2222', '#22579c', '#108750'])
    
    chart = alt.Chart(data_filtered).mark_bar().encode(
        alt.X('Palavras:N', axis=alt.Axis(title='', labelAngle=0)),
        alt.Y('Número de Arquivos:Q', axis=alt.Axis(title='')),
        alt.Color('Jornal:N', scale=color_scale, title='Jornal')
    ).properties(
        width=600,
        height=400,
        title=''
    )
    
    return chart

# Stacked Bar Chart - Menções (Altair)
def stacked_bar_chart_mencoes(jornais, df):
    data_filtered = df[df['Jornal'].isin(jornais)]
    
    color_scale = alt.Scale(domain=['Folha de São Paulo', 'O Globo', 'Estadão'],
                            range=['#9c2222', '#22579c', '#108750'])
    
    chart = alt.Chart(data_filtered).mark_bar().encode(
        alt.X('Palavras:N', axis=alt.Axis(title='', labelAngle=0)),
        alt.Y('Número de Menções:Q', axis=alt.Axis(title='')),
        alt.Color('Jornal:N', scale=color_scale, title='Jornal')
    ).properties(
        width=600,
        height=400,
        title=''
    )
    
    return chart



################## Arquivos ##################
selected_journals_arquivos = st.multiselect('Selecione os jornais para os quais você deseja ver o total de palavras por arquivos:', ['Folha de São Paulo', 'O Globo', 'Estadão'])
st.markdown("<hr>", unsafe_allow_html=True)

if selected_journals_arquivos:
    st.subheader('Comparação entre:  :orange[Palavras] :red[x] :orange[Arquivos]')
    st.altair_chart(stacked_bar_chart_arquivos(selected_journals_arquivos, df_arquivos), use_container_width=True)
    st.write('')
    st.markdown("<hr>", unsafe_allow_html=True)

################## Menções ##################
selected_journals_mencoes = st.multiselect('Selecione os jornais para os quais você deseja ver o total de palavras por menções:', ['Folha de São Paulo', 'O Globo', 'Estadão'])

if selected_journals_mencoes:
    st.subheader('Comparação entre:  :orange[Palavras] :red[x] :orange[Menções]')
    st.altair_chart(stacked_bar_chart_mencoes(selected_journals_mencoes, df_mencoes), use_container_width=True)
    st.write('')

rodape = '''
<style>
    .autor {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 16px;
        color: white;
    }
</style>
<div class="autor">
    Lucas Martins Lago
</div>
'''
st.markdown(rodape, unsafe_allow_html=True)