#Tu primer módulo: continuación
#Es hora de hacer este ejemplo más complejo: hemos asumido aquí que el archivo Python principal se encuentra en la misma carpeta o 
#directorio que el módulo que se va a importar.

#Realicemos el siguiente experimento mental:

#Estamos utilizando el sistema operativo Windows ® (esta suposición es importante, ya que la forma del nombre del archivo depende de ello).
#El script principal de Python se encuentra en C:\Users\user\py\progs y se llama main.py.
#El módulo a importar se encuentra en C:\Users\user\py\modules .

#¿Como lidiar con ello?

#Para responder a esta pregunta, tenemos que hablar sobre cómo Python busca módulos. Hay una variable especial (en realidad una lista) 
#que almacena todas las ubicaciones (carpetas o directorios) que se buscan para encontrar un módulo que ha sido solicitado por la 
#instrucción import.

#Python examina estas carpetas en el orden en que aparecen en la lista: si el módulo no se puede encontrar en ninguno de estos directorios, 
#la importación falla.

#De lo contrario, se tomará en cuenta la primera carpeta que contenga un módulo con el nombre deseado (si alguna de las carpetas restantes 
#contiene un módulo con ese nombre, se ignorará).

#La variable se llama path (ruta), y es accesible a través del módulo llamado sys. Así es como puedes verificar su valor:

#Hemos lanzado el código dentro del directorio C:\User\user y obtenemos:

#C:\Users\user
#C:\Users\user\AppData\Local\Programs\Python\Python36-32\python36.zip
#C:\Users\user\AppData\Local\Programs\Python\Python36-32\DLLs
#C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib
#C:\Users\user\AppData\Local\Programs\Python\Python36-32
#C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages