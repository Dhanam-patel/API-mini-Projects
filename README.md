
# API Mini Projects

A curated collection of small, focused API projects that document my learning journey in backend API development, machine learning model serving, and simple interactive frontends using Streamlit.

Each project in this repository is a compact, self-contained example that demonstrates real-world integration patterns: API design (FastAPI), model serialization and serving (pickle), data validation (Pydantic), and lightweight UIs (Streamlit).

---

## Why this repository

This repository is my playground to build and share mini API projects that solve narrow problems and illustrate practical patterns. The goals are:

- Learn and demonstrate backend API best practices using FastAPI.
- Show how to serve ML models with serialized artifacts (pickle / joblib).
- Provide simple interactive frontends using Streamlit for quick demos.
- Offer reproducible examples you can run locally and adapt.

---

## Quick overview

- Repo name: `API-mini-Projects` (owner: `Dhanam-patel`)
- Main focus: API design, ML model serving, interactive demos.

---

## List of Projects

- Insurance Premium ML API 

---
## Global setup (how to get the repo and environment ready)

These steps are written for Windows PowerShell (your default shell). They are copy-paste friendly.

1. Clone the repository:

```powershell
git clone https://github.com/Dhanam-patel/API-mini-Projects.git
cd "API-mini-Projects"
```

2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies for a specific project before running that project (instructions below). Each project typically includes its own `requirements.txt`.

Notes:

- Replace `Dhanam-patel` with your GitHub user or use your fork/clone URL.
- If you prefer virtualenv/conda, use those instead.

---

## Projects

This repository contains one (or more) sub-project directories. Each project has its own files and README (if present). Below is a detailed description of the included project(s).

### Insurance Premium ML

Brief: A compact FastAPI service that predicts an insurance premium category using a serialized ML model. A Streamlit app demonstrates the prediction UI.

Key concepts & technologies:

- FastAPI for the API endpoints and auto-generated interactive docs (`/docs`, `/redoc`).
- Pydantic for request validation and computed fields.
- Scikit-learn model served from a pickle file (`Model/model.pkl`) loaded in `Model/Predict.py`.
- Streamlit for a simple interactive frontend (`Streamlit/app.py`).

Main files and their roles:

- `api.py` — FastAPI application and route definitions (root, health, predict endpoints).
- `Model/Predict.py` — loads `Model/model.pkl` via `pickle`, provides a `Predict()` helper and exposes `Model_Version` and `Model_Loaded` flags.
- `Model/model.pkl` — the serialized ML model used by the API (expected to be located in the `Model` folder).
- `Schema/User_Input.py` — Pydantic model that defines input fields and computed properties (BMI, age group, life risk, city tier).
- `config/City_Tier.py` — helper lists of Tier 1 and Tier 2 cities used by the schema.
- `Streamlit/app.py` — a small UI that collects user input and (optionally) calls the API to show predictions.
- `requirements.txt` — project dependencies (`fastapi`, `uvicorn[standard]`, `scikit-learn`, `pandas`, `pydantic`, etc.).

How to run this project locally

1. Change into the project folder and create/activate a virtual environment (if not already done):

```powershell
cd "Insurance Premium ML"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the API (FastAPI + Uvicorn):

```powershell
# from the project root (Insurance Premium ML)
uvicorn api:app --reload --port 8000
```

After the API starts, open the auto-generated Swagger UI at:

http://127.0.0.1:8000/docs

And Redoc at:

http://127.0.0.1:8000/redoc

4. Run the Streamlit frontend (in a separate terminal/session):

```powershell
cd "Insurance Premium ML"
.\.venv\Scripts\Activate.ps1   # if needed
streamlit run Streamlit/app.py
```

The Streamlit UI will open in your browser (or show a local URL in the terminal).

Project-specific README: None included. This repository README contains run instructions for this project.

---

## Usage examples

API endpoints (Insurance Premium ML):

- GET `/` — root message.
- GET `/health` — returns service status, model version, and whether the model loaded.
- POST `/predict` — accepts the validated JSON user input and returns a predicted insurance premium category.

Example POST (curl):

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @- <<'JSON'
{
	"age": 30,
	"weight": 70,
	"height": 1.7,
	"income_lpa": 6.5,
	"smoker": false,
	"city": "Mumbai",
	"occupation": "private_job"
}
JSON
```

Or use the interactive Swagger UI at `/docs` to test requests.

Notes & common issues:

- Ensure `Model/model.pkl` is present. `Model/Predict.py` expects that file to exist and will load it with `pickle`.
- If you get import errors, check that you are running commands from the project folder and that the virtual environment is active.

---

## Contributing

Contributions, suggestions, and improvements are welcome. A simple workflow:

1. Open an issue describing the enhancement or bug.
2. Create a feature branch from `main`: `git checkout -b feat/your-change`.
3. Make changes, add tests where applicable, and ensure code runs locally.
4. Open a pull request with a clear description of what you changed and why.

Guidelines:

- Keep each mini-project small and focused.
- Prefer readable code and explicit comments where helpful.
- Add or update project README entries when you add new projects or change run steps.

---

## License

This repository is provided under the MIT License. See the `LICENSE` file for details (if you prefer a different license, update this section accordingly).

---

## Contact

- Owner: `Dhanam-patel` (GitHub profile: https://github.com/Dhanam-patel)
- For questions, open an issue or contact via the GitHub profile.

---

Thank you for checking out this collection of API mini-projects — I hope they help you prototype ideas quickly and learn practical integration patterns.
