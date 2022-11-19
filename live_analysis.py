from imports import *

def text_analysis(data):
    
    sentiment = ""
    st.write("")
    text = st.text_input(label="Enter some text to analyse",placeholder="Enter text")
    polarity = tb(text).sentiment.polarity

    if text:
        st.write('Word count:',len(text.split(' ')))
        if len(text.split(' ')) > 200:
                st.error("The sentence is to big. word limit is 200 words")   
        else:
                if polarity < 0:
                        sentiment = "Negative"
                        st.write("The text sentiment is Negative")
                elif polarity == 0:
                        sentiment = "Neutral"
                        st.write("The text sentiment is Neutral")
                elif polarity > 0:
                        sentiment = "Positive 😁"
                        st.write("The text sentiment is Positive")

                data.append({"text":text,"polarity":polarity,"sentiment":sentiment})
                st.table(data)

        
    