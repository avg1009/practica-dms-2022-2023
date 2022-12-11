# Arquitectura utilizada

Para el diseño del backend  contamos con tres capas, la capa de presentación, la capa de datos y la capa de servicios, por lo que podríamos considerarlo una arquitectura de tres capas.

## La capa de presentación 

Mario o claudia
Esta capa se encargará de recoger los objetos generados por el service y convertirlos en un Json.

## La capa de datos 

La capa de datos se encarga de almacenar todos los datos recogidos, esta capa contendrá la base de datos, las tablas generadas y toda la información relevante.
para su realización nos hemos fijado en dms2223auth y utilizado su misma estructura.
        db 
            exc
            results
                reportes
                votos
            resultsets
                reportes
                votos

## La capa de servicios

Es la intermedario entre la api y la base de datos.
Devuelve los objetos con la estructura del common para mandarselo a la api que es quien genera el json para enviarlo al front.

## Patrones utilizados

Los patrones utilizados para la creación de esta entrega

## Principios SOLID 

Los principios solid cubiertos para esta entregan han sido: 

## Union backend y frontend

Victor