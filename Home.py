import streamlit as st
 
st.set_page_config(
    page_title='Mercosul',
    page_icon='🗺️',
    initial_sidebar_state='expanded'
)
 
st.title('Home 🌎')
introducao = '''
- Seleção de três jornais brasileiros de alta circulação para investigar seu impacto na formação da Opinião Pública em temas políticos nacionais envolvendo o :orange[Mercosul]
    - :blue[O Globo]
    - :red[Folha de São Paulo]
    - :green[Estadão]
- Identificação da :red[Folha de São Paulo] como o jornal com maior circulação nacional entre 2016 e 2018, seguido por :blue[O Globo] e :green[Estadão]
- Investigação sobre o :orange[Mercosul], focando na invisibilização de sua ação cultural pela mídia brasileira devido a um suposto viés neoliberal
- Uso de nove palavras-chave divididas em grupos (*cultural*, *político* e *econômico*) para analisar como os jornais abordam o Mercosul em seus conteúdos
'''
st.markdown(introducao)

st.write('')

st.image(
    'images/LogoMERCOSUL_PT.png', 
    caption='Mercado Comum do Sul é uma organização intergovernamental regional fundada a partir do Tratado de Assunção em 26 de março de 1991.',
    use_column_width=True)

radape = '''
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
 
st.markdown(radape, unsafe_allow_html=True)