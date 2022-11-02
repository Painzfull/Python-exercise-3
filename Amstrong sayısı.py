"""
amstrong sayısını bulma programı

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
sayı = input("Bir sayı değeri giriniz:")
basamak_sayısı = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

geçici_sayı = sayı

while(geçici_sayı > 0):

    basamak = geçici_sayı % 10

    toplam += basamak ** basamak_sayısı

    geçici_sayı //= 10

if(toplam == sayı):
    print(sayı,"Bir amstrong sayısıdır.....")
else:
    print(sayı,"Bir amstrong sayısı değildir....")
