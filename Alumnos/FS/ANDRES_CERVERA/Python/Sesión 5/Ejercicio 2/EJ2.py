#Crea una clase Automóvil que disponga de los atributos necesarios y métodos para: Arrancar, Acelerar, Frenar, Parar

class Automovil:
    
    def __init__(auto, marca, modelo):
        auto.marca = marca
        auto.modelo = modelo
        auto.velocidad = 0
        auto.encendido = False
        
    def arrancar(auto):
        if not auto.encendido:
            auto.encendido = True
            print(f'Coche arrancado')
            print(f'La velocidad del coche es {auto.velocidad} KM/H')
        else:
            print(f'Ya estaba arrancado')
            print(f'La velocidad del coche es {auto.velocidad} KM/H')
            
    def acelerar(auto, velocidad):
       auto.velocidad = auto.velocidad + velocidad
       print(f'Acelerando...\n'
             f'La velocidad del coche es {auto.velocidad} KM/H')
    
    def acelerar(auto, velocidad):
       auto.velocidad = auto.velocidad + velocidad
       print(f'Acelerando...\n'
             f'La velocidad del coche es {auto.velocidad} KM/H')
            
        
coche = Automovil(marca = 'Alfa Romeo', modelo= 'Giulietta')
coche.arrancar()
coche.acelerar(10)
