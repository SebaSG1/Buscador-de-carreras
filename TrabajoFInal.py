from tabulate import tabulate
import time
import random
import os



# Declaracion de lista
carreras = [["ABOGACIA", 5 , "UNS, SIGLO21"],
           ["AGRIMENSURA", 5 ,"UNS"],
           ["ARQUITECTURA",5 ,"UNS, SIGLO 21"],
           ["BIOQUIMICA", 5 , "UNS"],
           ["CONTADOR PUBLICO", 5 ,"UNS, SIGLO21"],
           ["FARMACIA", 5 , "UNS"],
           ["INGENIERIA AGRONOMICA", 5, "UNS"],
           ["INGENIERIA CIVIL", 5, "UNS, UTN"],
           ["INGENIERIA DE ALIMENTOS", 5, "UNS"],
           ["INGENIERIA ELECTRICISTA", 5, "UNS"],
           ["INGENIERIA ELECTRONICA", 5, "UNS, UTN"],
           ["INGENIERIA EN COMPUTACION", 5, "UNS"],
           ["INGENIERIA EN SISTEMAS DE INFORMACION", 5, "UNS"],
           ["INGENIERIA MECANICA", 5 , "UNS, UTN"],	
           ["INGENIERIA QUIMICA", 5 , "UNS"],	
           ["LICENCIATURA EN ADMINISTRACION", 5 , "UNS, UTN, SIGLO21"],	    
           ["LICENCIATURA EN CIENCIAS AMBIENTALES", 5 ,"UNS, SIGLO21"],	
           ["LICENCIATURA EN CIENCIAS BIOLOGICAS", 5 ,"UNS, SIGLO21"],	
           ["LICENCIATURA EN CIENCIAS DE LA COMPUTACION", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN CIENCIAS DE LA EDUCACION", 5 ,"UNS, SIGLO21"],	
           ["LICENCIATURA EN CIENCIAS GEOLOGICAS", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN ECONOMIA", 5 ,"UNS, SIGLO21"],	
           ["LICENCIATURA EN ENFERMERIA", 5 ,"UNS"],		
           ["LICENCIATURA EN FILOSOFIA", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN FISICA", 5 ,"UNS"],		
           ["LICENCIATURA EN GEOFISICA", 5 ,"UNS, UTN, SIGLO21"],	
           ["LICENCIATURA EN GESTIÓN UNIVERSITARIA", 5 ,"UNS SIGLO21"],		
           ["LICENCIATURA EN HISTORIA", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN LETRAS", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN MATEMATICA", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN OCEANOGRAFIA", 5 ,"UNS"],		
           ["LICENCIATURA EN OPTICA Y CONTACTOLOGÍA", 5 ,"UNS,SIGLO21"],	
           ["LICENCIATURA EN QUIMICA", 5 ,"UNS, SIGLO21"],		
           ["LICENCIATURA EN SEGURIDAD PÚBLICA", 5 ,"UNS, SIGLO21"],	
           ["LICENCIATURA EN TURISMO", 5 ,"UNS, SIGLO21"],	
           ["MEDICINA", 5 ,"UNS"],		
           ["PROFESORADO DE EDUCACION INICIAL", 4 ,"UNS"],	
           ["PROFESORADO DE EDUCACION PRIMARIA", 4 ,"UNS, SIGLO21"],
           ["PROFESORADO EN CIENCIAS BIOLÓGICAS", 4 ,"UNS,SIGLO21"],		
           ["PROFESORADO EN ECONOMIA", 4 ,"UNS, SIGLO21"],		
           ["PROFESORADO EN ECONOMIA PARA LA ENSEÑANZA SECUNDARIA", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN EDUCACION SECUNDARIA EN CIENCIAS DE LA ADMINISTRACION", 4 ,"UNS,SIGLO21"],	
           ["PROFESORADO EN EDUCACION SECUNDARIA Y SUPERIOR EN CIENCIAS DE LA ADMINISTRACION", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN FILOSOFIA", 4 ,"UNS, SIGLO21"],		    
           ["PROFESORADO EN FISICA", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN GEOCIENCIAS", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN GEOGRAFIA", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN HISTORIA", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN LETRAS", 4 ,"UNS, SIGLO21"],		
           ["PROFESORADO EN MATEMATICA", 4 ,"UNS, SIGLO21"],	
           ["PROFESORADO EN QUIMICA", 4 ,"UNS, SIGLO21"],		
           ["PROFESORADO EN QUIMICA DE LA ENSEÑANZA MEDIA", 4 ,"UNS, SIGLO21"],
           ["TECNICATURA SUPERIOR AGRARIA EN SUELOS Y AGUAS", 4 ,"UNS, SIGLO21"],	
           ["TECNICATURA SUPERIOR EN ADMINISTRACION Y GESTION DE RECURSOS PARA INSTITUCIONES UNIVERSITARIAS", 3 ,"UNS, SIGLO21"],	
           ["TECNICATURA UNIVERSITARIA APICOLA", 3 ,"UNS"],	
           ["TECNICATURA UNIVERSITARIA EN ACOMPAÑAMIENTO TERAPÉUTICO", 3 ,"UNS"],		
           ["TECNICATURA UNIVERSITARIA EN CARTOGRAFIA, TELEDETECCION Y SISTEMAS DE INFORMACION GEOGRAFICA", 3 ,"UNS, SIGLO21"],	
           ["TECNICATURA UNIVERSITARIA EN ECONOMÍA Y GESTIÓN DE EMPRESAS ALIMENTARIAS", 3 ,"UNS, SIGLO21"],	
           ["TECNICATURA UNIVERSITARIA EN MEDIO AMBIENTE", 3 ,"UNS, SIGLO21"],	
           ["TECNICATURA UNIVERSITARIA EN OPERACIONES INDUSTRIALES", 3 ,"UNS, SIGLO21"],	
           ["TECNICATURA UNIVERSITARIA EN PROGRAMACION", 2 ,"UTN"],	
           ["TECNICATURA UNIVERSITARIA EN PARQUES Y JARDINES", 3 ,"UNS, SIGLO21"],	
           ["TECNICATURA UNIVERSITARIA EN SISTEMAS ELECTRÓNICOS INDUSTRIALES INTELIGENTES", 3 ,"UNS, SIGLO21"], 
           ['LICENCIATURA EN ADMINISTRACION', 4, 'SIGLO 21'],
           ['LICENCIATURA EN DISEÑO DE INDUMENTARIA TEXTIL', 4, 'SIGLO 21'],
           ['LICENCIATURA EN COMERCIALIZACION Y MARKETING', 4, 'SIGLO 21'],
           ['LICENCIATURA EN COMERCIO INTERNACIONAL', 4, 'SIGLO 21'],
           ['LICENCIATURA EN DISEÑO INDUSTRIAL', 4, 'SIGLO 21'],
           ['CONTADOR/A PUBLICO', 4, 'SIGLO 21'],
           ['LICENCIATURA EN DISEÑO GRAFICO', 4, 'SIGLO 21'],
           ['LICENCIATURA EN DISEÑO Y ANIMACION DIGITAL', 4, 'SIGLO 21'],
           ['INGENIERIA EN INNOVACION Y DESARROLLO', 5, 'SIGLO 21'],
           ['LICENCIATURA EN RELACIONES PUBLICAS E INSTITUCIONALES', 4, 'SIGLO 21'],
           ['LICENCIATURA EN GESTION DE RECURSOS HUMANOS', 4, 'SIGLO 21'],
           ['LICENCIATURA EN PSICOLOGIA', 4, 'SIGLO 21'],
           ['LICENCIATURA EN ADMINISTRACION AGRARIA', 4, 'SIGLO 21'],
           ['LICENCIATURA EN RELACIONES INTERNACIONALES', 4, 'SIGLO 21'],
           ['LICENCIATURA EN PUBLICIDAD EN PUBLICIDAD', 4, 'SIGLO 21'],
           ['LICENCIATURA EN KINESIOLOGIA Y FISIOTERAPIA', 4, 'SIGLO 21'],
           ['LICENCIATURA EN NUTRICION', 4, 'SIGLO 21'], 
           ['INGENIERIA ELECTRONICA', 6, 'UTN'],
           ['LICENCIATURA EN ORGANIZACION INDUSTRIAL', 4, 'UTN'],
           ['INGENIERIA ELECTRICA', 5, 'UTN'],
           ['INGENIERIA MECANICA', 5, 'UTN']]

# Funciones requeridas
def deco():
    print("""
             __             
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |                 |;       
     ;                 ;|    
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
  __ )                                      |                                                                  
  __ \    |   |    __|    __|    _` |       __|   |   |        __|    _` |    __|    __|    _ \    __|    _` | 
  |   |   |   |  \__ \   (      (   |       |     |   |       (      (   |   |      |       __/   |      (   | 
 ____/   \__,_|  ____/  \___|  \__,_|      \__|  \__,_|      \___|  \__,_|  _|     _|     \___|  _|     \__,_| 
                                                                                                               

      """)

def buscar_carrera():
    # Esta funcion determina la busqueda de la carrera que el usuario desea saber si se dicta en la ciduad. 

    carrera = input('Que carrera estas pensando estudiar?\n ')
    carrera = carrera.upper()

    # Mediante la lectura de archivos, busco la carrera que el usuario escribe 

    with open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/menu.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if len(carrera) > 6:
            if carrera in line:
                return True # Encuentra el string
        else:
            print("ingrese una carrera valida")
            time.sleep(3)
            os.system("clear")
            break
    return False  # No encuentra el string

def tipo_carrera():
    # Esta funcion determina el tipo de carrera que el usuario busca ya sea de grado tecnicatura o profesorado 
    # mediante la lectura de archivos correspondientes. 
    
    num = int(input('1) De grado.  \n2) Tecnicatura.  \n3) Profesorados.\n'))  
    if num == 1:
        print('Las carreras de grado permiten la formación en un conocimiento profundo de una o más disciplinas,')
        print('tanto en sus principios, teorías, leyes, como en sus formas de construcción del saber.\n')
        print('La duracion es de 5 a 6 años. Estas son las carreras de grado que se ofrecen en Bahía Blanca: \n')
        archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/degrado.txt', mode="r")
        print(archivo.read())

    elif num == 2:
        print('Las tecnicaturas son carreras que proporcionan conocimiento tecnico y especifico de determinada actividad profesional.\n')
        print('La duracion es de entre 3 y 2 años. Estas son las tecnicaturas que se ofrecen en Bahía Blanca: \n')
        archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/tecnicaturas.txt', mode="r")
        print(archivo.read())

    else:
        print('Los profesorados te permitiran convertirte en profesor o profesora, recibiendo los conocimientos necesarios para desempeñarte como docente.\n')
        print('La duracion de los mismos suele ser de 4 o 3 años. Estos son los profesorados que se ofrecen en Bahía Blanca: \n')
        archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/profesorados.txt', mode="r")
        print(archivo.read())

def modalidad():
    # Funcion que determina las carreras que pueden realizarse de forma virtual o presencial, mediante la lectura de archivos correspondientes. 
     
     modalidad = input('1) Presencial. \n2) Virtual. \n')
     if modalidad == "1":
         print('Las principales carreras que puedes estudiar de forma presencial en Bahía Blanca son: \n')
         time.sleep(0.2)
         archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/presencial.txt', mode="r")
         print(archivo.read())
       
     elif modalidad == "2":
         print('Las principales carreras que puedes estudiar de forma virtual son: \n')
         time.sleep(0.2)
         archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/virtual2.txt', mode="r")
         print(archivo.read())

def test_vocacional():
    # Funcion que realiza el test vocacional mediante una serie de preguntas.

    print('A continuacion realizaremos un breve test vocacional con el fin de poder orientarte en tu busqueda profesional.\n')
    print('Deberas ingresar la opcion 1, 2, 3, o 4 de la pregunta correspondiente.\n')
    time.sleep(1.0)

    print('¿Que personaje te identifica mas?: \n1) Elon Musk. \n2) Will Smith. \n3) Frida Kahlo. \n4) Nikola Tesla. \n')
    pregunta_a = int(input())

    while pregunta_a != 1 and pregunta_a != 2 and pregunta_a != 3 and pregunta_a != 4:
            print('Opcion invalida, por favor ingrese una opcion valida (1,2,3,4)')
            pregunta_a = int(input())
        
    else:
        print('\nTe atrae más: \n1) Una obra de teatro. \n2) Las camaras, microfonos y set de TV. \n3) Ayudar a las personas. \n4) Analizar mercados economicos. \n')
        pregunta_b = int(input())

        while pregunta_b != 1 and pregunta_b != 2 and pregunta_b != 3 and pregunta_b != 4:
              print('Opcion invalida, por favor ingrese una opcion valida (1,2,3,4)')
              pregunta_b = int(input())
        else:
             print('\nEs mejor tener: \n1) Una computadora. \n2) Un libro. \n3) Un microscopio. \n4) Una calculadora cientifica. \n')
             pregunta_c= int(input())

             while pregunta_c != 1 and pregunta_c != 2 and pregunta_c != 3 and pregunta_c != 4:
                   print('Opcion invalida, por favor ingrese una opcion valida (1,2,3,4)')
                   pregunta_c= int(input())

             else:
                  print('\n¿De iniciar un nuevo emprendimiento, cual seria? \n1) Local comercial. \n2) Una distribuidora. \n3) Empresa de servicios. \n4) Una agencia de medios. \n')
                  pregunta_d= int(input())

                  while pregunta_d != 1 and pregunta_d != 2 and pregunta_d != 3 and pregunta_d != 4:
                        print('Opcion invalida, por favor ingrese una opcion valida (1,2,3,4)')
                        pregunta_c= int(input())

                  else:
                       print('¿\nPrefieres trabajar con objetivos a: \n1) Corto plazo. \n2) Mediano plazo. \n3) Largo plazo. \n')
                       pregunta_e = int(input())

                       while pregunta_e != 1 and pregunta_e != 2 and pregunta_e != 3:
                            print('Opcion invalida, por favor ingrese una opcion valida (1,2,3)')
                            pregunta_e= int(input())

                       else:
                            print('\nImaginas tu vida profesional: \n1) Trabajando en equipo. \n2) Aprendiendo cosas nuevas. \n3) Un trabajo donde no te importe tomar riesgos. \n4) Un trabajo que te haga descubrir nuevos paises. \n')
                            pregunta_f = int(input())

                            while pregunta_f != 1 and pregunta_f != 2 and pregunta_f != 3 and pregunta_f != 4:
                                print('Opcion invalida, por favor ingrese una opcion valida (1,2,3,4)')
                                pregunta_f= int(input())

def agregar_carrera():

 carrera_nueva = input('Que tipo de carrera se agregara? \n1) Licenciatura. \n2) Tecnicatura. \n3) Profesorado. \n')
 
 if carrera_nueva == "1":
    archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/degrado.txt','a')
    print('Ingrese una nueva carrera:')
    archivo.write(input())
    print('Se agrego la nueva carrera al archivo')

 elif carrera_nueva == "2":
    archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/tecnicaturas.txt','a')
    print('Ingrese una nueva carrera:')
    archivo.write(input())
    print('Se agrego la nueva carrera al archivo')

 elif carrera_nueva == "3": 
    archivo = open('/Users/sebastiangomez/Desktop/TrabajoFinalPY/profesorados.txt','a')
    print('Ingrese una nueva carrera:')
    archivo.write(input())
    print('Se agrego la nueva carrera al archivo')

def tiempo_test(i): 

    # Funcion que realiza un conteo en forma regresiva.

    while i: 
        mins, secs = divmod(i, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        i -= 1

def pantalla_limpia():
    time.sleep(0.5)
    os.system('clear')

def menu():
    
 while True:
       # Presentacion del menu con opciones para el usuario 
       
       print('\n\t*********************************************************\n\t*\t\t\t\t\t\t\t*')
       print('\t*  Buscador de carrearas en la ciudad de Bahía Blanca\t*\n\t*\t\t\t\t\t\t\t*'   )
       print('\t*  '"⚙️","📊","🔭","💡","🎸","📚","👔","🚀","🔬","🎨","🎭","🔨","💼","💸","🎬","⚖️","📕","📣"'\t*')
       print('*******************************************************************************\n*  \t\t\t\t\t\t\t\t\t      *')
       time.sleep(0.2)
       print('* Opción 1: Oferta academica de la ciudad de Bahía Blanca.  \t\t',"📈",'  *')
       time.sleep(0.2)
       print('* Opción 2: Fijate si la carrera que quieres estudiar esta en la ciudad ',"✅",'  *')
       time.sleep(0.2)
       print('* Opción 3: ¿Que tipo de carrera quieres estudiar?  \t\t\t',"🤔",'  *')
       time.sleep(0.2)
       print('* Opción 4: ¿Presencial o virtual? \t\t\t\t\t',"🏛️ 💻", '*')
       time.sleep(0.2)
       print('* Opción 5: Test vocacional  \t\t\t\t\t\t',"🎯",'  *')
       time.sleep(0.2)
       print('* Opcion 6: Agregar una nueva carrera. \t\t\t\t\t' , "📝",'  *')
       time.sleep(0.2)
       print('* Opción 7: Salir\t\t\t\t\t\t\t',"👋", '  *\n*\t\t\t\t\t\t\t\t\t      *')
       time.sleep(0.2)
       print('*******************************************************************************\n') 
       seleccion = int(input('\nSeleccione una opción: \n'))
        # El usuario elije la opcion que desea.

       if seleccion == 1:
         pantalla_limpia()
         print('Bahia Blanca tiene una oferta academica de más de',len(carreras), 'carreras para estudiar.')

        # Con la funcion de Tabulate imprimo de manera mas ordenada y amigable para el usuario una lista con las principales
        # carreras de la ciudad con su informacion correspondiente (tiempo de durabilidad, institucion o universidad donde cursar)

         print(tabulate(carreras, headers=["Carrera", "Duracion", "Universidad o institucion"], numalign='center', tablefmt='grid'))

         input("Pulsa una tecla para continuar...")

       elif seleccion == 2:
         pantalla_limpia()
         if buscar_carrera():
             print('La carrera que elejiste puedes estudiarla en Bahía Blanca.',"✅")
         else:
            print('La carrera que elejiste no puedes estudiarla en Bahía Blanca.',"❌")

         input("Pulsa una tecla para continuar...")
          
       elif seleccion == 3:
        pantalla_limpia()
        tipo_carrera()
        input("Pulsa una tecla para continuar...")
        
       elif seleccion == 4:
        pantalla_limpia()
        modalidad()
        input("Pulsa una tecla para continuar...")
        
       elif seleccion == 5:
         pantalla_limpia()
         test_vocacional()
                                       
         print('Analizando respuestas...',"⏳")

         i = 5 
         tiempo_test(int(i))   

        # Luego de realizar la cuenta regresiva con la funcion correspondiente, mediante el uso de "random.choice"
        # se selecciona de manera automatica y aleatora una de las carreras definida en la lista "carreras" declarada en el inicio del programa.

         print('Segun el test vocacional tu carrera es: ', random.choice(carreras),"😉")
         input("Pulsa una tecla para continuar...")

       elif seleccion == 6:
        pantalla_limpia()
        agregar_carrera()
        input("Pulsa una tecla para continuar...")  

       elif seleccion == 7:
        print('¡Exitos en tu proxima carrera!', "💪")
        break

       else:
        print('Opción incorrecta') 
 

deco()
print(menu())




