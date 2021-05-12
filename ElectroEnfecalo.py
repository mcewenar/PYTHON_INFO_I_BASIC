class Paciente():
    visitas = {}

    def __init__(self, nombre = '', cedula = '', genero = ''):
        self.nombre = nombre
        self.cedula = cedula
        self.genero = genero
        return

    def getVisitas(self):
        return self.visitas

    def addVisita(self, visitas):
        self.visitas[visitas.getFecha()] = visitas
        return True

    def SetVisitas(self, visitas):
        self.visitas = visitas
        return True

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return True

    def getCedula(self):
        return self.cedula

    def setCedula(self, cedula):
        self.cedula = cedula
        return True

    def getGenero(self):
        return self.genero

    def setGenero(self, gen):
        self.genero = gen
        return True

    def verifyVisitas(self, file):
        return file in self.visitas.keys()

    def seve(self):
        return

    def load(self):
        return

    def info(self):
        return

class Visita():
    indices=[]
    data = {}

    def __init__(self, fecha = '', file = '', notas = ''):
        self.data['fecha'] = fecha
        self.data['file'] = file
        self.data['notas'] = notas

    def getIndices(self):
        return self.data['indices']

    def setIndices(self, indices):
        self.data['indices'] = indices
        return None

    def getFecha(self):
        return self.data['fecha']

    def getFileName(self):
        return self.data['file']

    def getNota(self):
        return self.data['notas']

    def verifyFileName(self, Ffecha):
        return self.data['fecha'] == Ffecha

    def getData(self):
        return self.data

class Indice():

    # El arreglo contiene la información
    data = [0, 0, 0, 0, 0, 0]
    # Ahora defino los índices
    pDelta = 0
    pTheta = 1
    pAlfa1 = 2
    pAlfa2 = 3
    pBeta = 4
    pGamma = 5

    def __init__(self, pDelta = 0., pTheta = 0., pAlfa1 = 0., pAlfa2 = 0., pBeta = 0. ,pGamma = 0.):
        self.data[self.pDelta] = pDelta
        self.data[self.pTheta] = pTheta
        self.data[self.pAlfa1] = pAlfa1
        self.data[self.pAlfa2] = pAlfa2
        self.data[self.pBeta] = pBeta
        self.data[self.pGamma] = pGamma

    def getIndices(self):
        return self.data

    def info(self):
        return

class Sistema():

    savepath = 'pacientesDB.xhk'
    TodosPacientes = {}

    def __init__(self):
        return

    def addPaciente(self, paciente):
        self.TodosPacientes[paciente.getCedula()] = paciente
        return True

    def getPaciente(self, cedula):
        return self.TodosPacientes[cedula]

    def verificarPaciente(self, paciente):
        return paciente.getCedula() in self.TodosPacientes.keys()

    def verificarPacienteCedula(self, cedula):
        return cedula in self.TodosPacientes.keys()

    def LimpiarPaciente(self, cedula):
        del self.TodosPacientes[cedula]

    def load(self):
        f = open(self.savepath, 'r')
        for line in f:
            print(line)
            if '?' in line:
                doc1 = line.replace('?','').replace('\n','').split('|')
                pac = Paciente(doc1[0], doc1[1], doc1[2])
                self.addPaciente(pac)
                pvic = {}
            elif '>' in line:
                doc2 = line.replace('>','').replace('\n','').split('|')
                vis = Visita(doc2[0], doc2[1], doc2[2])
            elif '*' in line:
                doc3 = line.replace('*','').replace('\n','').split('|')
                idx = Indice(doc3[0], doc3[1], doc3[2], doc3[3], doc3[4], doc3[5])
                vis.setIndices(idx.getIndices())
                pvic[doc2[0]] = vis
                pac.SetVisitas(pvic)
                self.addPaciente(pac)
        f.close()
    
    def save(self):
        f = open(self.savepath, 'w')
        for key, value in self.TodosPacientes.items():
            print(1, key, value.getNombre())
            f.write('?'+value.getNombre() + '|' +  value.getCedula() + '|' + value.getGenero() + '\n')
            viss = value.getVisitas()
            print(type(viss))
            for key2, value2 in viss.items():
                print('\t',2,key2,value2.getFecha())
                f.write('>'+value2.getFecha()+'|'+value2.getFileName()+'|'+value2.getNota()+'\n')
                idx = value2.getIndices()
                f.write('*'+'|'.join(idx)+'\n')
        f.close()

def main():
    mySys = Sistema()

    # Menú principal
    print('Bienvenido al sistema de administración de registros electrofisiológicos\n')
    while True:
        print('''\nMenú:
    1. Ingresar nuevo paciente.
    2. Editar registro de paciente existente
    3. Eliminar registros de paciente.
    4. Cargar información.
    5. Guardar información.
    6. Salir''')
        opt = input('\n >>> ')

        if opt == '1':
            print('\n###### Ingreso de nuevo paciente ######\n')
            Innombre = input("Nombre del paciente: ")
            Incedula = input("Cedula del paciente: ")
            Ingenero = input("Genero del paciente: ")

            if mySys.verificarPacienteCedula(Incedula):
                print('Sistema: El paciente ya está registrado, si desea editar dirigase a la opción 2 del menú principal.')
            else:
                mySys.addPaciente(Paciente(nombre = Innombre, cedula = Incedula, genero = Ingenero))
        elif opt == '2':
            print('\n###### Editar registro de paciente ######\n')

            while True:
                update = False
                print('Ingrese cedula de paciente a editar, escribar SALIR en cualquier momento para regresar el menú principal.')
                Incedula = input('\n\t>>> ')
                if Incedula.lower() == 'salir':
                    print('Regresando al menú principal...')
                    break
                if not mySys.verificarPacienteCedula(Incedula):
                    print('No existe un paciente con esa cédula!')
                    # Volver al inicio del ciclo while
                    continue
                
                

                print('Qué desea editar?')
                print('1. Editar nombre')
                print('2. Editar cedula')
                print('3. Editar genero')
                print('4. Editar visitas')
                print('5. salir')
                subopt = input('>>> ')

                pacC = mySys.getPaciente(Incedula)
                mySys.LimpiarPaciente(Incedula)

                if subopt.lower() == 'salir':
                    break

                if subopt == '1':
                    print('\n%%% Editar cedula %%%\n')
                    newCed = input('Nueva cédula')

                    if mySys.verificarPacienteCedula(newCed):
                        print('Ya exsite un paciente con esa cedula')
                        continue
                    
                    pacC.setCedula(newCed)
                    update = True
                elif subopt == '2':
                    print('\n%%% Editar nombre %%%\n')
                    NombreNuevo = input('Nuevo nombre: ')
                    pacC.setNombre(NombreNuevo)
                    update = True
                elif subopt == '3':
                    print('\n%%% Editar genero %%%\n')
                    newGen = input('Nuevo genero: ')
                    pacC.setGenero(newGen)
                    update = True
                elif subopt == '4':
                    update = True
                    while True:
                        
                        print('\n%%% menú de visitas %%%\n')
                        print('1. Añadir visita')
                        print('2. Eliminar visita')
                        print('3. salir')
                        subsubopt = input('>>> ')
                        if subsubopt == '1':
                            print('&&& Añadir visita &&&')
                            pvic = pacC.getVisitas()

                            fech = input('fecha:')
                            fil = input('nombre del archivo: ')

                            if pacC.verifyVisitas(fech):
                                print('El paciente ya tiene esa visita')
                                print('Recuerde que solo se permite una visita diaria por criterios de salud')
                                continue
                            
                            nota = input('Notas: ')

                            print('A continuación reporte los valores medidos durante la visita')

                            pDel = input('Potencia delta: ')
                            pThe = input('Potencia tehta: ')
                            pAl1 = input('Potencia alfa1: ')
                            pAl2 = input('Potencia alfa2: ')
                            pBet = input('Potencia beta: ')
                            pGam = input('Potencia Gamma: ')

                            newVisita = Visita(fecha = fech, file = fil, notas = nota)
                            newInd = Indice(pDel, pThe, pAl1, pAl2, pBet, pGam)
                            newVisita.setIndices(newInd.getIndices())

                            pvic[fech] = newVisita
                            
                            pacC.SetVisitas(pvic)
                        elif subsubopt == '2':
                            pvic = pacC.getVisitas()
                            print('Ingresé la fecha de la visita a eliminar, o escribar SALIR para salir de este menú')
                            for i in pvic.keys():
                                print(i)
                            print('Ingresé la fecha de la visita a eliminar:')
                            
                            while True:
                                delvis = input('>>> ')
                                if delvis in pvic.keys():
                                    del pvic[delvis]
                                else:
                                    print('Ingreso errado')
                                if delvis.lower() == 'salir':
                                    break
                                
                            pacC.SetVisitas(pvic)
                        elif subsubopt == '3':
                            print('&&& Saliendo &&&')
                            break
                        else:
                            print('Opción invalida')

                elif subopt == '5':
                    print('\n%%% Saliendo %%%\n')
                    break
                else:
                    print('Opción invalida')
                    continue

                if update:
                    mySys.addPaciente(pacC)
                    print('Actualización exitosa')
                
                    
        elif opt == '3':
            print('\n###### Eliminar registros de paciente ######\n')
            Incedula = input('Ingrese cédula del paciente a eliminar: ')
            if mySys.verificarPacienteCedula(Incedula):
                pass
            else:
                print('No existe un paciente con cedula ' + Incedula)
        elif opt == '4':
            print('\n###### Cargando información ######\n')
            mySys.load()
            print('\n###### Carga exitoisa ######\n')
        elif opt == '5':
            print('\n###### Guardando información del sistema ######\n')
            mySys.save()
            print('\n###### Guardado exitoso ######\n')
        elif opt == '6':
            print('\n###### Finalizando programa... ######\n')
            break
        else:
            print('\nOPCION INVALIDA\n')

if __name__ == '__main__':
    main()
