# Funcionamiento de la API REST
La función de una API REST es la de crear una interfaz que interactúe como intermediario para manejar de forma segura la información a través del navegador.
En este caso, hemos creado una API REST que va a comunicarse con el frontend y poder ofrecer los datos a nuestra web

## Capa de presentación
- Comentarios: será el encargado de realizar todas las acciones relacionadas con los comentarios a través de la capa de servicios
- Preguntas: será el encargado de realizar todas las acciones relacionadas con las preguntas a través de la capa de servicios
- Reportes: será el encargado de realizar todas las acciones relacionadas con los reportes a través de la capa de servicios
- Respuestas: será el encargado de realizar todas las acciones relacionadas con las respuestas a través de la capa de servicios
- Security: será el encargado de realizar todas las acciones relacionadas con la seguridad y la comprobación de los tokens (api_key y token)
- Server: será el encargado de realizar la comprobación del servidor

## Capa de servicios
- Comentarios Service: contiene los métodos que hacen la conexión entre la base de datos correspondiente a los comentarios (comentarioDB) permitiendo que se puedan ingresar y obtener datos 
- Preguntas Service: contiene los métodos que hacen la conexión entre la base de datos correspondiente a las preguntas (preguntaDB) permitiendo que se puedan ingresar y obtener datos 
- Reporte Service: contiene los métodos que hacen la conexión entre la base de datos correspondiente a los reportes (reporteComentarioDB, reportePreguntaDB, reporteRespuestaDB) permitiendo que se puedan ingresar y obtener datos
- Respuesta Service: contiene los métodos que hacen la conexión entre la base de datos correspondiente a los respuesta (resuestaDB) permitiendo que se puedan ingresar y obtener datos 
- Votos Service: contiene los métodos que hacen la conexión entre la base de datos correspondiente a los comentarios (votosComentarioDB y votosRespuestaDB) permitiendo que se puedan ingresar y obtener datos 