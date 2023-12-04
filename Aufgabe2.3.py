print("Für den folgenden Bereich ganzer Zahlen wird die Summe,\ndie Summe der Quadrate und die Summe der Kubikzahlen berechnet.")
m = input("Anfangswert m = ")
n = input("Endwert n = ")
zsumme = 0
qsumme = 0
ksumme = 0
m = int(m)
n = int(n)

i=m

for i in range(i,n+1):
    zsumme = zsumme + i

i=m

for i  in range(i,n+1):
    qsumme = qsumme + i**2

i=m

for i in range(i,n+1):
    ksumme = ksumme + i**3

print("\nFür die ganzen Zahlen von " + str(m) + " bis " + str(n) + " ergibt sich:\nDie Summe der Zahlen beträgt " +
      str(zsumme) + "\nDie Summe der Quadratzahlen beträgt " + str(qsumme) + "\nDie Summe der Kubikzahlen beträgt " + str(ksumme))

print("Die Berechnung wurde von Elyesa Sentürk durchgeführt.")