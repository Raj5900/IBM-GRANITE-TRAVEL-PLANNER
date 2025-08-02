from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    url=os.getenv("WATSONX_URL"),
    apikey=os.getenv("WATSONX_API_KEY"),
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    params={
        "max_new_tokens": 1000,
        "temperature": 0.7
    }
)

def format_plan_text(plan_dict: dict) -> str:
    html = ""
    for day, content in plan_dict.items():
        html += f"<h3>{day}</h3><p>{content}</p><br>"
    return html

def get_itinerary(destination: str, budget: int):
    prompt = f"""
You are a travel planning assistant.

Plan a detailed 3-day itinerary for a trip to {destination} with a budget of ₹{budget} per day.
also write about the weather of last 5 days
For each day, provide:
- Morning activity
- Afternoon activity
- Evening activity
- Hotel/hostel suggestion
- Meal recommendations
- Approximate cost

Ensure clear day-wise formatting and avoid repeating the same activities every day.
"""

    response = llm.invoke(prompt)

    print("🔁 RAW Granite Response:\n", response)  # ✅ ADD THIS LINE

    cleaned = response.replace("\\n", "\n").replace("\n", " ")
    parts = cleaned.split("Day ")

    plan = {}
    for part in parts[1:]:
        day_number = part.split(":")[0].strip()
        day_content = part[len(day_number)+1:].strip()
        plan[f"Day {day_number}"] = day_content

    return {
        "destination": destination,
        "budget": budget,
        "plan": plan
    }