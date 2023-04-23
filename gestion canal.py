import random

visualizaciones=0
likes=0
seguidores=0
tiempo=0
video=0
ganancias=0
# Gestion del canal
canal = {}
nombre=input("Digite el nombre de su canal: ")
descripcion=input("Ingrese la descripción de su canal: ")
videos=int(input('Ingrese la cantidad de videos que tiene: '))

while videos > 0:
    
    video+=1
    
    print("VIDEO NUMERO ", video)
    suscripciones_vid=random.randint(250, 2000)
    visitas = random.randint(1000, 100000)
    likes_vid = random.randint(1000, 15000)
    comentarios = random.randint(50, 300)
    tarifa= random.randint(2,32)

    print("Datos del video subido a YouTube:")
    print("Suscripciones: ",suscripciones_vid)
    print("Visitas:", visitas)
    print("Likes:", likes_vid)
    print("Comentarios:", comentarios)
    
    seguidores+=suscripciones_vid
    visualizaciones+=visitas
    likes+=likes_vid
    
    while True:
        try:
            duracion=float(input("Cuánto tarda el video en minutos: "))
            if duracion > 0:
                break
            else:
                print("ERROR: La duración del video debe ser mayor a 0.")
        except ValueError:
            print("ERROR: Ingrese un valor numérico válido para la duración del video.")

    segundos=duracion*60
    horas=segundos / 3600
    time=horas*visitas
    tiempo+=int(time)
    ganancia = tarifa * (visualizaciones / 1000)
    ganancias+=ganancia
    
    
    videos -= 1
    canal['visitas'] = visualizaciones
    canal['likes']= likes
    canal['tiempo de reproduccion']= tiempo
    canal['suscriptores']= seguidores
    canal['dinero']= ganancias
    
while True:
    try:  
        buscar=input("Qué información desea ver: (1) visitas, (2) likes, (3) tiempo de reproducción, (4) suscriptores, (5) ganancias, (6) salir? ")

        if buscar=="visitas" or buscar=="1":
            visitas = canal.get('visitas', 0)
            print(visitas)
        elif buscar=="likes" or buscar=="2":
            likes = canal.get('likes', 0)
            print(likes)
        elif buscar=="tiempo de reproducción" or buscar=="3":
            tiempo_rep = canal.get('tiempo de reproduccion', 0)
            print(tiempo_rep)
        elif buscar=="suscriptores" or buscar=="4":
            fans = canal.get('suscriptores', 0)
            print(fans)
        elif buscar=="ganancias" or buscar=="5":
            dinero_USD= canal.get('dinero')
            print(dinero_USD)
        elif buscar=="salir" or buscar=="6":
            print("¡Hasta luego!")
            break
        else:
            print("ERROR: Opción inválida. Por favor, seleccione una opción válida.")
    except Exception as e:
        print("ERROR: Ocurrió un error. Por favor, inténtelo de nuevo. Detalles del error:", str(e))
