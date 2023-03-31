ML Engineer Challenge - LATAM Airlines

Explicaremos el paso a paso para poder exponer el modelo en el endpoint de la API (la cual se construye usando FastAPI) y luego hacer el test de estres usando la tool wrk y obtener los resultados deseados.

# asegurarnos de estar posicionados en el directorio "api"
cd api

# Create virtual env, activate the virtual env in the current shell and install the corresponding libraries inside of it
source install_env.sh

# Run the fastapi
uvicorn mlapi:app --reload

# WRK
wrk -t15 -c500 -d45 -s test.lua --latency http://127.0.0.1:8000