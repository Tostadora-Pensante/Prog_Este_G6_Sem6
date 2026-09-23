vector = []
vector.append(2)
vector.append(5)
vector.append(9)
print(vector)
#To show the size of the vector.
print("Size of each vector")
print(len(vector))
#Para mostrar el doble de cada elemento
print("EL doble de cada elemento")
for i in range(len(vector)):
    if i !=(len(vector)-1):
        print(vector[i]*2,  end = ", ")
else:
    print(f"{vector[i]*2}.")

#agregar a la posicion 1
vector.insert(1, 36)
print (vector)