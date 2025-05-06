# Constituency Intelligence Service (`constituency-intel`)

## 📌 Overview

The `constituency-intel` service is responsible for gathering, analyzing, and summarizing real-world data about a political district to help candidates align with their constituents. It powers upstream decision-making for messaging, speechwriting, and policy positioning.

This service is the *foundation* of the PoliForge platform, as all candidate actions should stem from real constituent needs.

---

## 🎯 Responsibilities

* Collect publicly available data about a district:

  * Demographics (age, income, race, education, etc.)
  * Voting patterns (past elections)
  * Local and state legislation
  * News articles and public sentiment
* Summarize this data into:

  * Actionable issue overviews
  * District-level profiles
  * Stance deltas between incumbent and public opinion
* Provide input for:

  * Campaign platform planning
  * Talking point generation
  * Voter engagement strategy

---

## 🛠 MVP Scope

### ✅ Phase 1: Basic Data Aggregation (No AI)

* Accept user input: zip code, district, or city/state
* Pull data from:

  * OpenStates API (state legislation)
  * U.S. Census API (demographics)
  * Ballotpedia (scraped if needed)
  * ProPublica Congress API (federal legislation)
* Normalize and store data in internal format
* Expose simple REST API:

  * `GET /district/:id/profile`
  * `GET /district/:id/issues`

### 🔜 Phase 2: AI/RAG Integration (Optional, Later)

* Summarize legislation into issue categories
* Rank issues by frequency + public impact
* Use RAG to pull recent local news sentiment
* Generate issue briefs with source links ("receipts")

---

## 🧰 Tech Stack

| Component     | Tech                                 |
| ------------- | ------------------------------------ |
| Language      | Python (preferred for scraping + ML) |
| Framework     | FastAPI                              |
| Data          | PostgreSQL or SQLite for MVP         |
| External APIs | OpenStates, Census, ProPublica       |
| Optional      | Dockerized CLI tool for testing      |

---

## 🔗 API Design (MVP)

```http
GET /district/wa-22/profile
GET /district/wa-22/issues
```

Example response:

```json
{
  "district": "WA-22",
  "population": 149203,
  "demographics": {
    "median_age": 36.4,
    "income": 54500,
    "education": {
      "bachelor_or_higher": 32.1
    }
  },
  "top_issues": ["housing", "public transit", "opioids"]
}
```

---

## 🧭 Next Tasks

* Create a standalone repo `constituency-intel`
* Create OpenStates + Census API wrappers
* Define internal `DistrictProfile` data model
* Build `/profile` and `/issues` endpoints
* Test with WA-22, TX-35, and NY-14 as case studies
* Generate static JSONs for documentation/demo

---

This service will power the ethical, strategic heart of PoliForge — arming challengers with facts, not guesswork.
