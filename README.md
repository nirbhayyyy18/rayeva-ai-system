# Rayeva AI Systems Assignment

## Overview

This project implements AI-powered modules designed to automate sustainable commerce workflows.

The system reduces manual catalog effort and improves B2B proposal generation using AI models integrated with structured business logic.

Two modules have been fully implemented:

• AI Auto Category & Tag Generator  
• AI B2B Proposal Generator  

The system is built using FastAPI and follows a clean modular architecture separating API routes, AI logic, prompt design, and database operations.

---

# System Architecture Overview

The system follows a layered architecture to maintain separation between AI logic and application logic.

Flow of the system:

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
JSON Response to Client

Main components:

Routes → Handles API endpoints  
Services → AI integration and business logic  
Prompts → Prompt engineering for AI tasks  
Database → SQLAlchemy models for persistence  
Utils → Logging and helpers

---

# Module 1 — AI Auto Category & Tag Generator

This module automatically generates product metadata from product descriptions.

Features implemented:

• Auto-assign primary category from predefined list  
• Suggest sub-category  
• Generate SEO tags (5–10 tags)  
• Suggest sustainability filters such as plastic-free, biodegradable, recycled etc.  
• Return structured JSON output  
• Store results in database

Example Input


```json{
"name":"Bamboo Toothbrush",
"description":"Eco friendly biodegradable bamboo toothbrush"
}
```
Example Output

```{
"category":"Personal Care",
"sub_category":"Oral Care",
"tags":[
"bamboo toothbrush",
"eco friendly",
"plastic free",
"biodegradable",
"sustainable"
],
"sustainability":[
"plastic-free",
"biodegradable"
]
}
```
The generated data is stored in the database for catalog automation.

Module 2 — AI B2B Proposal Generator

This module generates sustainable corporate gifting proposals based on budget constraints.

Features implemented:

• Suggested sustainable product mix
• Budget allocation within provided limit
• Estimated cost breakdown
• Sustainability impact positioning summary
• Structured JSON output

Example Input

```json{
"budget":50000,
"event":"Corporate sustainability event"
}

Example Output

{
"products":[
{"name":"Reusable Water Bottles","quantity":200,"cost":10000},
{"name":"Eco Friendly Notebooks","quantity":200,"cost":8000},
{"name":"Sustainable Plant Kits","quantity":100,"cost":12000}
],
"total_cost":45000,
"impact_summary":"This proposal promotes reusable and eco friendly products, reducing plastic waste and supporting sustainable practices."
}
```

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

This module would estimate environmental impact metrics such as:

• Plastic saved
• Carbon emissions avoided
• Local sourcing benefits

The results would be stored with the order record.



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

Possible actions:

• Order status query
• Return policy handling
• Escalation for refund issues
• Conversation logging


Technical Features

• Structured JSON AI outputs
• Prompt and response logging
• Environment-based API key management using .env
• Clear separation of AI logic and application logic
• Error handling and validation


Tech Stack

Backend: FastAPI
Database: SQLite with SQLAlchemy
AI Integration: LLM API
Environment Management: python-dotenv


Running the Project

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn backend.main:app --reload

Open API documentation

http://127.0.0.1:8000/docs
