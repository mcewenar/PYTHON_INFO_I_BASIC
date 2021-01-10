#Escenario
#La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado,
#expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59.
#El resultado debe ser mostrado en la consola.

#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
#No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida,
#lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

#Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
# calcula los minutos y los convierte a una cadena
minutos=str((min+dura)%60)
# calcula los minutos totales y luego lo convierte a horas para luego convertirlo a una cadena
horas=str(((hora*60 + min + dura)//60) % 24)
print("Hora: "+horas+":"+minutos)

