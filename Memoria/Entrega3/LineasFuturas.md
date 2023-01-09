# Lineas a futuro 
*  Buscador de preguntas por palabras clave para que el usuario en cuestión pueda encontrar las preguntas que desea.
* Baneo de usuarios: si recibimos un reporte de algún usuario y se acepta, entonces el moderador podrá decidir cuanto será el tiempo de baneo de esa cuenta considerando el tiempo respecto la infracción.
* Respecto a la anterior los usuarios también podrán bloquear usuarios para evitar acosos, amenazas y tener una comunidad limpia.
* Crear relaciones entre usuarios, es decir, poder seguir a un usuario y entonces en tu feed personal verás las preguntas que realizan los usuario que sigues.(listado de preguntas de gente que sigues)
* Gestión básica de perfil de usuario cambiar credenciales, apodos, modo oscuro o modo claro, foto de perfil.
## Relaciones entre usuarios
Para crear las relaciones entre usuarios deberá existir primero en el frontend un botón que al pulsarlo transmita al back que sigue a un usuario y segundo hay que modificar la DB con una columna nueva en usuarios que tenga una lista de los usuarios que sigue.

Una vez tengamos la DB del usuario modificada con la lista de la gente que sigue, con una consulta a la DB desde la api dónde conociendo los usuarios que sigue el usuario, muestre las preguntas realizadas por dichos usuarios en una pestaña que sea "siguiendo".

## Baneo temporal y Bloqueo de usuarios
En la pestaña de reportes se añadirá tambien un botón que permitirá bloquear a ciertos usuarios durante un tiempo. también podriamos añadir una opción en los roles que sea bloqueado provocando que no tenga acceso a la aplicación.

Para poder llevar esto a cabo seria importante añadir en la base de datos de usuario un parámetro que diga si está bloqueado o no, y pueda modificarse.


## Gestión básica de perfil
 * Añadir diferentes pestañas dónde el usuario pueda cambiar credenciales, eleccion modo oscuro modo claro, una bibliografia y una foto de perfil.
## Buscador de palabras clave
  * Primero con la interfaz deberemos recoger texto ayudandonos de los formularios de html de este modo podemos recoger las palabras clave
  * De esta forma podemos consultar en la DB mediante la API ??????  los títulos de las preguntas que tengan el texto escrito en el formulario.