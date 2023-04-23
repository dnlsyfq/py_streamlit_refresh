import streamlit as st
import pandas as pd 

from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit.components.v1 import html

css ='''
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

def navigation_bar():
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["Home", "Upload", "Analytics", 'Settings', 'Contact'],
            icons=['house', 'cloud-upload', "graph-up-arrow", 'gear', 'phone'],
            menu_icon="cast",
            orientation="horizontal",
            styles={
                "nav-link": {
                    "text-align": "left",
                    "--hover-color": "#eee",
                }
            }
        )
        if selected == "Analytics":
            switch_page("Analytics")
        if selected == "Contact":
            switch_page("Contact")

navigation_bar()            

html_string = "<h3>this is an html string</h3>"

st.markdown(html_string, unsafe_allow_html=True)

# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

# Execute your app
st.title("Javascript example")
html(my_html)


html(f'''<input id="example" type="datetime-local"/>''')
# st.markdown('''# **Binance Price App**
# A simple cryptocurrency price app pulling price data from *Binance API*.
# ''')

# st.header('**Selected Price**')

# st.title('Title')
# st.markdown('Markdown')
# st.header('Header')
# st.subheader('Subheader')
# st.caption('Caption')
# st.code('x = 2023')
# st.latex(r'\frac{a}{b}')

# st.image('.jpg')
# st.audio('.mp3')
# st.video('.mp4')





# col1, col2, col3 = st.columns(3)


# st.info('Credit: Created by Chanin Nantasenamat (aka [Data Professor](https://youtube.com/dataprofessor/))')

