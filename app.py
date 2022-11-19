from imports import *
from file_upload import *
from live_analysis import *

data = []

st.title('Python sentiment analysis')

st.write('')
options = ['Live analysis using text','Analysis using file upload']
option = st.radio('Options for analysis',options,index=0,horizontal=True)

if option == options[0]:
    text_analysis(data) 

elif option == options[1]:
    upload()
