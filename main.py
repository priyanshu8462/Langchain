from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

def main():
    prompt = PromptTemplate.from_template("Explain about {topic}")
    #above line can be also be written as
    prompt = PromptTemplate(template="Explain about topic {topic}")

    new_prompt = prompt.format(topic="Langchain")
    print("Hello from langchain-course! ")

    chain = model.invoke(new_prompt)
    print(chain)


if __name__ == "__main__":
    main()
