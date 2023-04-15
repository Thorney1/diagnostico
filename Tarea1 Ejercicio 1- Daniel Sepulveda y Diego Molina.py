class Mascota:
    def __init__(self, nombre, especie, raza, fecha_nacimiento):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento

class Dueño:
    def __init__(self, nombre, fecha_nacimiento, ciudad, mascota):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad = ciudad
        self.mascota = mascota

nombre = input("Ingrese el nombre del dueño: ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento del dueño (dd/mm/yyyy): ")
ciudad = input("Ingrese la ciudad del dueño: ")

nombre_mascota = input("Ingrese el nombre de la mascota: ")
especie = input("Ingrese la especie de la mascota: ")
raza = input("Ingrese la raza de la mascota: ")
fecha_nacimiento_mascota = input("Ingrese la fecha de nacimiento de la mascota (dd/mm/yyyy): ")

mascota = Mascota(nombre_mascota, especie, raza, fecha_nacimiento_mascota)

dueno = Dueño(nombre, fecha_nacimiento, ciudad, mascota)

print("Datos del dueño:")
print("Nombre:", dueno.nombre)
print("Fecha de nacimiento:", dueno.fecha_nacimiento)
print("Ciudad:", dueno.ciudad)

print("Datos de la mascota:")
print("Nombre:", dueno.mascota.nombre)
print("Especie:", dueno.mascota.especie)
print("Raza:", dueno.mascota.raza)
print("Fecha de nacimiento:", dueno.mascota.fecha_nacimiento)