# Arquitectura utilizada
Para el diseño del backend  contamos con tres capas, la capa de presentación, la capa de datos y la capa de servicios, por lo que podríamos considerarlo una arquitectura de tres capas.

## La capa de datos 
La capa de datos se encarga de almacenar todos los datos recogidos, esta capa contendrá la base de datos, las tablas generadas y toda la información relevante.
para su realización nos hemos fijado en dms2223auth y utilizado su misma estructura.
       
## La capa de presentación 
Esta capa será la encargada de realizar todas las acciones relacionadas con las distintas clases a través de la capa de servicios, convirtiendolos en un Json

## La capa de servicios
Es la intermedario entre la capa de presentación y la base de datos.
Devuelve los objetos con la estructura del common para mandarselo a la api que es quien genera el json para enviarlo al front.

## Patrones utilizados
### Fachada
En nuestro caso, como queremos acceder al backend desde el frontend, necesitamos que haya un desacoplamiento entre el frontend y el backend. Con esto conseguiremos que a través de la clase backservice se pueda acceder al backend y el frontend desconozca lo que hace el backend. Es por esto, que el patrón que más se adapta a lo que queremos es el patrón Fachada.

## Principios SOLID 
### Single responsability
Siguiendo la definición: "una clase o módulo debería tener una y solo una razón para cambiar", hemos tenido en cuenta que cada una de las clases que tengamos solo tenga una única responsabilidad.
- En el caso de la clase Preguntas, que esta solo fuera la encargada de las acciones a realizar sobre las preguntas.
- En el caso de la clase Respuestas, que esta solo fuera la encargada de las acciones a realizar sobre las repuestas.
- En el caso de la clase Comentarios, que esta solo fuera la encargadad de las acciones a realizar sobre los comentarios.
- En el caso de las clase Reporte, que esta solo fuera la encargada de las acciones a realizar sobre los reportes.

### Interface segregation
Siguiente la definición: "ningún cliente debería estar obligado a depender de métodos qeu no utiliza".
En nuestro caso, los endpoints de la interfaz REST están organizados de tal forma que se cumpla simultáneamente junto a la responsabilidad única.

### Dependency inversion
Siguiendo la definición: "una clase debería depender de abstracciones, no de concreciones"
En nuestro caso, estamos teniendo en cuenta que nuestros módulos volátiles dependan de los estables, evitando que se produzcan cambios graves en cascada.