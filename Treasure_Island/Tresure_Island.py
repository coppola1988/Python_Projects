print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Willkommen zu Treasure Island.")
print("Du bist auf einer geheimnisvollen Insel gelandet, auf der Suche nach dem legendären Schatz des Piratenkönigs.")

print("Szene 1: Der Strand\nDu stehst am Strand und blickst auf das endlose Meer hinaus.\n"
      "Hinter dir liegt ein dichter Dschungel.")

choose = input("Wohin möchtest du gehen? 'A': Dschungel oder 'B': Folge dem Strand\n")
choose1 = choose.lower()


if choose1 == 'a':
    print("Der Dschungel verschlingt dich mit seinem dichten Blätterdach.\n")
    choose = input("Du findest einen Pfad, der sich vor dir gabelt. 'A': Links oder 'B': Rechts")
    choose1 = choose.lower()
    if choose1 == 'b':
        print("Rechts entdeckst du eine alte Schatzkarte an einem Baum.")
        choose = input("'A': Folge der Karte oder 'B': Ignoriere die Karte.")
        choose1 = choose.lower()
        if choose1 == 'a':
            print("Die Karte führt dich zu einer verborgenen Höhle voller Gold und Juwelen.\n"
                  "Du hast den Schatz gefunden!\n"
                  "   HERZLICHEN GLÜCKWUNSCH!!!")
        else:
            print("Ohne die Karte wanderst du ziellos umher und verlierst dich im Dickicht.\n"
                  "Das Abenteuer endet hier!\n"
                  "     GAME OVER!")
    else:
        print("Ein falscher Schritt und du fällst in die tiefe Grube. Das Abenteuer endet hier!\n"
              "    GAME OVER!")
elif choose1 == 'b':
    print("Am Strand findest du eine Flaschenpost,die im Sand halb vergraben ist.\n")
    choose = input("'A': Öffne die Flasche. oder 'B': Lasse sie liegen.")
    choose1 = choose.lower()
    if choose1 == 'a':
        print("In der Flasche befinden sich ein Schlüssel und eine Notiz mit Hinweisen zum Schatz.")
        choose = input("'A': Suche nach dem Schloss für den Schlüssel oder"
                       " 'B': Schwimme davon in der Hoffnung auf Rettung.")
        choose1
        choose1 = choose.lower()
        if choose1 == 'a':
            print("Deine Suche führt dich zu einer verborgenen Höhle am Fuße eines Kliffs.\n"
                  "Der Schlüssel passt zu einem alten Schloss an einer steinernen Tür.\n"
                  "Dahinter liegt der Schatz!\n"
                  "   HERZLICHEN GLÜCKWUNSCH!!!")
        else:
            print("Du versuchst zu schwimmen, aber die Strömungen sind zu stark.\n"
                  "Du wirst ins offene Meer gezogen. Das Abenteuer endet hier!\n"
                  "     GAME OVER!!!")
    else:
        print("Du lässt die Flasche liegen und gehst weiter am Strand entlang.\n"
              "Doch bald darauf wirst du von den Geistern"
              " ehemaliger Piraten heimgesucht.\nDas Abenteuer endet hier!\n "
              "        GAME OVER!")
else:
    print("Das war leider keine korrekte Eingabe! Game Over!")
