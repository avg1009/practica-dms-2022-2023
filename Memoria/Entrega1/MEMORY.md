# Memoria de la primera entrega
Realizada por Oscar Valverde, Adolfo Jesússs Viñé, Victor Pascual, Claudia Landeira, Mario García
# Desarrollo del Frontend
Para crear la aplicación nos hemos centrado en que tenga una arquitectura de 3 capas para diferenciar entre la presentación, los datos y la lógica. Al usar esta arquitectura cubrimos el caso de Seperation of concerns.(Esta es nuestra idea original pero es modificable, de este modo podemos utilizar un patron de arquitectura MVC más adelante(modelo-vista-controlador) dónde el controlador seríala logica utilizada, el modelo la capa de datos y por ultimo la vista que es donde nos centramos ahora.)
También queremos cubrir la gran mayoria de los principios SOLID.
De los principios solid el que mas nos importa cubrir ahora mismo es el Single Responsability y el Open Close



## Presentación 

    Con la presentación tenemos la interaccion que tiene el cliente con el software, es decir, una interfaz para que el usuario no tenga problemas para interactuar y llamar a los datos. 

## Datos 

    De momento cada pregunta comentarios reporte etc etc... será guardado en un array del propio objeto correspondiente(de momento slo usamos navegacion de objetos al dedicarnos exclusivamente al frontend).No hemos tocado realizar un backend y utilizar uno de pega en esta primera entrega
## Logica 

    El manejo específico de la aplicación que hace con los datos.Lo tenemos diferenciado para no mezclar con los datos y en esta capa lo que hariamos seria el propio tratamiento de datos. 

A menudo podemos utilizar que la presentación o interfaz pueda llamar a los datos de manera directa.

Podemos realizar navegación inversa para recuperar comentarios y sus respuestas, para que en un reporte tengamos solo un objeto en el propio.
# Los patrones creacionales Usados son

## Singelton 

    Para crear una unica instancia pensamos que este es el mejor patron creacional posible pero a su vez como flask nos ofrece una 
    funcionalidad llamado global que se encarga de esto mismo no veemos necesario implementarlo de momento.

    Queremos que solo exista una instancia del objeto 