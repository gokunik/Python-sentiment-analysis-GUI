from imports import *

def visualize(df):
    options = ["Line Chart","Bar chart","Scatter Plot"]
    chart = st.selectbox("Select a chart to plot",options)
    dataColumn = st.multiselect('Select a text column for sentiment analysis',df.columns)
    fig, ax = plt.subplots()
    
    if  (dataColumn):
        if chart == options[0]:
            st.line_chart(data=df[dataColumn])
        elif chart == options[1]:
            st.bar_chart(df[dataColumn])
        elif chart == options[2]:
            if not(len(dataColumn) < 2):
                x = df[dataColumn[0]]
                y = df[dataColumn[1]]
                ax.scatter(x,y,marker='o')
                st.pyplot(fig)
            else:
                st.error("select two columns to plot scatter graph")