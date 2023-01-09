# Lineas a futuro 
*  Buscador de preguntas por palabras clave para que el usuario en cuestión pueda encontrar las preguntas que desea.
* Baneo de usuarios: si recibimos un reporte de algún usuario y se acepta, entonces el moderador podrá decidir cuanto será el tiempo de baneo de esa cuenta considerando el tiempo respecto la infracción.
* Respecto a la anterior los usuarios también podrán bloquear usuarios para evitar acosos, amenazas y tener una comunidad limpia.
* Crear relaciones entre usuarios, es decir, poder seguir a un usuario y entonces en tu feed personal verás las preguntas que realizan los usuario que sigues.(listado de preguntas de gente que sigues)
* Gestión básica de perfil de usuario cambiar credenciales, apodos, modo oscuro o modo claro, foto de perfil.
## Relaciones entre usuarios
La idea principal es que los usuarios puedan seguir a otros,de este modo en nuestra feed principal o home nos aparezcan las últimas preguntas realizadas por los usuarios que seguimos en un orden cronológico.

A la hora de implementarlo tendriamos que seguir los siguientes pasos:

Primero en el frontend deberá existir un botón de "Seguir" en los perfiles de los usuarios.

Habrá que modificar la base de datos de los usuarios añadiendo una columna que almacene todos los usuarios que seguimos.

Una vez tengamos la DB del usuario modificada con una consulta desde la API podremos conseguir la información de los usuarios que seguimos y las preguntas que han realizado, debido a que en la DB de preguntas tenemos el atributo "creador".

Ahora podemos enviarle la información de las preguntas que tenemos que mostrar al frontend que aparecerán en "Home".

## Baneo temporal y Bloqueo de usuarios
En la pestaña de reportes se añadirá tambien un botón que permitirá bloquear a ciertos usuarios durante un tiempo. también podriamos añadir una opción en los roles que sea bloqueado provocando que no tenga acceso a la aplicación.

Para poder llevar esto a cabo seria importante añadir en la base de datos de usuario un parámetro que diga si está bloqueado o no, y pueda modificarse, provocando que aunque ponga los credenciales correctos en el "log in" no le deje acceder.

Ya a una linea más de futuro para evitar las multicuentas de usuarios bloqueados podemos bloquearlos via IP pero este apartado tiene que ver más con la seguridad de la propia web.


## Gestión básica de perfil
 * Añadir diferentes pestañas dónde el usuario pueda cambiar credenciales, eleccion modo oscuro modo claro, una bibliografia y una foto de perfil.
 * Esto conlleva poder realizar modificaciones en la base de datos y sobreescribir los datos antiguos con los nuevos.
## Buscador de palabras clave
  * Primero con la interfaz deberemos recoger texto ayudandonos de los formularios de html de este modo podemos recoger las palabras clave
  * De esta forma podemos consultar en la DB mediante la API los títulos de las preguntas que tengan el texto escrito en el formulario.