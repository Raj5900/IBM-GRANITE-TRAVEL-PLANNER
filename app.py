from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from granite_agent import get_itinerary

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.get("/plan", response_class=HTMLResponse)
def plan_trip(request: Request, destination: str, budget: int):
    result = get_itinerary(destination, budget)

    # Format plan into readable HTML
    formatted_plan = ""
    if isinstance(result, dict) and "plan" in result:
        for day, activities in result["plan"].items():
            formatted_plan += f"<h3>{day}</h3><p>{activities}</p><br>"
    else:
        formatted_plan = "<p>Could not generate itinerary. Please try again.</p>"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": formatted_plan,
        "destination": destination,
        "budget": budget
    })
