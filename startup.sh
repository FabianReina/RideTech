PORT=${PORT=-8000}

echo "=================================================="

echo "iniciando FASTAPI"

gunicorn -w 4 uvicorn.workers.UvicornWorker init:app --bind 0.0.0.0 $PORT
