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
