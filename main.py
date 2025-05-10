from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio

browser = Browser(config=BrowserConfig())


llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.0,
)

async def main():
    agent = Agent(
        task="go to google.com and search for a photo of dogs",
        llm=llm,
    )
    result = await agent.run()
    print(result)
    input("Press enter when you are done watching")
    await browser.close()

asyncio.run(main())
