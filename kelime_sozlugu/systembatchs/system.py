import random

words = {
    "azim": "bir işi başarmak için gösterilen kararlılık ve çaba",
    "merhamet": "başkalarının sıkıntılarına karşı duyulan acıma ve yardım etme isteği",
    "keşif": "daha önce bilinmeyen bir şeyi bulma veya ortaya çıkarma",
    "özgürlük": "kısıtlama olmadan istediğini yapabilme durumu",
    "hayal": "zihinde canlandırılan düşünce veya düş",
    "cesaret": "korkuya rağmen bir şeyi yapabilme gücü",
    "bilge": "bilgili ve deneyimli kişi",
    "sadakat": "bağlılık ve güvenilirlik",
    "umut": "iyi bir şeyin gerçekleşeceğine inanma duygusu",
    "fedakârlık": "başkalarının iyiliği için kendi çıkarlarından vazgeçme",
    "sevinç" : "mutlu olma , huzurlu olma",
    "mutlu" : "huzurlu olma",
    "güven" : "bir kişinin niyetini iyi olduğunu düşünerek ona karşı oluşan bir duvar"

}



def GetAnswer(word : str):
    num1 = random.randint(1,2)
    num2 = random.randint(1,2)
    if word in words:
        if num1 == 1:
            print(f"                          {str(word.capitalize())} {words[word]} anlamına gelir. Başka ne sormak istersin?")
        elif num1 == 2:
            print(f"                          {str(word.capitalize())} {words[word]} anlamına gelir. İstediğin başka bir kelime var mı?")
    else:
        while True:
            ans = input("""                          Bilmiyorum ama istersen bana öğretebilirsin e/h:
                        sen:""").lower().strip()
            if ans not in ["e", "h"]:
                print("                          Lütfen e yada h yazınız")
            elif ans in ["e", "h"]:
                break 
            
        if ans == "e":
            wordx = input("Kelime : ")
            wordwr = input("Anlamı: ")
            words[str(wordx)] = str(wordwr)
            if num2 == 1:
                print(f"                          Tamamdır. Bana demeye çalışıyorsun ki {wordx} kelimesi {words[wordx]} anlamına gelir. ")
            elif num2 == 2:
                print(f"                          Tamamdır. Bana demeye çalışıyorsun ki {wordx} kelimesi {words[wordx]} demektir. ")
                
        else:
            print("pekala")