goruntulenenler=[]
def goruntulenme():
    urun=input("Görüntülenen ürün:")
    goruntulenenler.append(urun)
            

def goruntulenmeSay():
    arananUrun=input("Aranan Ürün:")
    print("Görüntülenme sayısı:",goruntulenenler.count(arananUrun))


while True:
    secenek=input("Ürün görüntülemek istiyorsanız A harfine görüntüleme sayısi için B harfine tıklayınız:")

    if secenek=="A":
        goruntulenme()
    elif secenek=="B":
        goruntulenmeSay()
    elif secenek=="q":
        break    





