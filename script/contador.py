import time
from pynput import keyboard

tiempo_inicio = None
en_ejecucion = False

print("=== CRONOMETRO DE REACCION PARA MODELOS WEB ===")
print("Instrucciones:")
print("1. Carga la imagen en la interfaz web de la IA.")
print("2. Presiona ENTER para enviar el mensaje e iniciar el conteo.")
print("3. Cuando la IA termine de responder, presiona ESC para detener el tiempo.")
print("------------------------------------------------")


def al_presionar(tecla):
    global tiempo_inicio, en_ejecucion

    try:
        if tecla == keyboard.Key.enter and not en_ejecucion:
            tiempo_inicio = time.time()
            en_ejecucion = True
            print("\nEnvio detectado. Cronometro iniciado.")

        elif tecla == keyboard.Key.esc and en_ejecucion:
            tiempo_fin = time.time()
            en_ejecucion = False
            latencia = tiempo_fin - tiempo_inicio
            print(f"Respuesta finalizada. Tiempo registrado: {latencia:.2f} segundos")
            print("Listo para la siguiente prueba. Presiona ENTER para iniciar otra vez o Ctrl+C para salir.")

    except Exception as error:
        print(f"Error en la lectura de teclado: {error}")


with keyboard.Listener(on_press=al_presionar) as listener:
    listener.join()
