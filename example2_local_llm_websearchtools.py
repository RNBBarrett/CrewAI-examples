import os
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain.tools import DuckDuckGoSearchRun
from datetime import date

today = date.today()

# Textual month, day and year	
current_date = today.strftime("%B %d, %Y")

#concept crewai uses AGENTS to accomplish TASKS, these agents can optionally use TOOLS
#you define your AGENTS
#you define your TASKS
#you send them off to do what you have asked!

#define local llm
ollama_mistral = Ollama(model="mistral")

#define tools
#search_tool = SerperDevTool()
search_tool = DuckDuckGoSearchRun()

#if you choose to use serper, you must sign up for a key
#os.environ["SERPER_API_KEY"] = "API_KEY_HERE" #https://serper.dev/

#define the agent - note no tools so its only going to tell you what it knows
researcher = Agent(
    role='researcher',
    goal='Uncoverer very detailed information about new CVEs that came out today',
    backstory='You are a Top CyberSecurity researcher tasked with finding highly detailed information about new CVEs',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_mistral
)

#define the agent - note no tools so its only going to tell you what it knows
writer = Agent(
    role='A writer of a popular cybersecurity newsletter',
    goal='Generate a detailed Cybersecurity newsletter covering the most Critical CVEs that came out today',
    backstory='You are a Top CyberSecurity writer known for writing detailed and engaging newsletters supplying technical depth in a concise manner',
    verbose=True,
    allow_delegation=False,
    llm=ollama_mistral
)

#define the tasks
#task1 = Task(description='Investigate emerging cybersecurity vulnerabilities. Set the input parameter as : search_query', agent=researcher, expected_output='A bulleted list of all of the latest vulnerabilities')
task1 = Task(description='Gather data about new Critical CVEs from todays date '+current_date, agent=researcher, expected_output='A bulleted list of todays CVEs')
task2 = Task(description='Write a compelling and detailed newsletter about the most critical CVEs that came out today, make sure each CVE recieves its own section the newsletter', agent=writer, expected_output='A refined finalized version of report in text format')

#get working
crew = Crew(
    agents=[researcher,writer],
    tasks=[task1,task2],
    verbose=2,
    #process=Process.sequential
)

result = crew.kickoff()

