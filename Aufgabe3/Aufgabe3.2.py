print("Bestimmung der Lichtfarbe aus der Wellenlänge.\n")
while True:
    wl = int(input("Eingabe der (ganzzahligen) Wellenlänge in nm: "))
    if wl > 780:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: nicht sichtbar!")
    elif wl > 649:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: Rot")
    elif wl > 584:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: Orange")
    elif wl > 574:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: Gelb")
    elif wl > 489:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: Grün")
    elif wl > 419:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: Blau")
    elif wl > 379:
        print("Die Wellenlänge", str(wl), "nm entspricht einer Lichtfarbe von: Violett")
    elif wl == 0:
        print("Sie haben das Programm beendet!")
        break
    else:
        print("Die Wellenlänge\t", str(wl), "nm entspricht einer Lichtfarbe von: nicht sichtbar!")

print("\nDas Programm wurde ausgeführt von Elyesa Sentürk.")
