PORT=${PORT:-8000} 

 

echo "==========================================" 

echo " Iniciando FastAPI en el puerto $PORT" 

echo " Archivo principal: init.py" 

echo " Instancia de FastAPI: app" 

echo "==========================================" 


gunicorn -w 4 -k uvicorn.workers.UvicornWorker init:app --bind 0.0.0.0:$PORT 

EOF 