from pytube import YouTube #Libreria de youtube
from colorama import * #Libreria de colores en python
import os
def completo(stream, filepath):
    print(Fore.MAGENTA + 'Ubicación \033 '+ filepath, Style.RESET_ALL)#Mostramos la ubicación del archivo y resetteamos los colores
def cargando(stream, chunk, bytes_remaining):
    proceso = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%' #Hacemos una operación para mostrar el porcentaje
    print('\n'+Fore.RED + proceso)

#https://www.youtube.com/watch?v=C9qxnGlS3PQ

init() #Iniciamos la libreria colorama
ubicacion = r'C:\Users\TomiCat xD\Downloads' #Variable para la ruta, lo mejorare a una ventana ;)

#Descargar
while True: #Empezamos a iniciar un menu interactivo
    link = input('\n Youtube link: ') #Ingresamos un link de youtube
    video= YouTube(link,on_complete_callback=completo,on_progress_callback=cargando)#Mandamos a llamar la función principal de la libreria pytube y le pasamos en parametros las funciones
    while True: #Empezamos el segundo menu interactivo
        #Informacion del video
        print(Style.BRIGHT + Fore.YELLOW + f'Titulo:      \033[39m {video.title}')
        print(Fore.YELLOW + f'Duración:    \033[39m { round(video.length / 60,2)} minutes') #Operación para tener los minutos exactos
        print(Fore.YELLOW + f'Vistas:      \033[39m { video.views / 1000000} million') #Lo hice en caso de que tenga un millon de vistas
        print(Fore.YELLOW + f'Author:      \033[39m {video.author}')

        #Opcciones
        print(
            Fore.GREEN + 'Descargar en calidad:' + 
            Fore.RED + ' (A)lta \033[39m|' + 
            Fore.CYAN + '(B)aja \033[39m|' + 
            Fore.BLUE + '(S)onido \033[39m| (E)xit')
        opcciones = input('Opcción: ')
        posible_error = opcciones.lower() #Lo pasamos a minusculas por si viene un gracioso
        if posible_error=='a':
            video.streams.get_highest_resolution().download(ubicacion)#Descargamos el video con maxima resolución junto con el link y los parametros ya dados y lo guardamos en la variable ubicación
        elif posible_error == 'b':
            video.streams.get_lowest_resolution().download(ubicacion)#De calidad media-baja
        elif posible_error == 's':
            audio = video.streams.filter(only_audio=True).first()#Filtramos el tipo audio
            descarga = audio.download(ubicacion)#Obción de audio mp3
            base, ext = os.path.splitext(descarga)#Preparamos para pasarlo de mp4 a mp3
            nuevo = base + '.mp3'#Le cambiamos la extención
            os.rename(descarga, nuevo)#Ya que descargamos lo convertimos a mp3
        elif posible_error == 'e':
            exit()#Para cancelar la consola
        pregunta = input('\n¿Quieres repetir? y/n: ') #Aqui empiza el menu interactivo
        pregunta2 = pregunta.lower()
        if pregunta2 == 'y':
            break #En caso de que quiera otro video, se le hara otra otra vez la petición de el link de dicho video
        elif pregunta2 == 'n':
            exit() #Si no, entonces cancelamos consola