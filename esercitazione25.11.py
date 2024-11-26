print("Vincenzo "+"Thomas "+"Leo")
Vincenzo=int(input("Scegli l'età "))
Thomas=int(input("Scegli l'età "))
Leo=int(input("Scegli l'età "))

if Vincenzo<18:
    print("minorenne")
elif (40>Vincenzo>18):
    print("maggiorenne")
else:
    print("anziano")

if Thomas<18:
    print("minorenne")
elif (18<=Thomas>40):
    print("maggiorenne")
else:
    print("anziano")

if Leo<18:
    print("minorenne")
elif (18<=Leo>40):
    print("maggiorenne")
else:
    print("anziano")


operazione=str(input("Adesso scegli l'operazione "))

if operazione=="somma":
    print("La somma della loro età è: ", (Vincenzo+Thomas+Leo))
   
 
 