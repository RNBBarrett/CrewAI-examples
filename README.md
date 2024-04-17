### A simple crewai example.

This code uses a simple example of employing two AI agents and a local llm to do work for you.

In simple terms:

-Crew AI used agents to do work for you.
-We define tasks and assign those tasks to our agents.
-The agents may also use tools to assist in their tasks.

This simple example we setup two agents:

A security researcher.
A security writer.

I used openhermes as my llm running via ollama on my local machine, so no cost to the user.

In the example I do not define any tools for the agents to use to go out and do searches on the web, so in this simple example the agents will rely on the latest knowledge in the llm.

Example output from the agents:

>In recent months, several emerging cybersecurity vulnerabilities have emerged, posing significant risks to organizations and individuals alike. Among these vulnerabilities are CVE-2021-34527 (Log4Shell/LogJam), CVE-2021-44228 (Krab-OID), CVE-2021-36934 (NinjaLake), and CVE-2021-31267. Each of these vulnerabilities requires immediate attention and action to mitigate their potential impact.

>CVE-2021-34527, also known as Log4Shell or LogJam, is a remote code execution vulnerability that affects the widely used Log4j logging library. Since its discovery in December 2021, this critical vulnerability has been exploited in various attacks, making it one of the most significant cybersecurity threats in recent years. To address this issue, organizations must ensure their systems are updated with the latest patches and monitor their logs for any suspicious activity....
