# Rayeva AI Systems Assignment

## Overview

This project implements AI-powered modules designed to automate sustainable commerce workflows.

The system reduces manual catalog effort and improves B2B proposal generation using AI models integrated with structured business logic.

Two modules have been fully implemented:

- AI Auto Category & Tag Generator  
- AI B2B Proposal Generator  

The backend is built using **FastAPI** and follows a modular architecture separating API routes, AI services, prompt design, and database operations.

---

# System Architecture Overview

The system follows a layered architecture to separate AI logic from application logic.

System Flow:

Client Request  
↓  
FastAPI Routes  
↓  
Service Layer (Business Logic)  
↓  
Prompt Builder  
↓  
AI Model API  
↓  
Response Parser  
↓  
Database Storage  
↓  
JSON Response

Main Components:

- **Routes** → Handles API endpoints  
- **Services** → AI integration and business logic  
- **Prompts** → Prompt engineering for AI tasks  
- **Database** → SQLAlchemy models for persistence  
- **Utils** → Logging and helper functions  

---

# Project Structure


rayeva-ai-system
│
├── backend
│ ├── main.py
│
│ ├── routes
│ │ ├── category_routes.py
│ │ └── proposal_routes.py
│
│ ├── services
│ │ ├── ai_category_service.py
│ │ └── ai_proposal_service.py
│
│ ├── prompts
│ │ ├── category_prompt.py
│ │ └── proposal_prompt.py
│
│ ├── database
│ │ ├── db.py
│ │ ├── models.py
│ │ └── schemas.py
│
│ ├── utils
│ │ └── logger.py
│
│ └── logs
│ └── ai_logs.txt
│
├── requirements.txt
├── README.md
└── .env.example


---

# AI Prompt Design

AI modules rely on carefully designed prompts to ensure structured and reliable outputs.

The prompts instruct the AI model to:

- Use predefined product categories  
- Generate structured JSON responses  
- Suggest SEO tags and sustainability filters  
- Respect business constraints such as budget limits  

Example prompt logic for category generation:


You are an AI product catalog assistant for a sustainable commerce platform.

Classify the product into one of the allowed categories and generate metadata.

Allowed Categories:
Personal Care
Home
Kitchen
Office
Stationery
Packaging

Return ONLY valid JSON with:

category
sub_category
tags
sustainability filters


This prompt design ensures consistent AI responses that can be parsed and stored safely in the database.

---

# Module 1 — AI Auto Category & Tag Generator

This module automatically generates product metadata from product descriptions.

### Features

- Auto-assign primary category from predefined list  
- Suggest sub-category  
- Generate SEO tags (5–10 tags)  
- Suggest sustainability filters such as plastic-free, biodegradable, recycled etc.  
- Return structured JSON output  
- Store results in database  

### Example Input

```json
{
  "name": "Bamboo Toothbrush",
  "description": "Eco friendly biodegradable bamboo toothbrush"
}
Example Output
{
  "category": "Personal Care",
  "sub_category": "Oral Care",
  "tags": [
    "bamboo toothbrush",
    "eco friendly",
    "plastic free",
    "biodegradable",
    "sustainable"
  ],
  "sustainability": [
    "plastic-free",
    "biodegradable"
  ]
}

The generated metadata is stored in the database to automate product catalog management.

Module 2 — AI B2B Proposal Generator

This module generates sustainable corporate gifting proposals based on budget constraints.

Features

Suggested sustainable product mix

Budget allocation within provided limit

Estimated cost breakdown

Sustainability impact positioning summary

Structured JSON output

Example Input
{
  "budget": 50000,
  "event": "Corporate sustainability event"
}
Example Output
{
  "products": [
    {"name": "Reusable Water Bottles", "quantity": 200, "cost": 10000},
    {"name": "Eco Friendly Notebooks", "quantity": 200, "cost": 8000},
    {"name": "Sustainable Plant Kits", "quantity": 100, "cost": 12000}
  ],
  "total_cost": 45000,
  "impact_summary": "This proposal promotes reusable and eco friendly products, reducing plastic waste and supporting sustainable practices."
}
Architecture for Additional Modules
Module 3 — AI Impact Reporting Generator

Architecture concept:


Order Data
↓
Impact Calculation Engine
↓
AI Impact Summary Generator
↓
Impact Report


This module would estimate environmental metrics such as:

Plastic saved

Carbon emissions avoided

Local sourcing benefits

The generated impact report would be stored with the order data.

Module 4 — AI WhatsApp Support Bot

Architecture concept:


Customer (WhatsApp)
↓
WhatsApp API / Twilio
↓
FastAPI Support Bot
↓
AI Intent Detection
↓
Business Logic
↓
Database
↓
Response to Customer


Possible capabilities:

Order status queries

Return policy assistance

Escalation of refund issues

Conversation logging

API Endpoints
Generate Product Category
POST /generate-category

Generates category, tags and sustainability filters.

Generate B2B Proposal
POST /generate-proposal

Generates sustainable product proposal within a given budget.

Technical Features

Structured JSON AI outputs

Prompt and response logging

Environment-based API key management using .env

Clean separation of AI logic and application logic

Error handling and validation

Tech Stack

Backend: FastAPI
Database: SQLite + SQLAlchemy
AI Integration: LLM API
Environment Management: python-dotenv

Running the Project
Install dependencies
pip install -r requirements.txt
Run the server
uvicorn backend.main:app --reload
Open API documentation
http://127.0.0.1:8000/docs
Author

Nirbhay Tiwari
