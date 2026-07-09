# Technical Architecture

## Overview

RotaNet is designed as a modular AI-powered logistics decision support platform. The system processes logistics data, optimizes delivery routes, analyzes operational performance and generates AI-assisted recommendations.

The architecture is designed to support future scalability while keeping the first MVP simple and maintainable.

---

## System Architecture

```
                User
                  │
                  ▼
        Streamlit Web Interface
                  │
                  ▼
        Data Upload (CSV / Excel)
                  │
                  ▼
         Data Validation Layer
                  │
                  ▼
        Route Optimization Engine
           (Google OR-Tools)
                  │
         ┌────────┴────────┐
         ▼                 ▼
 Route Results      Performance Metrics
         │                 │
         └────────┬────────┘
                  ▼
          AI Recommendation Engine
             (Google Gemini)
                  │
                  ▼
          Dashboard & Reports
```

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Optimization | Google OR-Tools |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Visualization | Plotly |
| Artificial Intelligence | Google Gemini API |
| Mapping | Folium *(planned)* |

---

## Data Flow

1. User uploads logistics data.
2. Data is validated and processed.
3. OR-Tools calculates optimized routes.
4. Performance metrics are generated.
5. Gemini analyzes the optimization results.
6. Dashboard displays maps, KPIs and AI recommendations.

---

## MVP Scope

The first version of RotaNet will include:

- CSV upload
- Route optimization
- Vehicle capacity optimization
- Interactive dashboard
- KPI calculations
- AI-generated operational recommendations

---

## Future Improvements

- Live traffic integration
- Real-time vehicle tracking
- Multi-depot optimization
- Demand forecasting
- ERP integration
- User authentication
- Cloud deployment

