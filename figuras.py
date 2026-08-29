#Este codigo es de prueba 
nombrefigura=input("Ingrese el nombre de la figura: Triangulo, Rectangulo o Circunferencia")

#Lo haremos con funciones; mi espacio: lineas 6-26, Vanessa: lineas 27-57 y Carlos: lineas 58-78
print("Solo numeros positivos")

if nombrefigura.lower()=="triangulo" or nombrefigura.lower()=="rectangulo":
    medida1=int(input("Ingresa la altura: "))
    medida2=int(input("Ingresa el tamaño de la base: "))

elif nombrefigura.lower()=="circunferencia":
    medida1=int(input("Ingresa la medida del radio: "))
    medida2=int(input("Ingresa los digitos que desees de pi: "))
else: 
    print("LOL que mal escriba bien :p ")



def areacircunferencia(radio,pi):
    medidas=[]
    medidas.append(radio*radio*pi)
    medidas.append(radio*2*pi)
    return medidas

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# quiero ver si agragando esto eso estoy en mi rama o en la main 
#porque los archivos son iguales










































































