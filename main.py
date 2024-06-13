import os
import colorama

colorama.init()
#from replit import clear

Fragen = ["hi1", "Hi2"]
Parteien = {"Me": [1, 2], "You": [2, 2]}


def Balken(zeichen, length, punkte, maximal):
  output = ""
  count = 0
  while count < length * punkte / maximal:
    output += colorama.Back.GREEN + zeichen
    count += 1
  while count < length:
    output += colorama.Back.RED + zeichen
    count += 1
  output += colorama.Back.RESET
  return output


print(Balken(" ", 35, 70, 100))  #


def Vergleich(Antworten, Partei):
  while 3 in Antworten:
    ind = Antworten.index(3)
    Partei.pop(ind)
    Antworten.pop(ind)
  count = 0
  points = 0
  while count < len(Antworten):
    antwort = Antworten[count]
    partei = Partei[count]
    points += 2 - max(partei, antwort) + min(partei, antwort)
    count += 1
  print(points)
  ret = str(50 * points / len(Antworten)) + ".0000"
  ret = ret[:ret.index(".") + 2] + "%"
  return [points, 2 * len(Antworten), ret]


def Antwortmoeglichkeiten():
  Antwortmoeglichkeiten = (colorama.Fore.GREEN + """0 Zustimmung
""" + colorama.Fore.YELLOW + """1 Neutral
""" + colorama.Fore.RED + """2 Ablehnung
""" + colorama.Fore.RESET + """3 Überspringen""")
  print(Antwortmoeglichkeiten)


Antworten = []
count = 0
while count < len(Fragen):
 # clear() ##
  #pass
  print(Fragen[count])
  Antwortmoeglichkeiten()
  Antworten.append(input(" "))
  if Antworten[-1] in ["0", "1", "2", "3"]:
    count += 1
    Antworten[-1] = int(Antworten[-1])
  else:
    Antworten.pop(len(Antworten) - 1)
#print(Antworten)  #
#print(Vergleich(Antworten, Parteien["Me"])[2])#
Vergleichsprozent = {}
Parteibalken = {}
Prozente = []
Parteien_Ab = []
for partei in Parteien.keys():
  Vergleichsprozent.update({partei: Vergleich(Antworten, Parteien[partei])})
  Parteibalken.update({
      partei:
      Balken(" ", 60, Vergleichsprozent[partei][0],
             Vergleichsprozent[partei][1])
  })
  #print(Parteibalken[partei])
  #print(partei)
  #print(Vergleichsprozent)
  Prozente.append(float(Vergleichsprozent[partei][2][:-1]))
  Parteien_Ab.append(partei)
Prozente.sort(reverse=True)
#print(Prozente)
#clear()
while len(Parteien_Ab) > 0:
  for partei in Parteien_Ab:
    if float(Vergleichsprozent[partei][2][:-1]) == Prozente[0]:
      print(partei + "  " + Vergleichsprozent[partei][2])
      print(Parteibalken[partei])
      Parteien_Ab.remove(partei)
      Prozente.pop(0)
