# AI-Driven Lead Qualification and Nurturing System

This project presents a sophisticated approach to lead qualification and nurturing, leveraging the power of CrewAI's multi-agent orchestration framework. By deploying a network of specialized AI agents, the system automates and optimizes the process of gathering lead data, assessing cultural fit, scoring leads based on predefined criteria, and crafting personalized follow-up emails. This granular approach ensures a data-driven and highly tailored experience for each prospective lead, ultimately enhancing conversion rates and streamlining lead management workflows.

## Workflow Stages

The system's workflow comprises five distinct stages, each handled by a dedicated AI agent:

1. **Lead Data Acquisition and Analysis:** The `lead_data_agent` meticulously collects and analyzes both personal and company-level data for each lead, encompassing attributes such as job title, company size, industry, revenue, and market presence.

2. **Cultural Fit Evaluation:** The `cultural_fit_agent` delves into the nuances of the lead's company culture, assessing its alignment with the organization's values and strategic objectives. This ensures that potential partnerships are not only strategically sound but also culturally compatible, fostering long-term success.

3. **Lead Scoring and Validation:** The `scoring_validation_agent` aggregates the acquired data and applies predefined criteria to assign a lead score. This score reflects the lead's overall potential and guides subsequent engagement strategies. The agent also rigorously validates the scoring process to maintain accuracy and consistency.

4. **Personalized Email Crafting:** The `email_content_specialist` leverages the gathered insights to craft a highly personalized email that resonates with the lead's individual interests and company profile. This tailored approach ensures that communication is relevant and engaging.

5. **Engagement Optimization:** The `engagement_strategist` refines the email draft, strategically incorporating strong calls to action (CTAs) and engagement hooks to encourage immediate action from the lead. This optimization maximizes the potential for conversion and fosters prompt follow-up.

## Getting Started

1. **Environment Setup:**
   - Create a virtual environment using conda: `conda create -n your_env_name python=3.9`
   - Activate the environment: `conda activate your_env_name`

2. **Dependency Installation:**
   - Install the required packages: `pip install -r requirements.txt`

3. **API Key Configuration:**
   - Create a `.env` file in your project directory.
   - Add your API keys as environment variables in the `.env` file:

     ```
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY = your_seper_api_key
     # Add other API keys as needed
     ```

4. **Execution:**
   - Run your main script(sales_flow.py) to initiate the workflow.
