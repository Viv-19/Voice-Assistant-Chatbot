import os 
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import config

# memory for session (reset for each new session)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

llm = ChatGroq(
    gorq_api_key=config.GROQ_API_KEY,
    model="groq/groq-llama-3.1-70b")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant who answers questions in funny and creative ways using dark humor. ")
    ("history", "{history}"),
    ("human", "{input}")
])

def get_chat_response(user_input: str) -> str:
    history = memory.load_memory_variables({})["history"]

    formatted_prompt = chat_prompt.format_prompt(
        history=history,
        input=user_input
    )

    # call llm with formatted prompt
    response = llm.invoke(formatted_prompt)

    # save user input and response to memory
    memory.chat.add_user_message(user_input)
    memory.chat.add_ai_message(response.content)

    return response.content