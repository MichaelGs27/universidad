import pywhatkit as kit
import time

def enviar_mensajes(numero, mensaje, cantidad):
    """
    Envía múltiples mensajes de WhatsApp a un número específico.
    
    Args:
        numero (str): Número de WhatsApp con el formato +[código de país][número].
        mensaje (str): Mensaje que deseas enviar.
        cantidad (int): Cantidad de mensajes que se enviarán.
    """
    for i in range(cantidad):
        try:
            # Envía un mensaje con un intervalo entre envíos
            kit.sendwhatmsg_instantly(numero, mensaje, wait_time=1)
            print(f"Mensaje {i+1} enviado correctamente.")
            time.sleep(1)  # Evitar bloqueo o exceder límites
        except Exception as e:
            print(f"Error al enviar el mensaje {i+1}: {e}")

# Ejemplo de uso:
numero_telefono = "+573045425321"  # Cambia por el número deseado
mensaje_texto = "¡Hola! Este es un mensaje automatizado."
cantidad_mensajes = 5

enviar_mensajes(numero_telefono, mensaje_texto, cantidad_mensajes)