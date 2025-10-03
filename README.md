# AgenticAI-PolyBlog
**Polyglot blog generation powered by Agentic AI.**  
Generate multilingual, SEO-ready blog content via agent-driven workflows built with **LangGraph**, **LangChain**, **Groq / OpenAI**, and **FastAPI**.

---

[![Docker](https://img.shields.io/badge/docker-ready-blue)]()
[![Python](https://img.shields.io/badge/python-3.11+-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## Overview

AgenticAI-PolyBlog is an **agentic** AI system for generating blog posts in multiple languages. It uses LangGraph for graph-based orchestration of agent work, LangChain (and community/providers) for LLM integrations, FastAPI as the HTTP backend, and LangSmith (Studio) for tracing and debugging runs.

Key design goals:
- Multi-language content generation (polyglot)  
- Agentic workflows (LangGraph graphs orchestrate LLM calls + tools)  
- Observability via LangSmith Studio for debugging and traces  
- Dockerized for local dev and production deployment

---

## Tech stack / Dependencies

Primary dependencies used by this project (also listed in `requirements.txt`):

- `langchain`, `langchain_core`, `langchain_community`
- `langgraph`, `langgraph-cli[inmem]` — graph orchestration + local dev server. :contentReference[oaicite:0]{index=0}  
- `langchain_groq`, `langchain_openai`, `groq` — Groq + OpenAI providers for LLMs. :contentReference[oaicite:1]{index=1}  
- `fastapi`, `uvicorn` — backend + ASGI server.  
- `watchdog` — optional file watcher for hot reload in dev.  
- `python-dotenv` — load `.env` config.  
(See `requirements.txt` for exact pins.)

---

## Quickstart — Docker (recommended)

This repo is Dockerized. The following commands build the image, start the dev server (LangGraph + FastAPI), and show logs.

> Build image (no cache):  
```bash
docker compose build --no-cache web
