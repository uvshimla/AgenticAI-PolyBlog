#!/usr/bin/env bash
set -e

# Load .env into environment for the process (optional if you use docker-compose env_file)
if [ -f /app/.env ]; then
  export $(grep -v '^#' /app/.env | xargs)
fi

# run migrations / pre-start hooks here if any

exec uvicorn app:app --host 0.0.0.0 --port "${PORT:-8000}" --workers 1
