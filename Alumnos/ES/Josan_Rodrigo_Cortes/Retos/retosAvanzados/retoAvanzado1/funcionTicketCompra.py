from tienda import listaDiscos
from funcionpedidoCompra import pedidoCompra

def ticketCompra():

    print("TICKET DE COMPRA")
    mipedido=pedidoCompra()
    importeTotal=0
    print(f' NOMBRE\t|ARTISTA\t|AÑO\t|GENERO\t|DESCUENTO\t|PRECIO|\t|SUBTOTAL|\t|DESCUENTO|\t|TOTAL|')
    for discos in mipedido:
        #Creo las variables para acceder al valor de cada una de ellas en el bucle
        nombreDisco=discos["Nombre"]
        artistaDisco=discos["Artista"]
        anyoDisco=discos["Año"]
        precioDisco=discos["Precio"]
        generoDisco=discos["Genero"]
        descuentoDisco=discos.setdefault("Descuento",0)

        #Creo el if para darle el que corresponde a la clave Descuento
        if generoDisco=="Black Metal":
            descuentoDisco=(30)
        elif generoDisco=="Electro":
            descuentoDisco=(30)
        else:
            discos["Genero"]=(0)
        #Creo los totales y subtotales:
        if descuentoDisco!=0:
            importeSubtotal=precioDisco
            descuento=descuentoDisco/100
            importeTotalUnidad=importeSubtotal*descuento
        else:
            importeTotal=precioDisco
            importeTotalUnidad=importeSubtotal

        importeTotal+=importeTotalUnidad


        print(f' {nombreDisco:<1} {artistaDisco:<10} {anyoDisco:<10} {generoDisco:<10} {descuentoDisco:<10} {precioDisco:<10} {importeSubtotal:<10} {importeTotalUnidad:<10}')
        
        print(importeTotal)

ticketCompra()    

   