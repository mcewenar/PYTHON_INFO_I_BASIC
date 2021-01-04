"""La función print() - los argumentos de palabras clave
Python ofrece otro mecanismo para transmitir o pasar los argumentos, que puede ser útil cuando se desea convencer a la función print() de que cambie su comportamiento un poco.

No se va a explicar en profundidad ahora. Se planea hacer esto cuando se trate el tema de funciones. Por ahora, simplemente queremos mostrarte como funciona. Siéntete libre de utilizarlo en tus propios programas.

El mecanismo se llama argumentos de palabras clave. El nombre se deriva del hecho de que el significado de estos argumentos no se toma de su ubicación (posición) sino de la palabra especial (palabra clave) utilizada para identificarlos.

La función print() tiene dos argumentos de palabras clave que se pueden utilizar para estos propósitos. El primero de ellos se llama end.

En la ventana del editor se puede ver un ejemplo muy simple de como utilizar un argumento de palabra clave.

Para utilizarlo es necesario conocer algunas reglas:

Un argumento de palabra clave consta de tres elementos: una palabra clave que identifica el argumento (end -termina aquí); un signo de igual (=); y un valor asignado a ese argumento.
Cualquier argumento de palabra clave debe ponerse después del último argumento posicional (esto es muy importante).

En nuestro ejemplo, hemos utilizado el argumento de palabra clave end y lo hemos igualado a una cadena que contiene un espacio.

Ejecuta el código para ver como funciona.

La consola ahora debería mostrar el siguiente texto:

Mi nombre es Python. Monty Python.

Como puedes ver, el argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.

El comportamiento predeterminado refleja la situación en la que el argumento de la palabra clave end se usa implícitamente de la siguiente manera: end="\n"."""

print("Mi nombre es", "Python.", end="")
print("Monty Python.")