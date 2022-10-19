print("""
################################################
ATM Programı
İşlemler:
1-Bakiye Sorgulama 
2_Para Yatırma
3-Para Çekme

Programı sonlandırmak için "q" tuşuna basın
################################################
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if(işlem == "q"):
        print("İYİ GÜNLER DİLERİZ")
        break
    elif(işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif(işlem == "2"):
        miktar = int(input("yatırmak istediğiniz tutarı giriniz:"))

        bakiye += miktar

    elif(işlem == "3"):
        miktar = int(input("çekmek istediğiniz tutarı giriniz:"))
        if(bakiye - miktar < 0):
            print("Bakiye Yetersiz!!!!!!!")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz işlem")