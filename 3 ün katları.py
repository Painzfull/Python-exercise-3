"""
birden 100 e kadar olan sayılar içinde 3 ün katları olan sayıları bastıracağım.....
"""
for i in range (1,101):
    if(i % 3 != 0):
        continue
    print(i)
