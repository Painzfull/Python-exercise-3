"""
1 den 10 a kadar olan sayıları çarpım olarak bastıracağım
"""
for i in range(1,11):
    print("Listedeki sayıların çarpımı")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))