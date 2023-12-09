'''Ejercicio 3
Crea clases de automóvil distintas como y que dispongan de distintos atributos, pero hereden los métodos de Automóvil a la hora de Arrancar, Acelerar, Frenar o Parar, salvo que algunos deben tener más potencia que otros:
Coche
Moto
Camión'''

from ejercicio2 import Automovil
	
class Moto(Automovil):
    def __init__(self, marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas, tipodemoto):
        # Llamamos al constructor de la clase base (Automovil)
        super().__init__(marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas)
        # Atributo adicional específico de la clase Moto
        self.tipo_moto = tipodemoto

    # Métodos adicionales o sobrescritos específicos de la clase Moto
    def realizar_acrobacia(self):
        print(f"La moto ha realizado una acrobacia.")
			


class Camion(Automovil):
    def __init__(self, marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas, capacidad_carga):
        # Llamamos al constructor de la clase base (Automovil)
        super().__init__(marca, modelo, color, matricula, id_seguro, titular, velocidad, ruedas)
        # Atributo adicional específico de la clase Camion
        self.capacidad_carga = capacidad_carga

    # Métodos adicionales o sobrescritos específicos de la clase Camion
    def cargar_mercancia(self):
        print(f"El camión ha cargado mercancía.")




# Crear una instancia de Moto
moto_ejemplo = Moto(marca="Honda", modelo="CBR", color="Rojo", matricula="ABC123", id_seguro="12345",
                    titular="Juan", velocidad=0, ruedas=2, tipo_moto="Deportiva")

# Acceder a atributos y métodos de la clase base
print(moto_ejemplo.velocidad)  # Imprimir velocidad
moto_ejemplo.arrancar()         # Llamar al método arrancar de la clase base

# Llamar a métodos específicos de la clase Moto
moto_ejemplo.realizar_acrobacia()