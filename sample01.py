import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

############################################
# progress bar
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

############################################
# layout

left_column, right_column = st.columns(2)

button = left_column.button('Show String')
if button:
    right_column.write(f"Button is {button}.")

expander = st.expander('FAQ1')
expander.write('Answer1.')


############################################
# layout

option1 = st.sidebar.slider('Volume',0,100,50,key='opt1')
'Slide value1 is', option1, '.'
option2 = st.sidebar.slider('Volume',0,100,50,key='opt2')
'Slide value2 is', option2, '.'

option = st.sidebar.text_input('What is your hobby?')

'Your hobby is ', option, '.'