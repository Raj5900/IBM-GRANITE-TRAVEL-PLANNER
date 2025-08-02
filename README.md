🧠 IBM Granite Travel Planner Agent
A smart AI-powered travel assistant that generates detailed 3-day itineraries for any destination using IBM Granite (Watsonx) via FastAPI.

✈️ Features
Generates a realistic 3-day travel plan based on your chosen destination and daily budget

Suggests:

Morning, afternoon & evening activities

Hotel/hostel options

Local meal recommendations

Cost estimates per day

Begins with a weather summary of the destination for the past 5 days

Built with FastAPI + Jinja2 for a clean UI

Powered by IBM Granite Foundation Model (via langchain_ibm)

Local browser interface for quick interaction

🛠 Tech Stack
🧠 IBM Granite (13B Instruct v2) via Watsonx

🐍 FastAPI (Backend)

🧩 Langchain IBM integration

🌐 HTML + CSS (Jinja2 Templates)

☁️ IBM Cloud Lite (dev/testing)

🔧 Prerequisites
Python 3.10+

pip install -r requirements.txt

IBM Watsonx credentials:

WATSONX_API_KEY

WATSONX_PROJECT_ID

WATSONX_URL


# 1. Clone the repo
git clone https://github.com/your-username/ibm-granite-travel-planner.git
cd ibm-granite-travel-planner

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Watsonx credentials in a `.env` file
WATSONX_API_KEY=your_api_key
WATSONX_PROJECT_ID=your_project_id
WATSONX_URL=https://your-region.ml.cloud.ibm.com

# 4. Run the app
uvicorn app:app --reload

# 5. Open in browser
http://127.0.0.1:8000



Project Structure


├── app.py                  # FastAPI backend
├── granite_agent.py        # IBM Granite integration
├── templates/
│   └── index.html          # Jinja2 UI template
├── static/                 # Optional static files
├── .env                    # IBM Watsonx credentials
├── requirements.txt
└── README.md


OUTPUT UI

<img width="653" height="640" alt="Screenshot 2025-08-03 010836" src="https://github.com/user-attachments/assets/076bd400-bc91-41b1-bfa5-27f3c8a3fc69" />

<img width="705" height="358" alt="Screenshot 2025-08-03 010747" src="https://github.com/user-attachments/assets/fab9d607-1ff0-493b-a3a8-c658e7888658" />
<img width="564" height="769" alt="Screenshot 2025-08-03 012136" src="https://github.com/user-attachments/assets/15860563-bca4-4494-b095-363fd0920d67" />



