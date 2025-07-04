import random
import time

oyuncu1= {

    "name":"devo",
    "puan":0

}

oyuncu2 = {
    "name":"beko",
    "puan":0
}



while (oyuncu1["puan"]<30 and oyuncu2["puan"]<30):
    tahmin1=random.randint(1,6)
    oyuncu1["puan"]+=tahmin1
    print(f"{oyuncu1['name']} isimli oyuncunun tahmini: {tahmin1}")

    tahmin2=random.randint(1,6)
    oyuncu2["puan"]+=tahmin2
    print(f"{oyuncu2['name']} isimli oyuncunun tahmini: {tahmin2}")

    print("*"*50)


    print(f"{oyuncu1['name']} isimli oyuncunun puanı: {oyuncu1['puan']}")
    print(f"{oyuncu2['name']} isimli oyuncunun puanı: {oyuncu2['puan']}")

    print()
    print()
    print()

    time.sleep(5)

    if(oyuncu1["puan"]>=30>oyuncu2["puan"]):
        print(f"{oyuncu1['name']} isimli oyuncu {oyuncu1['puan']} - {oyuncu2['puan']} kazandı!")
        break
    elif(oyuncu2["puan"]>=30>oyuncu1["puan"]):
        print(f"{oyuncu2['name']} isimli oyuncu {oyuncu2['puan']} - {oyuncu1['puan']} kazandı!")
        break
    elif(oyuncu1["puan"]>=30 and oyuncu2["puan"]>=30):
        print("oyun berabere")
        break

        

    


