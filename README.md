# xaldigital api

## Docker
- Correr el comando **docker-compose up -d** para correr docker
### Construir la base de datos 
   - Correr **docker-compose exec backend bash** para acceder a la terminal en la ruta de la aplicacion
   - Correr **python manage.py db init** para crear el repositorio de migrasion de la base de datos
   - Correr **python manage.py db migrate** para crear el esquema de la base de datos
   - Correr **python manage.py db upgrade** para construir las tablas en la base de datos

## Endpoints

La ruta para usada es **localhost:5000/api/** y los endpoints se muestran en la tabla

Rutas           | Metodo        |Funcionalidad            |
--------------- | ------------- | ----------------------- | 
/api/get_items  | GET           | Retorna todos los items |
/api/get_items  | POST          | Crea un nuevo item      |
/api/get_item_by/id| GET           | Retorna un item por id  |
/api/get_item_by/id| PUT           | Modifica un item por id |
/api/get_item_by/id| DELETE        | Elimina un item por id  |