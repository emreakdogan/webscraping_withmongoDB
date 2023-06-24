# import required libraries
import streamlit as st
import os
import pandas as pd
import pymongo
import api_key
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

# connect mongodb
client = pymongo.MongoClient('mongodb://localhost:27017')

# select database
db = client['smartmaple']

# select collection
collection = db['kitapyurdu']

# get data
data = collection.find()

# get url
title = []
writer = []
publisher = []
price = []
for item in data:
    title.append(item['title'])
    writer.append(item['writers'])
    publisher.append(item['publisher'])
    price.append(item['price'])

dataframe = pd.DataFrame({"title":title,"writer":writer,"publisher":publisher,"price":price})
dataframe.to_csv("veri.csv",index=False)


# load llm and agent for ours data
os.environ['OPENAI_API_KEY'] =  api_key.key

agent = create_csv_agent(
    OpenAI(temperature=0),
    "veri.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
# streamlit app edit
st.title("🤖BookStore-Search")
query = st.text_input('Ask a question about book!')
if query:
    st.write("ANSWER:")
    st.write(agent.run(query))
    st.write("First 20 Data")
    st.write(pd.read_csv("veri.csv").head(20))
    

    


