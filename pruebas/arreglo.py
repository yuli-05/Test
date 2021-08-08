def ordenar(array):
    array.sort()
    return array

def per_mayores(diccionario):
    count = 0
    for i in diccionario:
        if i.get("edad") < 18:
            pass
        else:
            count = count+1
    print("Existen: ",count," personas mayores de edad registradas")
    return count