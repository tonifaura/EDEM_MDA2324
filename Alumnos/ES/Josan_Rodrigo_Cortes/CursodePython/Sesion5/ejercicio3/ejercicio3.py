'''Ejercicio 3
Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión'''

from ejercicio2 import Automovil
	
class Moto(Automovil):
	
 
	def __init__(self, marca,modelo,color,matricula,id_seguro,titular,velocidad,ruedas,tipo):
        #Aquí haríamos uso del constructor de super
		super().__init__(self, marca,modelo,color,matricula,id_seguro,titular,velocidad,ruedas,tipo)
            self.marca=marca
            self.modelo=modelo
            self.color=color
            self.matricula=matricula
            self.id_seguro=id_seguro
            self.titular=titular
            self.velocidad=velocidad
            self.ruedas = ruedas 
            self.tipo=tipo
 
	def tumbarEnLasCurvas():
            print("La moto esta tomando una curva y va casi rozando el suelo")
			
moto=Moto(tipo="Carretera")
print(moto)