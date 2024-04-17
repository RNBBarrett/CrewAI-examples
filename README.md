# Crew AI Examples

In simple terms:

1. Crew AI used agents to do work for you.
2. We define tasks and assign those tasks to our agents.
3. The agents may also use tools to assist in their tasks.

### Example 1 local llm no tools

This code uses a simple example of employing two AI agents and a local llm to do work for you, NO TOOLS.

This simple example we setup two agents:

A security researcher.
A security writer.

I used openhermes as my llm running via ollama on my local machine, so no cost to the user.

In the example I do not define any tools for the agents to use, so the agents will rely solely on the latest knowledge captured in the llm.

Example output from the agents:

>In recent months, several emerging cybersecurity vulnerabilities have emerged, posing significant risks to organizations and individuals alike. Among these vulnerabilities are CVE-2021-34527 (Log4Shell/LogJam), CVE-2021-44228 (Krab-OID), CVE-2021-36934 (NinjaLake), and CVE-2021-31267. Each of these vulnerabilities requires immediate attention and action to mitigate their potential impact.

>CVE-2021-34527, also known as Log4Shell or LogJam, is a remote code execution vulnerability that affects the widely used Log4j logging library. Since its discovery in December 2021, this critical vulnerability has been exploited in various attacks, making it one of the most significant cybersecurity threats in recent years. To address this issue, organizations must ensure their systems are updated with the latest patches and monitor their logs for any suspicious activity....

### Example 2 local llm web search tools

In this example we added the option of two search tools, comment out the one you don't use:

from langchain.tools import DuckDuckGoSearchRun #note its going to warn you to use the langchain community edition, that is not working with crewai today at time of writing
from crewai_tools import SerperDevTool

#search_tool = SerperDevTool()
search_tool = DuckDuckGoSearchRun()

Note that the task description for the serper tool task requires Set the input parameter as : search_query in the description. I have a commented out version of task 1 for this.

Also note:
I grab the present date using:
today = date.today()

Textual month, day and year	
current_date = today.strftime("%B %d, %Y")

I supply this date to the task so that the task is looking for news from the present date.

Example output from the agents with search:

>In this issue of our cybersecurity newsletter, we will dive into the most critical vulnerabilities disclosed and addressed in the latest patch releases from Oracle and Microsoft. Let's begin with the Oracle Critical Patch Update for April 2024.

>CVE-2024-2152: Microsoft Windows Remote Code Execution Vulnerability
>---------------------------------------------------------------

>The second critical vulnerability is CVE-2024-2152, which affects multiple Microsoft Windows components. An attacker could exploit this remote code execution vulnerability by sending a specially crafted packet to a targeted system over the network. Once successfully exploited, an attacker gains full control of the affected machine and can install malware or perform further actions at their leisure.

