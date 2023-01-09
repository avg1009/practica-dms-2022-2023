# Lineas a futuro 
*  Buscador de preguntas por palabras clave para que el usuario en cuestión pueda encontrar las preguntas que desea.
* Baneo de usuarios: si recibimos un reporte de algún usuario y se acepta, entonces el moderador podrá decidir cuanto será el tiempo de baneo de esa cuenta considerando el tiempo respecto la infracción.
* Respecto a la anterior los usuarios también podrán bloquear usuarios para evitar acosos, amenazas y tener una comunidad limpia.
* Crear relaciones entre usuarios, es decir, poder seguir a un usuario y entonces en tu feed personal verás las preguntas que realizan los usuario que sigues.(listado de preguntas de gente que sigues)
* Gestión básica de perfil de usuario cambiar credenciales, apodos, modo oscuro o modo claro, foto de perfil.

Teniendo en cuenta que nos hemos basado en un patrón de diseño de fachada, el añadir clases nos permitiría no tener que hacer grandes cambios estructurales. Además, este patrón permitiría cumplir el open close, ya que estaría cerrado a modificaciones, pero abierto a futuras extensiones.

## Relaciones entre usuarios

![](https://i.imgur.com/yPEknRV.jpg)



La idea principal es que los usuarios puedan seguir a otros,de este modo en nuestra feed principal o home nos aparezcan las últimas preguntas realizadas por los usuarios que seguimos en un orden cronológico.

A la hora de implementarlo tendriamos que seguir los siguientes pasos:

Primero en el frontend deberá existir un botón de "Seguir" en los perfiles de los usuarios.

Una opción sería modificar la base de datos actual de los usuarios añadiendo una columna que almacene todos los usuarios que seguimos, pero dicha base pertenece al servicio de autenticación, y esta información no es relevante para dicho servicio, si no para el uso interno de aplicación.
Por ello, la mejor opción sería crear una base de datos en el back end relaccionada con los usuarios del servicio de autenticación, pero que contenga esta información adicional, la cual es útil a nivel de aplicación para relaccionar los usuarios. También sería necesario crear los servicios y la API REST para interaccionar con esta nueva tabla.

Una vez tengamos la DB del usuario modificada con una consulta desde la API podremos conseguir la información de los usuarios que seguimos y las preguntas que han realizado, debido a que en la DB de preguntas tenemos el atributo "creador".

Ahora podemos enviarle la información de las preguntas que tenemos que mostrar al frontend que aparecerán en "Home".


Opción añadida, pero que conllevaría demasiados cambios en todo el proyecto y que por eso es algo que no sería conveniente aplicar tal como tenemos hecho el proyecto actualmente:

Si queremos enfocar este proyecto a una especie de red social dónde los usuarios van a estar interactuando entre sí, creando diferentes post que a su vez pueden ser comentados por otros usuarios, sería mejor utilizar una base de datos NoSql orientada en grafos.

Al decantarnos por una base de datos estructurada en grafos debemos cumplir las reglas ACID:

* Atomicidad: Las preguntas o se crean o no, igual que los comentarios, no se pueden generar de forma parcial.
* Consistencia: la BD siempre pasa por estados consistentes en estos casos las claves primarias de las preguntas.
* Independencia: En nuestro caso todos los post serán de la misma manera no habrán cambios, todos tendrán que tener la misma estructura, al igual que los comentarios, por tanto todos tendrán la misma consistencia.
* Durabilidad: una vez ejecutada una transacción, sus efectos deben permanecer a pesar de fallos en el servidor, tendremos que tener en cuenta que al ser una red social no nos podemos permitir caer y dejar la aplicación inoperativa durante x periodo de tiempo. 
* Con todo lo expuesto anteriormente nos decantamos por NEO4J 
Se basa en el modelo clave-valor, los nodos tendrán relaciones entre sí y además los nodos y estas relaciones tendrán descripciones. 
Los índices se crean sobre las etiquetas de los nodos, las relaciones y las propiedades.
Las consultas básicas son: Búsqueda de nodos(POST,USUARIOS), relaciones mediante los índices.Navegación por el grafo (traversals). 

Esto sería ya remodelar toda la base de datos y centrarlo más a una red social como puede ser Twitter, que a un foro. Es por esta razón, que no es adecuado realizar estos cambios, pero aún así nos ha parecido interesante incluirlo. 
Tal y como está diseñada la aplicación, se podría implementar una versión básica, utilizando la nueva tabla del Back End de información del usuario, para relaccionar a los usuarios entre si. Una vez relaccionados, en el apartado reservado para mostrar información de los usuarios que sigues, se podría mostrar la lista de preguntas que ha realizado dicho usuario en el foro, mediante una consulta SQL a la base de datos de preguntas, filtrando por el usuario creador, y así obtener dicha información. 
Esta versión sería limitada, ya que no permitiría tener una buena escalabilidad a futuro, como la que si tendríamos utilizando relacciones de grafos, las cuales nos permiten estudiar dichas relacciones en profundidas y en un futuro poder incluso implementar un sistema de recomendación de usuarios a seguir, en base a las relacciones de los usuarios que sigues.




## Baneo temporal y Bloqueo de usuarios
En la pestaña de reportes se añadirá tambien un botón que permitirá bloquear a ciertos usuarios durante un tiempo. También podriamos añadir una opción en los roles que sea bloqueado provocando que no tenga acceso a la aplicación.

Para poder llevar esto a cabo seria importante añadir en la base de datos de usuario un parámetro que diga si está bloqueado o no, y pueda modificarse, provocando que aunque ponga los credenciales correctos en el "log in" no le deje acceder. Esta información si que es relevante para el sistema de autenticación, para validar o rechazar el "log in", por lo que dicha información sería conveniente almacenarla en la base de datos actual del sistema de autenticación.

Ya a una linea más de futuro para evitar las multicuentas de usuarios bloqueados podemos bloquearlos via IP pero este apartado tiene que ver más con la seguridad de la propia web.


## Gestión básica de perfil
 * Añadir diferentes pestañas dónde el usuario pueda cambiar credenciales, eleccion modo oscuro modo claro, una bibliografia y una foto de perfil.
 * Esto conlleva poder realizar modificaciones en la base de datos y sobreescribir los datos antiguos con los nuevos.
 * Esta información podríamos almacenarla en una nueva tabla del Back End de información de usuario, ya que no es información util para el sistema de autenticación, pero es importante tenerla relaccionada con cada usuario del foro, para que todos puedas realizar su personalización propia y se cargue cada vez que entren al foro.


## Buscador de palabras clave.
  * Primero con la interfaz deberemos recoger texto ayudandonos de los formularios de html de este modo podemos recoger las palabras clave
  * De esta forma podemos consultar en la DB mediante la API los títulos de las preguntas que tengan el texto escrito en el formulario.
