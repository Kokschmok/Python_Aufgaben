print("Berechnung der Oberfläche und des Volumens eines\nZylinders aus dessen Radius und Länge.")
Zradius = input('Radius des Zylinders (in m): ')
Zlaenge = input('Länge des Zylinders (in m): ')
radius = float(Zradius)
laenge = float(Zlaenge)

print("\nFür einen Zylinder mit einem Radius von " + str(radius) + "m\nund einer Länge von " + str(laenge) + "m ergeben sich folgende Werte:")

Zvolumen   = 3.1416 * (radius)**2
Zvolumen = round(Zvolumen, 2)

Zoberflaeche = 2 * 3.1416 * radius * laenge
Zoberflaeche = round(Zoberflaeche, 2)

print("\nVolumen des Zylinders: " + str(Zvolumen) + " Kubikmeter\nOberfläche des Zylinders: " + str(Zoberflaeche) + " Quadratmeter")
print("\nDie Berechnung wurde von Elyesa Sentürk durchgeführt.1")