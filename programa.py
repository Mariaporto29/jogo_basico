import random
ninja = input("Qual é seu ninja predileto de NARUTO?")
print ("LEGAL ESSE(a)",ninja, "é muito pika!")

while True:
   ninja_secreto = random.choice(["naruto", "itachi", "gaara", "ino", "sasuke", "sakura"])
   palpite = (input("tente adivinha qual ninja eu estou pensando..."))

   if palpite.lower == ninja_secreto:
      print("Uau que jutsu você utilizou em?")
   
   else:
       print("Otário o ninja era o(a)", ninja_secreto)

       resposta = input("QUER JOGAR NOVAMENTE? (s/n):")

   if resposta == "n":
            print("Então chega o fim de mais um ninja, até!")
            break
   palpite = (resposta)

