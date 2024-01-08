print("Für den folgenden Bereich ganzer Zahlen wird die Summe,\ndie Summe der Quadrate und die Summe der Kubikzahlen berechnet.")
m = input("Anfangswert m = ")
n = input("Endwert n = ")
zsumme = 0
qsumme = 0
ksumme = 0
m = int(m)
n = int(n)

for i in range(m,n+1):
    zsumme = zsumme + i
    qsumme = qsumme + i ** 2
    ksumme = ksumme + i ** 3

print("\nFür die ganzen Zahlen von " + str(m) + " bis " + str(n) + " ergibt sich:\nDie Summe der Zahlen beträgt " ,"\t\t\t"+
      str(zsumme) + "\nDie Summe der Quadratzahlen beträgt " ,"\t"+ str(qsumme) + "\nDie Summe der Kubikzahlen beträgt " ,"\t\t"+ str(ksumme))

print("Die Berechnung wurde von Elyesa Sentürk durchgeführt.")