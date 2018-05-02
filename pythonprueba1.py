# organizacion de empleados enpytho

class Empleados:
	def __init__(self, nombre, apellido, sueldo):
		self.nombre = nombre
		self.apellido = apellido
		self.sueldo = sueldo
		self.correo = nombre + '.'+apellido + '@gmail.com'

	def fullname(self):
		return self.nombre + self.apellido

empleado1 = Empleados('Pedro', 'Porras', 10000)
empleado2 = Empleados('Mike', 'Flores', 10000)
empleado3 = Empleados('Toño', 'Villa', 15000)

print(empleado1.fullname())
