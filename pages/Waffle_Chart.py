import streamlit as st
import matplotlib.pyplot as plt
from pywaffle import Waffle
from data import utils

st.set_page_config(
    page_title='Mercosul Waffle Chart',
    page_icon='🧇'
)
st.title('Waffle Chart 🧇')

st.logo('images/jornal.png')

st.html("""
  <style>
    [alt=Logo] {
      height: 4rem;
    }
  </style>
        """)

######################### Waffle Chart #########################
def plot_waffle_chart(data, years):
    totals = {
        'Folha de São Paulo': sum([data['Folha de São Paulo'][year] for year in years]),
        'O Globo': sum([data['O Globo'][year] for year in years]),
        'Estadão': sum([data['Estadão'][year] for year in years])
    }
    
    total_mentions = sum(totals.values())
    percentages = {jornal: (total / total_mentions) * 100 for jornal, total in totals.items()}
    total_per_year = {year: sum(data[jornal][year] for jornal in data) for year in years}

    colors = {
        'Folha de São Paulo': "#9c2222",
        'O Globo': "#22579c",
        'Estadão': "#108750"
    }

    fig = plt.figure(
        FigureClass=Waffle,
        rows=15,
        columns=10,
        values=totals,
        colors=[colors[jornal] for jornal in totals.keys()],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
        #icons='newspaper',
        icon_size=20,
        icon_legend=True
    )

    ######################### Sidebar #########################
    st.sidebar.header('Total de menções ao :orange[Mercosul] 🗺️ por jornal nos anos selecionados:')
    st.sidebar.subheader(f'Anos selecionados: {", ".join(map(str, years))}')
    total_por_ano = 0
    for jornal, total in totals.items():
        percentage = percentages[jornal]
        if jornal == 'Folha de São Paulo':
            st.sidebar.markdown(f":red[{jornal}]: {total} ({percentage:.2f}%)")
            total_por_ano += total
        if jornal == 'O Globo':
            st.sidebar.markdown(f":blue[{jornal}]: {total} ({percentage:.2f}%)")
            total_por_ano += total
        if jornal == 'Estadão':
            st.sidebar.markdown(f":green[{jornal}]: {total} ({percentage:.2f}%)")
            total_por_ano += total
    st.sidebar.markdown(f':violet[Total]: {total_por_ano} (100%)')
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    st.pyplot(fig)

# Dados
data = utils.waffle_data

# Seleciona Anos
years = st.multiselect('Selecione os anos', list(data['Folha de São Paulo'].keys()))
if years:
    plot_waffle_chart(data, years)

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