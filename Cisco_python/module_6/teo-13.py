#Las excepciones son clases
#Todas las excepciones integradas de Python forman una jerarquía de clases.

#Analiza el código en el editor.
def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

printExcTree(BaseException)

#Este programa muestra todas las clases de las excepciónes predefinidas en forma de árbol.

#Como un árbol es un ejemplo perfecto de una estructura de datos recursiva, la recursión parece ser la mejor manera de recorrerlo. 
# La función printExcTree() toma dos argumentos:

#Un punto dentro del árbol desde el cual comenzamos a recorrerlo.
#Un nivel de anidación (lo usaremos para construir un dibujo simplificado de las ramas del árbol).
#Comencemos desde la raíz del árbol: la raíz de las clases de excepciónes de Python es la clase BaseException 
# (es una superclase de todas las demás excepciones).

#Para cada una de las clases encontradas, se realiza el mismo conjunto de operaciones:

#Imprimir su nombre, tomado de la propiedad __name__.
#Iterar a través de la lista de subclases provistas por el método __subclasses__(), e invocar recursivamente la función printExcTree(), 
# incrementando el nivel de anidación respectivamente.
#Ten en cuenta cómo hemos dibujado las ramas. La impresión no está ordenada de alguna manera: si deseas un desafío, puedes intentar ordenarla tu mismo. Además, hay algunas imprecisiones sutiles en la forma en que se presentan algunas ramas. Eso también se puede arreglar, si lo deseas.

#Así es como se ve:

#BaseException
#   +---Exception
#   |   +---TypeError
#   |   +---StopAsyncIteration
#   |   +---StopIteration
#   |   +---ImportError
#   |   |   +---ModuleNotFoundError
#   |   |   +---ZipImportError
#   |   +---OSError
#   |   |   +---ConnectionError
#   |   |   |   +---BrokenPipeError
#   |   |   |   +---ConnectionAbortedError
#   |   |   |   +---ConnectionRefusedError
#   |   |   |   +---ConnectionResetError
#   |   |   +---BlockingIOError
#   |   |   +---ChildProcessError
#   |   |   +---FileExistsError
#   |   |   +---FileNotFoundError
#   |   |   +---IsADirectoryError
#   |   |   +---NotADirectoryError
#   |   |   +---InterruptedError
#   |   |   +---PermissionError
#   |   |   +---ProcessLookupError
#   |   |   +---TimeoutError
#   |   |   +---UnsupportedOperation
#   |   |   +---herror
#   |   |   +---gaierror
#   |   |   +---timeout
#   |   |   +---Error
#   |   |   |   +---SameFileError
#   |   |   +---SpecialFileError
#   |   |   +---ExecError
#   |   |   +---ReadError
#   |   +---EOFError
#   |   +---RuntimeError
#   |   |   +---RecursionError
#   |   |   +---NotImplementedError
#   |   |   +---_DeadlockError
#   |   |   +---BrokenBarrierError
#   |   +---NameError
#   |   |   +---UnboundLocalError
#   |   +---AttributeError
#   |   +---SyntaxError
#   |   |   +---IndentationError
#   |   |   |   +---TabError
#   |   +---LookupError
#   |   |   +---IndexError
#   |   |   +---KeyError
#   |   |   +---CodecRegistryError
#   |   +---ValueError
#   |   |   +---UnicodeError
#   |   |   |   +---UnicodeEncodeError
#   |   |   |   +---UnicodeDecodeError
#   |   |   |   +---UnicodeTranslateError
#   |   |   +---UnsupportedOperation
#   |   +---AssertionError
#   |   +---ArithmeticError
#   |   |   +---FloatingPointError
#   |   |   +---OverflowError
#   |   |   +---ZeroDivisionError
#   |   +---SystemError
#   |   |   +---CodecRegistryError
#   |   +---ReferenceError
#   |   +---BufferError
#   |   +---MemoryError
#   |   +---Warning
#   |   |   +---UserWarning
#   |   |   +---DeprecationWarning
#   |   |   +---PendingDeprecationWarning
#   |   |   +---SyntaxWarning
#   |   |   +---RuntimeWarning
#   |   |   +---FutureWarning
#   |   |   +---ImportWarning
#   |   |   +---UnicodeWarning
#   |   |   +---BytesWarning
#   |   |   +---ResourceWarning
#   |   +---error
#   |   +---Verbose
#   |   +---Error
#   |   +---TokenError
#   |   +---StopTokenizing
#   |   +---Empty
#   |   +---Full
#   |   +---_OptionError
#   |   +---TclError
#   |   +---SubprocessError
#   |   |   +---CalledProcessError
#   |   |   +---TimeoutExpired
#   |   +---Error
#   |   |   +---NoSectionError
#   |   |   +---DuplicateSectionError
#   |   |   +---DuplicateOptionError
#   |   |   +---NoOptionError
#   |   |   +---InterpolationError
#   |   |   |   +---InterpolationMissingOptionError
#   |   |   |   +---InterpolationSyntaxError
#   |   |   |   +---InterpolationDepthError
#   |   |   +---ParsingError
#   |   |   |   +---MissingSectionHeaderError
#   |   +---InvalidConfigType
#   |   +---InvalidConfigSet
#   |   +---InvalidFgBg
#   |   +---InvalidTheme
#   |   +---EndOfBlock
#   |   +---BdbQuit
#   |   +---error
#   |   +---_Stop
#   |   +---PickleError
#   |   |   +---PicklingError
#   |   |   +---UnpicklingError
#   |   +---_GiveupOnSendfile
#   |   +---error
#   |   +---LZMAError
#   |   +---RegistryError
#   |   +---ErrorDuringImport
#   +---GeneratorExit
#   +---SystemExit
#   +---KeyboardInterrupt
