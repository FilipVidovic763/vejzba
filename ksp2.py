
import random

bot_izbori = ["Papir", "Škare", "Kamen"]
igraj = "Da"
bodovi = int(0)

while igraj == "Da":
    print("=" * 20)
    igrac = str(input("Talion: "))
    bot = random.choice(bot_izbori)
    print("Ork je odabrao {}".format(bot))
    print("=" * 20)
    
    if(igrac == bot):
        print("\nIzjednačeno!")
    elif(igrac == "Papir"):
        if(bot == "Kamen"):
            print("\nTalion je pobijedio!")
            bodovi += 1
        elif(bot == "Škare"):
            print("\nOrk je pobijedio!")
            bodovi -= 1
    elif(igrac == "Kamen"):
        if(bot == "Škare"):
            print("\nTalion je pobijedio!")
            bodovi += 1
        elif(bot == "Papir"):
            print("\nOrk je pobijedio!")
            bodovi -= 1
    elif(igrac == "Škare"):
        if(bot == "Papir"):
            print("\nTalion je pobijedio!")
            bodovi += 1
        elif(bot == "Kamen"):
            print("\nOrk je pobijedio!")
            bodovi -= 1
    else:
        print("\nTalion je unio krivu vrijednost.")

    print("Talion ima {} bodova.".format(bodovi))

    igraj = input("Ponovi igru? (Da/Ne)")