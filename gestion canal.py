#gestion canal
canal = {}
nombre=input("digite el nombre de su canal: ")
descripcion=input("ingrese la descripcion de su canal: ")
categoria=input(""" 
                    ┌─────────────────────────────────────────────────────────┐
                    │       elija la categoria de su canal:                   │
                    │_________________________________________________________│
                    │                                                         │
                    │    1- comedia                                           |
                    |    2- animación                                         |
                    |    3- belleza                                           |
                    |    4- moda                                              |
                    |    5- cocina                                            │
                    │    6- ASMR(respuesta sensorial meridiana autónoma)      |
                    |    7- vlogs                                             |
                    |    8- videojuegos                                       |
                    |    9- empresas                                          |
                    │   10- tecnología                                        |
                    |   11- viajes                                            |
                    |                                                         |
                    └─────────────────────────────────────────────────────────┘ 
                """)
videos=int(input('ingrese la cantidad de videos que tiene: '))
visualizaciones=0
like=0
seguidores=0
tiempo=0
video=0
while videos > 0:
    # Información para un video en particular
    video+=1
    print("VIDEO NUMERO ", video)
    visitas=int(input("cuantas visitas tiene el video?: "))
    visualizaciones+=visitas
    likes=int(input("cuantas me gusta tiene el video?: "))
    like+=likes
    duracion=float(input("cuanto tarda el video tiempo en minutos: "))
    segundos=duracion*60
    horas=segundos / 3600
    time=horas*visitas
    tiempo+=time
    suscripciones=int(input("¿cuantos seguidores obtubo del video?: "))
    seguidores+=suscripciones
    videos -= 1
    canal['visitas'] = visualizaciones
    canal['likes']= like
    canal['tiempo de reproduccion']= tiempo
    canal['suscriptores']= seguidores
    print("""
            ┌─────────────────────────────────────────────────────────┐
            │       Elija cual metodo usa para generar ganacias       │
            │_________________________________________________________│
            │                                                         │
            │    1- Publicidad en los videos                          │
            │    2- Membresías de YouTube                             │
            │                                                         │
            └─────────────────────────────────────────────────────────┘ 
            """) 
    opcion=int(input("ingrese la por cual metodo obtiene ganacias responda (1 0 2): "))
    
    if canal['tiempo de reproduccion'] > 0:

        if opcion==1:
            tarifa=float(input("ingrese la tarifa de youtube por (1000) visualizaciones: "))
            ganancia1=tarifa*(visualizaciones/1000)
            print("el total ganado de la publicidad de su canal es: ",ganancia1)
        elif opcion==2:
            membresia=float(input("ingrese el precio que usted eligio para la membresia de su canal: "))
            suscritos=int(input("cuantas personas estan susbcritas a esta membresia: "))
            if suscritos<=seguidores:
                ganancia2=(suscritos*membresia)*0.70
                print("el total ganado de la suscripcion de su canal es: ",ganancia2)
                exit()
            else:
                print("ERROR, ingrese de nuevo los datos")
        else:
            print("Error intente denuevo")
    

    
buscar=input("que informacion desea ver: visistas , likes, tiempo de reproduccion, suscriptores ")

if buscar=="visitas":
    visitas = canal.get('visitas', 0)
    print(visitas)
elif buscar=="likes":
    likes = canal.get('likes', 0)
    print(likes)
elif buscar=="tiempo de reproduccion":
    tiempo_rep = canal.get('tiempo de reproduccion', 0)
    print(tiempo_rep)
elif buscar=="suscriptores":
    fans = canal.get('suscriptores', 0)
    print(fans)
else:
    print("Opcion invalida")
print("deseas borrar los datos?")

borrar=input("¿Desea borrar la informacion de la base de datos? si/no ")
if borrar=="si":
    canal.clear()
else:
    exit()