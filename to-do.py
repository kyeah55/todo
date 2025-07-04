secim=2 # seçilen sayı 1 ile 4 arası girilecek kontrol yapmaya gerek yok, 2 atanmasının sebebi döngüye girmek

gorevler=[]

def menu():
    print("[1] Görev Ekle\n[2] Görevleri Listele\n[3] Görev Sil\n[4] Çıkış")
    print("*"*50)


def gorevEkle(gorev):
    gorevler.append(gorev)

def gorevleriListele():

    sayac=1
    for items in gorevler:
        print(f"{sayac}- {items}")
        sayac+=1

def gorevleriSil():
    gorevleriListele()
    silinen=int(input("Hangi görevi silmek istiyorsunuz?"))

    del gorevler[silinen-1]

    print("Görev başarıyla silindi! Yeni liste:\n")
    gorevleriListele()

def exiting():
    print("Görüşmek üzere, görevlerini yaptığından emin ol!")

while secim!=4:

    menu()
    secim=int(input())

    if secim==1:
        eklenecekGorev=input("Eklemek istediğiniz görev nedir: ")
        gorevEkle(eklenecekGorev)
    elif secim==2:
        gorevleriListele()
    elif secim==3:
        gorevleriSil()
    elif secim==4:
        exiting()
