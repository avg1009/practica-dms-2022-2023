# Introduccion
El objetivo de este proyecto consiste en realizar un entorno web de discusión entre usuarios dividiendo la realización del mismo entre diferentes servicios:
    -Un servicio de autenficación previamente incluido encargado de controlar la gestión de usuarios, las sesiones y los permisos de cada usuario
    -Un servicio de backend, el cual gestiona las capas de datos y de servicios las cuales se encargan de la implementación en base de datos de las preguntas, respuestas , comentarios y reportes a traves de la api.
    -Un servicio de frontend basado en la capa de presentación que permite la interacción del sistema con los usuarios a través del navegador web.

En concreto, esta parte de la memoria está centrada en los objetivos establecidos para la segunda entrega los cuales corresponden con la implementación completa de los requisitos no funcionales detallados para el proyecto dentro del servicio de backend.

# Arquitectura utilizada
Para el diseño del backend  contamos con tres capas, la capa de presentación, la capa de datos y la capa de servicios, por lo que podríamos considerarlo una arquitectura de tres capas.

## La capa de datos 
La capa de datos se encarga de almacenar todos los datos recogidos, esta capa contendrá la base de datos, las tablas generadas y toda la información relevante.
para su realización nos hemos fijado en dms2223auth y utilizado una estructura similar.
       
## La capa de presentación 
Esta capa será la encargada de realizar todas las acciones relacionadas con las distintas clases a través de la capa de servicios, convirtiendolos en un Json, lo cual permitirá el enlace a través de la api con la capa de servicios.

## La capa de servicios
Es la intermedario entre la capa de presentación y la base de datos.
Devuelve los objetos con la estructura del common para mandarselo a la api que es quien genera el json para enviarlo al front. En esta capa es donde nos centramos principalmente en realizar la implementacion y construcción de los objetos con la información obtenida a través de la capa de presentación por parte de los usuarios para posteriormente poder actualizar la base de datos con estos elementos.
La construcción se realiza a través de las clases definidas en la primera versión de la entrega pertenecientes al directorio dms2223common con el fin de evitar la reedición de código.

## Posibles Patrones utilizados
### Fachada
En nuestro caso, como queremos acceder al backend desde el frontend, necesitamos que haya un desacoplamiento entre el frontend y el backend. Con esto conseguiremos que a través de la clase backservice se pueda acceder al backend y el frontend desconozca lo que hace el backend. Es por esto, que el patrón que más se adapta a lo que queremos es el patrón Fachada.

## Principios SOLID 
### Interface segregation
Siguiente la definición: "ningún cliente debería estar obligado a depender de métodos que no utiliza".
En nuestro caso, los endpoints de la interfaz REST están organizados de tal forma que se cumpla simultáneamente junto a la responsabilidad única.

### Dependency inversion
Siguiendo la definición: "una clase debería depender de abstracciones, no de concreciones"
En nuestro caso, estamos teniendo en cuenta que nuestros módulos volátiles dependan de los estables, evitando que se produzcan cambios graves en cascada.

## Posibles patrones no incluidos
Debido a la simplificación de la primera entrega en la capa de presentación con respecto a la segunda hemos tenido que redifinir parte del código del servicio de frontend puesto que no se adecuaba con la nueva implementación dentro de las capas de servicios y datos. Lo cual rompe con el Open/Closed Principle y con el Single Responsablity Principle. El cambio más significativo donde esto se produce es en el ejemplo anterior no obstante este principio se ha roto probablemente en más casos.