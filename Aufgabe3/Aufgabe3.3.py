import turtle
import turtle as t

turtle.bgcolor('black')


def fktNEck(n, laenge, xPos, yPos):
    t.pu()
    t.setpos(xPos, yPos)
    t.pencolor('red')
    t.pd()
    recursion(n, laenge, n)


def recursion(n, laenge, index):
    if index > 0:
        t.forward(laenge)
        t.left(360 / n)
        recursion(n, laenge, index - 1)


while True:
    n = int(input("Anzahl der Ecken (Abbruch mit 0): "))
    if (n==0):
        break
    laenge = int(input("Seitenlänge des: "))
    xPos = int(input("x-Anfangskoordinate: "))
    yPos = int(input("y-Anfangskoordinate: "))
    fktNEck(n, laenge, xPos, yPos)

print("Die Zeichnung der n_ecke wurde durchgeführt von: Elyesa Sentürk")
t.done()
