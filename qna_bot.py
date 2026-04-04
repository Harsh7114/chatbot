from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
llm = ChatGoogleGenerativeAI(model ="gemini-3-flash-preview")

st.title("🤖 AskBuddy ~ AI QnA Bot")
st.markdown("My QnA bot with Langchain and Google Gemini")

# to make chat window retain in UI\
if "messages" not in st.session_state:
    st.session_state.messages =[]

for message in st.session_state.messages:
    role= message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)




#chat window
query = st.chat_input("Ask Any Question:")
if query:
   st.session_state.messages.append({"role":"user","content":query})

   st.chat_message("user").markdown(query)
   res= llm.invoke(query)
   st.chat_message("ai").markdown(res.content[0]["text"])
   st.session_state.messages.append({"role":"ai","content":res.content[0]["text"]})
if False:
    """while True :
    query = input("User:")

    if query.lower() in ["quit","exit","bye"]:
        print ("GoodBYE >")
        break;

    res= llm.invoke(query)
    print("AI:",res.content[0]["text"]) """

#question = "who is pm of india?"

#res = llm.invoke(question)
#print(parser.invoke(res))


