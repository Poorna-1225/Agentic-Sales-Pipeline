import os
from dotenv import load_dotenv
load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['model_name'] = 'gpt-40-mini'


from crewai import Crew, Agent, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from src.loading_task_agent_configurations import lead_agents_config, lead_tasks_config, email_agents_config, email_tasks_config
from src.pydantic_model_output import LeadScoringResult

# Creating Lead qualification agents, tasks, and crew

lead_data_agent = Agent(
    config = lead_agents_config['lead_data_agent'],
    tools =[SerperDevTool(), ScrapeWebsiteTool()],
)

cultural_fit_agent =  Agent(
    config =  lead_agents_config['cultural_fit_agent'],
    tools = [SerperDevTool(), ScrapeWebsiteTool()],
)

scoring_validation_agent = Agent(
    config = lead_agents_config['scoring_validation_agent'],
    tools = [SerperDevTool(), ScrapeWebsiteTool()],
)

# Creating Tasks
lead_data_task = Task(
  config=lead_tasks_config['lead_data_collection'],
  agent=lead_data_agent
)

cultural_fit_task = Task(
  config=lead_tasks_config['cultural_fit_analysis'],
  agent=cultural_fit_agent
)

scoring_validation_task = Task(
  config=lead_tasks_config['lead_scoring_and_validation'],
  agent=scoring_validation_agent,
  context=[lead_data_task, cultural_fit_task],
  output_pydantic=LeadScoringResult
)

# Creating Crew
lead_scoring_crew = Crew(
  agents=[
    lead_data_agent,
    cultural_fit_agent,
    scoring_validation_agent
  ],
  tasks=[
    lead_data_task,
    cultural_fit_task,
    scoring_validation_task
  ],
  verbose=True
)