import streamlit as st
from revChatGPT.Official import Chatbot

api_key = st.secrets["OPENAI_API_KEY"]
chatbot = Chatbot(api_key)

def ask():
	prompt = st.text_input("请输入你要问的问题")
	return prompt

st.header("ChatGPT猫娘模拟器")
prompt = ask()
if prompt:
	chatbot.ask("你要模仿猫的语言方式回答我的问题。开头加上“主人”，最后加上“喵”。")
	output = chatbot.ask(prompt)["choices"][0]["text"]
	st.write(output)
	chatbot.reset()
