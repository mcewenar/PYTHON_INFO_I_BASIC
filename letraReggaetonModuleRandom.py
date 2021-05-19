import random #se importa la librería de python random

sujetos = ["mami", "bebé", "princess", "mami"]  #se define una lista
intenciones = ["yo quiero", "yo puedo", "yo vengo a", "voy a"]
verbos = ["encendelte", "amalte", "ligal", "jugal"]
advs = ["suave", "lento", "lápido", "fuelte"]
complementos_uno = ["hasta que salga el sol", "toda la noche", "hasta el amanecer", "todo el día"]
complementos_dos = ["sin anestesia", "sin compromiso", "feis to feis", "sin miedo"]

sujeto_seleccionado = random.choice(sujetos) #se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
intencion_seleccionada = random.choice(intenciones)
verbo_seleccionado = random.choice(verbos)
adv_seleccionado = random.choice(advs)
compl1s_seleccionado = random.choice(complementos_uno)
compl2s_seleccionado = random.choice(complementos_dos)

print("letra generada: " + sujeto_seleccionado + " " + intencion_seleccionada + " " + verbo_seleccionado + " " 
      + adv_seleccionado + " " + compl1s_seleccionado + " " + compl2s_seleccionado) #se imprime la canción