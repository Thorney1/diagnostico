from os import system

class Chistes:
    def __init__(self):
        self.chistes = [
            {"titulo": "Campo laboral", "texto": "\n¿Cuántos programadores hacen falta para cambiar una bombilla? \n–Ninguno, porque es un problema de hardware.\n"},
            {"titulo": "Todo bien, creo...", "texto": "\nError 0094782: No se detecta ningún teclado pulse una tecla para continuar."},
            {"titulo": "Apoyo emocional", "texto": "\n¿Qué le dice un .GIF a un .JPEG?\n -Anímate viejo."},
            {"titulo": "Practicas dudosamente efectivas", "texto": "\nNo te despedirán del trabajo, si nunca comentas tu código y además eres el único que sabe cómo funciona."},
            {"titulo": "Contados", "texto": "\nSólo hay 10 tipos de personas en este bendito mundo, las que entienden binario y las que no."}
        ]
    
    def mostrar_chiste(self):
        print(self.chistes[0]["titulo"]) # Mostrar el titulo del primer chiste
        print(self.chistes[0]["texto"]) # Mostrar el texto del primer chiste
        self.chistes = self.chistes[1:] + [self.chistes[0]] # Mover el primer chiste al final de la lista
    
chistes = Chistes()

while True:
    respuesta = input("¿Quieres ver un chiste? Responde con 'si' o 'no': ")
    if respuesta.lower() == "si":
        system("cls")
        while True:
            chistes.mostrar_chiste()
            input("\nPresione ENTER para el siguiente chiste o cierra si ya te aburrió\n")
            system("cls")
    elif respuesta.lower() == "no":
        print("Bueno, adiós!")
        exit()
        
    elif respuesta != "si" or "no":
        system("cls")
        print("Ingresa una respuesta de verdad porfa")

