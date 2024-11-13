
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI 
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter influencer assistant tasked with writing excellent twitter posts"
            " Generate the best twitter post possisble for the user's request."
            " If the user provides critique, respond with a revised version of your previous attempts."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOllama(model="llama3.2")
generate_chain = generation_prompt | llm | StrOutputParser()
reflect_chain = reflection_prompt | llm | StrOutputParser()

#llm = ChatOpenAI()
#generate_chain = generation_prompt | llm 
#relect_chain = reflection_prompt | llm 