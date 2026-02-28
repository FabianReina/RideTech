#!/bin/bash

PORT=${PORT:-8000}

echo "=========================================="
echo " Iniciando FastAPI en el puerto $PORT"
echo " Archivo principal: main.py"
echo " Instancia de FastAPI: app"
echo "=========================================="

# Arranca la app con Gunicorn y Uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT