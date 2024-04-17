# Crew AI Examples

### Example 1 local llm no tools

This code uses a simple example of employing two AI agents and a local llm to do work for you.

In simple terms:

1. Crew AI used agents to do work for you.
2. We define tasks and assign those tasks to our agents.
3. The agents may also use tools to assist in their tasks.

This simple example we setup two agents:

A security researcher.
A security writer.

I used openhermes as my llm running via ollama on my local machine, so no cost to the user.

In the example I do not define any tools for the agents to use, so the agents will rely solely on the latest knowledge captured in the llm.

Example output from the agents:

>In recent months, several emerging cybersecurity vulnerabilities have emerged, posing significant risks to organizations and individuals alike. Among these vulnerabilities are CVE-2021-34527 (Log4Shell/LogJam), CVE-2021-44228 (Krab-OID), CVE-2021-36934 (NinjaLake), and CVE-2021-31267. Each of these vulnerabilities requires immediate attention and action to mitigate their potential impact.

>CVE-2021-34527, also known as Log4Shell or LogJam, is a remote code execution vulnerability that affects the widely used Log4j logging library. Since its discovery in December 2021, this critical vulnerability has been exploited in various attacks, making it one of the most significant cybersecurity threats in recent years. To address this issue, organizations must ensure their systems are updated with the latest patches and monitor their logs for any suspicious activity....
