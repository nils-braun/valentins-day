import numpy as np


def greatest():
    product = []
    f = open('/home/sophie/Projekte/Python/valentins-day/exercises/second.dat', 'r')

    data = f.readline()
    data = data.strip("\n")

    for j in range(len(data)-12):
        sum = 1
        for i in np.arange(j, j+ 13):
            sum *= int(data[i])
        product.append(sum)
        #print(sum)

    # Maximum und Position des Max finden und dann diesen Ausschnitt zurück geben
    max_product = max(product)
    position = product.index(max_product)
    result = [int(data[i]) for i in np.arange(position, position+13) ]
    return result

print(greatest())