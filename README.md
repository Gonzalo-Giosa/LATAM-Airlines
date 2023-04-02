# ML Engineer Challenge - LATAM Airlines


### Carpetas 

#### api 

Esta carpeta contiene los archivos necesarios para las pruebas de la API. En particular, se encuentra la aplicación FastAPI que expone el modelo de aprendizaje automático.

#### dev 

Esta carpeta contiene los archivos de desarrollo, como notebooks y modelos. En esta carpeta se pueden encontrar los notebooks utilizados para la exploración y análisis de los datos, así como también los modelos entrenados.

Dentro de la carpeta 'dev' podemos encontrar la carpeta 'notebooks' donde se encuentran los dos notebooks principales del desafio donde se desarrollaron los modelos.

to-expose.ipynb : Trabajo de 'Juan', punto de partida. El projecto se baso en encontrar mejoras y optimizar el modelo de 'Juan' en cuanto a performance en evaluacion y en produccion

## Proceso:

### Explicaremos el paso a paso para poder exponer el modelo en el endpoint de la API (la cual se construye usando FastAPI) y luego hacer el test de estres usando la tool wrk y obtener los resultados deseados.

#### Asegurarnos de estar posicionados en el directorio "api"

cd api

Este comando cambia el directorio actual a la carpeta api, que es donde se encuentra la aplicación FastAPI que expone el modelo de aprendizaje automático.
#### Create virtual env, Activar el entorno virtual en el shell actual e instalar las bibliotecas correspondientes dentro de él

source install_env.sh

Este comando crea un entorno virtual para la aplicación y luego instala todas las dependencias necesarias en ese entorno virtual. El script install_env.sh es el encargado de realizar estas acciones.

#### Run the fastapi

uvicorn mlapi:app --reload

Este comando inicia la aplicación FastAPI en el servidor local, lo que permite acceder al endpoint de la API. La opción --reload indica que el servidor debe reiniciarse automáticamente cada vez que se detecten cambios en los archivos del proyecto.

#### WRK

opcion 1: wrk -t15 -c500 -d45 -s test.lua --latency http://127.0.0.1:8000

opcion 2: wrk -t15 -c400 -d45s -s /mnt/c/Users/LATAM_VF/project_vf/api/test.lua http://127.0.0.1:8000


Este comando utiliza la herramienta wrk para realizar pruebas de estrés en el endpoint de la API. Los parámetros -t, -c y -d indican el número de hilos, conexiones y duración de la prueba, respectivamente. El parámetro -s especifica el script que se utilizará para generar la carga de trabajo. El parámetro --latency indica que se debe medir la latencia de la respuesta del servidor.