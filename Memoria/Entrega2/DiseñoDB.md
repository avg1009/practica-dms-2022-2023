# Diseño de la base de datos

Hemos decidido realizar una base de datos relacional y SQLAchemy como ORM.

El almacenamiento de datos será recogido en diferentes tablas:

- Pregunta Almacena los datos de todas las preguntas creadas en el portal. 
  - Cada pregunta tiene su propio Id, independiente del Id del resto de elementos.
- Respuesta contiene las respuestas de cada pregunta
  - Cada respuesta tiene su propio Id, independiente del Id del resto de elementos.
  - Cada respuesta está asociada mediante clave foranea a la pregunta a la que está respondiendo
- Comentarios contiene los comentarios de cada respuesta
  - Cada comentario tiene su propio Id, independiente del Id del resto de elementos.
  - Cada comentario está asociado mediante clave foranea a la respuesta a la que está comentado
- ReportePregunta  almacena el usuario que ha realizado el reporte y a qué pregunta
  - Cada ReportePregunta tiene su propio Id, independiente del Id del resto de elementos.
  - Cada ReportePregunta está asociado mediante clave foranea a la pregunta que está reportando.
- ReporteRespuesta  almacena el usuario que ha realizado el reporte y a qué respuesta
  - Cada ReporteRespuesta tiene su propio Id, independiente del Id del resto de elementos.
  - Cada ReporteRespuesta está asociado mediante clave foranea a la respuesta que está reportando.
- ReporteComentario  almacena el usuario que ha realizado el reporte y a qué comentario
  - Cada ReporteComentario tiene su propio Id, independiente del Id del resto de elementos.
  - Cada ReporteComentario está asociado mediante clave foranea al comentario que está reportando.
- VotosRespuesta almacena el usuario que ha realizado el voto y a qué respuesta
  - Cada VotoRespuesta tiene su propio Id, independiente del Id del resto de elementos.
  - Cada VotoRespuesta está asociado mediante clave foranea a la respuesta que está votando.
- VotosComentario almacena el usuario que ha realizado el voto y a qué comentario
  - Cada VotoComentario tiene su propio Id, independiente del Id del resto de elementos.
  - Cada VotoComentario está asociado mediante clave foranea al comentario que está votando.

![](https://i.imgur.com/PT5SQrO.jpeg)

