import google.generativeai as genai
import pandas as pd


def get_ai_insights(api_key, drivers_df, vehicles_df, deliveries_df):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are an experienced logistics operations manager.

Analyze the following datasets and prepare the best logistics operation plan.

DRIVERS

{drivers_df.to_string(index=False)}

------------------------------------------------------

VEHICLES

{vehicles_df.to_string(index=False)}

------------------------------------------------------

DELIVERIES

{deliveries_df.to_string(index=False)}

------------------------------------------------------

Your task:

1. Select the best driver for every delivery.
2. Select the most suitable vehicle.
3. Consider:

- Driver availability
- Weekly working hours
- Rest days
- Consecutive trips
- License class
- Driver type
- Vehicle capacity
- Delivery priority
- Fair workload distribution

Return your answer in this format:

Delivery:
Driver:
Vehicle:
Reason:

At the end write:

Overall Operation Evaluation

Fairness Score (0-100)

Potential Risks

Recommendations
"""

    response = model.generate_content(prompt)

    return response.text
