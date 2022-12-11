# Diseño de la base de datos

Hemos decidido realizar una base de datos relacional y SQLAchemy como ORM.

El almacenamiento de datos será recogido en diferentes tablas:

- Pregunta Almacena los datos de todas las preguntas creadas en el portal
- Respuesta contiene las respuestas de cada pregunta
- Comentarios contiene los comentarios de cada respuesta
- ReporteComentario  almacena el usuario que ha realizado el reporte y a qué comentario
- ReportePregunta  almacena el usuario que ha realizado el reporte y a qué pregunta
- ReporteRespuesta  almacena el usuario que ha realizado el reporte y a qué respuesta
- VotosComentario almacena el usuario que ha realizado el voto y a qué comentario
- VotosRespuesta almacena el usuario que ha realizado el voto y a qué respuesta

![](https://i.imgur.com/PT5SQrO.jpeg)

