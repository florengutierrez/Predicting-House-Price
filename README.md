![tasapi](/static/images/readme.png)




TASAPI es el proyecto final del bootcamp a full time de Data Analyst de Ironhack.

El objetivo de este proyecto es observar las diferencias de precios de las viviendas, en la Comunidad de Madrid según su geolocalización y crear un tasador.

El proyecto se divide en 4 fases:


1. Exploración y Limpieza de datos:

- Seleccionamos el dataset https://www.kaggle.com/mirbektoktogaraev/madrid-real-estate-market.

- Realizamos una limpieza y exploración del dataset para comprender los datos.

📚 Librerías: *Pandas, Numpy


2. Geolocalización:

- Encontrar latitud y longitud de las viviendas en venta, por direcciones exactas.

- Encontrar latitud y longitud de las viviendas por barrio en aquellas que en el primer filtro no se encontraron.


📚 Librerías: *Geocoder
              *Requests
              *Pandas, Numpy
              

3. Aplicar Modelos de Machine Learning para predecir el precio de la vivienda según características de esta y geolocalización.

  * Modelos usados: "Random Forest" 
                    "Bagging"
                    "Extra Tree Regressor"
                    "Linear Regression"
                    "Ridge"
                    "RidgeCV"
                    "Lasso"
                    "Decision Tree Regressor"
                    "Gradient Boosting Regressor" 
                    "KNeighbors Regressor"
  
  * Modelo con mayor predicción: **Random Forest**, haciendo uso de GridSearchCV para evaluar y seleccionar los parámetros de este.
  
📚 Librerías: *SKlearn
  

4. Montaje de App Web:

- Flask junto con HTML, realizo la siguiente App Web, la cual, introduciendo la dirección de la vivienda y las carácterísticas de esta, te predice el precio de su vivienda según su geolocalización y parámetros introducidos.


![tasapi](/static/images/app.png)



*Por favor, haz git clone al repositorio, e introduzca en su terminal dentro de la carpeta del repositorio: **app.py.

