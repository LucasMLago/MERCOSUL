import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from data import utils

st.set_page_config(page_title='Mercosul Word Cloud', page_icon='☁️', initial_sidebar_state='expanded')
st.title('Word Cloud ☁️')

st.logo('images/jornal.png')

st.html("""
  <style>
    [alt=Logo] {
      height: 4rem;
    }
  </style>
        """)

checkbox_style = """
<style>
    .stCheckbox input[type=checkbox] {
        accent-color: green;
    }
    .centered-line {
        width: 100%;
        text-align: center;
    }
</style>
"""
st.markdown(checkbox_style, unsafe_allow_html=True)

# Dados
data = utils.word_cloud_data

df = pd.DataFrame(data)

# Cores para as palavras
colors = {
    'Economia': 'dodgerblue',
    'Comércio': 'orange',
    'Democracia': 'green',
    'Integração': 'red',
    'Ditadura': 'purple',
    'Consumo': 'brown',
    'Cultura': 'magenta',
    'Identidade': 'grey',
    'Autoritarismo': 'black'
}

# Word Cloud
def generate_wordcloud(data, colors):
    wordcloud = WordCloud(width=800, height=400, background_color='white', color_func=lambda *args, **kwargs: colors[args[0]]).generate_from_frequencies(data)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# Sidebar Legend
def display_legend(data, column_name):
    sorted_data = df.sort_values(by=column_name, ascending=False)
    st.sidebar.subheader(f'Legenda - {column_name}')
    for palavra, numero in zip(sorted_data['Palavras'], sorted_data[column_name]):
        color = colors[palavra]
        st.sidebar.markdown(f"<p style='color: {color}; margin: 0;'>{palavra}: {numero}</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)


# Checkboxes para selecionar qual Word Cloud mostrar
col1, col2 = st.columns(2)
with col1:
    show_files_wc = st.checkbox('Word Cloud - Arquivos', value=True)
with col2:
    show_mentions_wc = st.checkbox('Word Cloud - Menções')

# Word Cloud com legendas
if show_files_wc:
    st.subheader('Word Cloud - Número de Arquivos')
    col1, col2 = st.columns([2, 1])
    with col1:
        file_wordcloud_data = dict(zip(df['Palavras'], df['Número de Arquivos']))
        generate_wordcloud(file_wordcloud_data, colors)
    with col2:
        display_legend(df, 'Número de Arquivos')
    st.markdown("<hr>", unsafe_allow_html=True)

if show_mentions_wc:
    st.subheader('Word Cloud - Número de Menções')
    col1, col2 = st.columns([2, 1])
    with col1:
        mentions_wordcloud_data = dict(zip(df['Palavras'], df['Número de Menções']))
        generate_wordcloud(mentions_wordcloud_data, colors)
    with col2:
        display_legend(df, 'Número de Menções')
    st.markdown("<hr>", unsafe_allow_html=True)

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
