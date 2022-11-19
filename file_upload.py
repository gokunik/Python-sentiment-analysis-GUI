from imports import *
from chart import *
from sentiment_analysis import *

def upload():
    supported_files = ['csv','excel','xlsx']
    file = st.file_uploader("Upload a file",supported_files)

    if file is not None:
        st.success("File uploaded succesfully",icon='✅')
        file_type = file.name.split(".")[-1]

        if file_type == 'csv':
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        df = df.dropna()
        data_details(df)
        
def data_details(df):
    st.write("Dataset")
    st.dataframe(df,use_container_width=True)
    st.write("Total No. of Index in dataset: ",df.count()[0])
    st.write("Dataset details")
    st.write(df.describe())


    st.write("")
    options = ['Sentiment Analysis','Plot a chart']
    option = st.radio('Select analysis options',options,horizontal=True)

    if option == options[0]:
        analysis(df)
    else:
        visualize(df);
