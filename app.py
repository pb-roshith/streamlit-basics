import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title='Indian Dragon')

st.header('i am india')

st.subheader('drogon')

st.markdown('(body: SupportsStr, unsafe_allow_html: bool = False, *, help: str | None = None) -> DeltaGenerator')

st.latex('y = m*x+c')

st.markdown('_y = m*x+c_') #underscore front and back for italic

st.text('this a dragon')

st.caption('this is big fire dragon')

st.code('''
    def good(a, b):
        print(a+b)
    a,b=map(int,input().split())
    good(a,b)        
''', language='python')

data = pd.read_csv('play_tennis.csv')

st.dataframe(data)

st.table(data)

j = {'a':[1,2,3], 'b':[4,5,6]}

st.json(j)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('AAPL','$70','4')

with col2:
    st.metric('AAPL','$90','-4')

with col3:
    st.metric('speed','89kmph','20%')
    
c = st.checkbox('Submit')

if c:
    st.table(data)
    
    st.radio('pick one: ', ('a', 'b', 'c'))
    
b = st.button('Submit')

if b:
    st.table(data)
    
    st.radio('pick one: ', ('b', 'b', 'c'))
    
cols = list(data.columns)

st.write(cols)

name = st.selectbox('choose a feature', cols)

st.write(name)

c1, c2 = st.columns(2)

with c1:
    a = st.slider('Enter a number 1', 0,100,10)
    
with c2:
    b = st.number_input('Enter a number 2')
    
sub = st.button('ADD')

if sub:
    st.write(a+b)
    
option = st.multiselect('choose your variable', cols)

st.write(option)

ss = st.checkbox('show image')

if ss:
    i = Image.open('hacker.jpeg')
    j = open('ambulance detection.mp4','rb')
    
    st.image(i)
    st.video(j, format='video/mp4')
    
st.success('i am bad')
st.info('i am bad')
st.warning('i am bad')
st.error('i am bad')
st.exception('i am bad')

@st.cache_data
def data_read(data):
    return data.to_csv().encode('utf-8')

c = data_read(data)

st.download_button(label='download', data=c, file_name='play_tennis.csv')

with open("hacker.jpeg", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="hacker.jpeg",
            mime="image/png"
          )