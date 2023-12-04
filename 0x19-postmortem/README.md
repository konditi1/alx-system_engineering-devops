Postmortem: Teacher Trek Program Web Outage Incident

Issue Summary:

Duration:

Start Time: 2023-05-15 10:00 AM (UTC)
End Time: 2023-05-15 02:30 PM (UTC)
Impact:

The outage impacted the Teacher Trek Program website, causing users to be unable to access the platform.
User Experience: Users experienced slow loading times and intermittent errors.
Approximately 40% of users were affected.
Root Cause:

The root cause of the outage was identified as an unexpected surge in database queries due to an inefficient code deployment.
Timeline:

10:00 AM: Issue detected through monitoring alerts indicating a spike in error rates and slow response times on the Teacher Trek Program website.

10:15 AM: Investigation initiated by the Development team, suspecting a potential issue with the database.

10:45 AM: Misleading path: Focused on database optimization without identifying the recent code deployment as a potential cause.

11:30 AM: Escalation to the Database Administration team for a more in-depth analysis of database performance.

12:00 PM: Database team found no significant issues. Attention shifted to recent code changes.

12:30 PM: Realization: A recent code deployment introduced inefficient database queries, leading to a surge in resource utilization.

01:00 PM: Incident escalated to the Development and Operations teams for a coordinated effort in addressing the code-related issue.

02:30 PM: Resolution: Code rollback implemented to restore the previous stable version, alleviating the strain on the database and resolving the performance issues.

Root Cause and Resolution:

Root Cause:

The root cause was traced to a recent code deployment that introduced inefficient database queries, causing a surge in resource utilization and impacting the website's performance.
Resolution:

Immediate code rollback implemented to restore the system to the previous stable version, mitigating the impact on database performance and resolving the issues.
Corrective and Preventative Measures:

Improvements/Fixes:

Code review process: Strengthen the code review process to catch inefficient queries and potential performance bottlenecks before deployment.
Automated testing: Enhance automated testing procedures to include performance testing, ensuring that code changes do not negatively impact system resources.
Incident response training: Provide additional training for team members on efficient incident response, emphasizing quick identification and resolution of code-related issues.
Tasks:

Develop deployment checklist: Create a comprehensive deployment checklist to ensure that code changes are thoroughly reviewed for potential performance impacts before release.
Performance monitoring: Implement additional performance monitoring tools to detect and alert on abnormal resource utilization patterns.
Communication protocol: Establish a clear communication protocol for cross-team collaboration during incidents, ensuring timely escalation and resolution.



Postmortem: The Great Teacher Trek Tango - A Web Odyssey

Issue Summary:

Duration:

Start Time: 2023-05-15 10:00 AM (UTC)
End Time: 2023-05-15 02:30 PM (UTC)
Impact:

The Teacher Trek Program website went on an unexpected intergalactic adventure, causing users to experience slow loading times and intermittent errors.
User Experience: Users found themselves in a digital warp zone, unable to access the platform.
Approximately 40% of users were caught in the cosmic chaos.
Root Cause:

The disturbance in the web force was traced back to an unexpected surge in database queries, all thanks to a mischievous code deployment.
Timeline:

10:00 AM: Our monitoring droids started beeping like R2-D2 on espresso, alerting us to a disturbance in the force.

10:15 AM: The Development Jedi Council assembled, suspecting a Sith Lord messing with our database lightsabers.

10:45 AM: Misdirection alert! We chased ghosts in the database Death Star without realizing it was a rebel code deployment causing a disturbance in the galaxy.

11:30 AM: Escalation to the Database Yoda for wisdom on database mysteries.

12:00 PM: Yoda said, "No database issues, there are. Code issues, you must look into, young Padawan."

12:30 PM: Eureka moment: A recent code deployment turned out to be the dark side of the force, introducing inefficient queries and causing chaos in our Jedi temple.

01:00 PM: Lightsabers were unsheathed, and the Development and Operations Jedi united to combat the code-induced stormtroopers.

02:30 PM: The Rebellion prevailed! A code rollback was executed, bringing peace to the galaxy, and the force was balanced once again.

Root Cause and Resolution:

Root Cause:

The dark side of code deployment introduced inefficient database queries, creating a disturbance in the force and disrupting the peace on the Teacher Trek Program website.
Resolution:

The Jedi council swiftly executed a code rollback, vanquishing the dark code forces and restoring order to the galaxy.
Corrective and Preventative Measures:

Improvements/Fixes:

Jedi Code Review: Strengthen our Jedi code review process to catch Sith-like code changes before they infiltrate our servers.
Force-testing: Enhance automated testing procedures to include force-sensitive tests for potential performance bottlenecks.
Lightsaber Training: Provide additional lightsaber training for team members on efficient incident response, ensuring quick identification and resolution of code-related dark forces.
Tasks:

Develop Galactic Deployment Checklist: Create a comprehensive deployment checklist to ensure our code changes don't succumb to the dark side before release.
Force Monitoring: Implement additional force-sensitive monitoring tools to detect abnormal Sith activities in the system.
Galactic Communication Protocol: Establish a clear communication protocol for cross-galactic collaboration during incidents, ensuring timely escalation and resolution.
May the Code be with you, always. 🚀✨

Toggle navigation
You just released the advanced tasks of this project. Have fun!
0x19. Postmortem
DevOps
SysAdmin
 By: Sylvain Kalache
 Weight: 1
 Project over - took place from Nov 6, 2023 6:00 AM to Nov 13, 2023 6:00 AM
 Manual QA review was done by on Nov 25, 2023 11:15 AM
In a nutshell…
Manual QA review: 0.0/13 mandatory & 0.0/1 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%
Concepts
For this project, we expect you to look at this concept:

On-call
Background Context


Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.
Resources
Read or watch:

Incident Report, also referred to as a Postmortem
The importance of an incident postmortem process
What is an Incident Postmortem?
More Info
Manual QA Review
It is your responsibility to request a review for your postmortem from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

Tasks
0. My first postmortem
mandatory
Score: 0.0% (Checks completed: 0.0%)


Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

Issue Summary (that is often what executives will read) must contain:
duration of the outage with start and end times (including timezone)
what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
what was the root cause
Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
how the incident was resolved
Root cause and resolution must contain:

explain in detail what was causing the issue
explain in detail how the issue was fixed
Corrective and preventative measures must contain:

what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
Be brief and straight to the point, between 400 to 600 words

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

Add URLs here:
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x19-postmortem
File: README.md
  
1. Make people want to read your postmortem
#advanced
Score: 0.0% (Checks completed: 0.0%)
We are constantly stormed by a quantity of information, it’s tough to get people to read you.

Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

Add URLs here:
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x19-postmortem
File: README.md
  
Copyright © 2023 ALX, All rights reserved.

