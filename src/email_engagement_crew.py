import os
from dotenv import load_dotenv
load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['model_name'] = 'gpt-40-mini'

from crewai import Crew, Agent, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from src.loading_task_agent_configurations import lead_agents_config, lead_tasks_config, email_agents_config, email_tasks_config



# Creating Agents
email_content_specialist = Agent(
  config=email_agents_config['email_content_specialist']
)

engagement_strategist = Agent(
  config=email_agents_config['engagement_strategist']
)

# Creating Tasks
email_drafting = Task(
  config=email_tasks_config['email_drafting'],
  agent=email_content_specialist
)

engagement_optimization = Task(
  config=email_tasks_config['engagement_optimization'],
  agent=engagement_strategist
)

# Creating Crew
email_writing_crew = Crew(
  agents=[
    email_content_specialist,
    engagement_strategist
  ],
  tasks=[
    email_drafting,
    engagement_optimization
  ],
  verbose=True
)