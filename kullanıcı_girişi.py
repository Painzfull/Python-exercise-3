print("""
##############################################
Kullanıcı Girişi Programı
      
##############################################

""")
sys_kullanıcı_adı = "mete can "
sys_parola = "12345"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adı hatalı")
        giriş_hakkı -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalı")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı")
        giriş_hakkı -= 1
    else:
        print("Sisteme giriş yapılıyor")
        break
    if(giriş_hakkı == 0):
        print("Giriş Hakkı Kalmadı")
        break

