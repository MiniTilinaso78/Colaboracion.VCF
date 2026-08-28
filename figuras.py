#Este codigo es de prueba 
nombrefigura=input("Ingrese el nombre de la figura: Triangulo, Rectangulo o Circunferencia")

#Lo haremos con funciones; mi espacio: lineas 6-26, Vanessa: lineas 27-57 y Carlos: lineas 58-78














































def areatriangulo (base,altura):
    area = base * altura
    return area













escorrecto = True

while escorrecto == True:
    valor1 = int(input("Ingrese la medida de la base del rectangulo"))
    valor2 = int(input("Ingrese la medida de la altura del resctangulo"))
    resultado = areatriangulo(valor1,valor2)
    if resultado < 0: 
        print ("No se permiten numeros negativos")
        escorrecto = True
    else:
        print("el area es ",resultado" metros cuadrados")
        escorrecto = False

























