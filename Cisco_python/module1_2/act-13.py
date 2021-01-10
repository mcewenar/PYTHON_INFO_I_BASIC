"""Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:
3x3 - 2x2 + 3x - 1
El resultado debe ser asignado a y.
Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo flotante.
Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados. No te desanimes por no lograrlo en el primer intento. Se persistente y curioso."""

for x in [0,1,-1]:
    x = float(x) #Convert to float
    y=3*x**3-2*x**2+3*x-1
    print("y =", y)