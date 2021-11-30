from datetime import date

class Persona(object):

    def __init__(self, dni,fecha_nacimiento, nombre="", edad=0):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"nombre : {self.nombre} edad :{self.edad} dni : {self.dni}")

    def edad(self, fecha_nacimiento):
        fecha_actual = datetime.date.today()
        edad = fecha_actual.year - fecha_nacimiento.year
        return edad


    def es_mayor_de_edad(self, edad):
        if edad >= 18:
            return True
        else:
            return False