# Technical Architecture

## System Overview

RotaNet is designed as a modular AI-powered logistics decision support platform.

The system consists of independent modules responsible for data processing, optimization, visualization and artificial intelligence. This architecture allows each component to be developed and maintained separately while keeping the platform scalable.

---

## System Architecture

```
                User
                  │
                  ▼
        Streamlit Web Interface
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
 Dataset Loader  Optimization  AI Engine
                  Engine
        │         │         │
        └─────────┼─────────┘
                  ▼
          Analytics Dashboard
                  │
                  ▼
             Maps & Reports
```

---

## Frontend

The frontend is built with Streamlit.

Responsibilities:

- User interface
- Dataset upload
- Parameter selection
- Dashboard visualization
- Route visualization
- KPI presentation

---

## Backend

The backend handles business logic and optimization.

Responsibilities:

- Data processing
- Route optimization
- Distance calculation
- Fleet utilization analysis
- Cost estimation

---

## Artificial Intelligence Module

The AI module is responsible for generating operational insights.

Planned capabilities:

- Route explanation
- Decision support
- Alternative scenario recommendations
- Risk analysis
- Operational summaries

Technology:

- Google Gemini API

---

## Optimization Engine

The optimization engine is based on Google OR-Tools.

Optimization objectives:

- Minimize total distance
- Increase vehicle utilization
- Reduce transportation costs
- Improve operational efficiency

---

## Data Layer

Supported formats:

- CSV
- Excel (.xlsx)

Future support:

- SQL Database
- REST API
- ERP Integration

---

## Visualization

Visualization technologies:

- Plotly
- Folium
- OpenStreetMap

Displayed information:

- Routes
- Vehicle locations
- KPIs
- Operational metrics

---

## Project Structure

```
RotaNet/
│
├── ai/
├── assets/
├── backend/
├── datasets/
├── docs/
├── frontend/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Future Integrations

- Google Maps API
- Traffic Data
- Weather Services
- ERP Systems
- Fleet Management Systems
- Cloud Deployment
- 
