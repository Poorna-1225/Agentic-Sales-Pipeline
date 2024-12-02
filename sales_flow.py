from crewai import Flow
from crewai.flow.flow import  listen, start
from src.lead_qualification_crew import lead_scoring_crew
from src.email_engagement_crew import email_writing_crew
from IPython.display import IFrame

# Define the SalesPipeline class to represent our sales pipeline flow
class SalesPipeline(Flow):

    @start()
    def fetch_leads(self):
        # pull leads from the database.
        leads =[
            {
                "lead_data": {
                    "name": "João Moura",
                    "job_title": "Director of Engineering",
                    "company": "Clearbit",
                    "email": "joao@clearbit.com",
                    "use_case": "Using AI Agent to do better data enrichment."
                },
            }
        ]

        return leads
    
    @listen('fetch_leads') # now this method will wait for the compeltion of fetch_leads funcition. we can also pass a list of methods as parameter
    def score_leads(self, leads):
        scores = lead_scoring_crew.kickoff_for_each(leads)
        self.state['score_crews_results'] = scores
        return scores
    
    @listen(score_leads)
    def store_leads_score(self, scores):
        # Here we would store the scores in the database
        return scores
    
    @listen(score_leads)
    def filter_leads(self, scores):
        return [score for score in scores if score['lead_score'].score > 70]

    @listen(filter_leads)
    def write_email(self, leads):
        scored_leads = [lead.to_dict() for lead in leads]
        emails = email_writing_crew.kickoff_for_each(scored_leads)
        return emails

    @listen(write_email)
    def send_email(self, emails):
        # Here we would send the emails to the leads
        return emails
    


salespipeline_flow = SalesPipeline()

emails = salespipeline_flow.kickoff()

salespipeline_flow.plot()

IFrame(src='./flow_images/crewai_flow.html', width='150%', height=600)

import pandas as pd

# Convert UsageMetrics instance to a DataFrame
df_usage_metrics = pd.DataFrame([salespipeline_flow.state["score_crews_results"][0].token_usage.dict()])

# Calculate total costs
costs = 0.150 * df_usage_metrics['total_tokens'].sum() / 1_000_000
print(f"Total costs: ${costs:.4f}")

# Display the DataFrame
#df_usage_metrics