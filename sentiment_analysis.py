from imports import *


def analysis(df):
    dataColumns = st.selectbox('Select a text column for sentiment analysis',df.columns)

    x = []
    
    for text in df[dataColumns]:
        sentiment = ""
        polarity = tb(text).sentiment.polarity
        if polarity < 0:sentiment = "Negative"
        elif polarity == 0: sentiment = "Neutral"
        elif polarity > 0: sentiment = "Positive" 

        x.append({"text":text,"polarity":polarity,"sentiment":sentiment})
 
    df2 = pd.DataFrame(x)

    st.write("Sentiment analysis dataset")
    st.dataframe(df2,use_container_width=True)
    st.write("Download the file as csv")
    st.download_button(label="Download",data=df2.to_csv().encode('utf-8'), file_name="sentiment.csv",mime="text/csv")

    st.write("Data Frame details")
    st.table(df2["sentiment"].value_counts())
    fig,ax = plt.subplots()
    ax.pie(df2["sentiment"].value_counts(),labels=df2["sentiment"].value_counts().index,autopct='%.2f')
    ax.legend()

    st.pyplot(fig)

    st.write("Bar chart")
    fig2,ax2 = plt.subplots()
    ax2.plot(df2["sentiment"].value_counts().index,df2["sentiment"].value_counts(),marker='o')
    st.pyplot(fig2)


    
        

