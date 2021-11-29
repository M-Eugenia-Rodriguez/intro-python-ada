import datetime

class Persona(object):

    def __init__(self, dni,fecha_nacimiento, nombre="", edad=0):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"nombre : {self.nombre} edad :{self.edad} dni : {self.dni}")

    def edad(self):
        hoy = datetime.datetime.now().date()
        fecha_nacimiento = datetime.date(1989, 3, 15)
        edad = =int((td-bd). days /365.25)

    def es_mayor_de_edad(self, edad):
        if edad >= 18:
            return True
        else:
            return False