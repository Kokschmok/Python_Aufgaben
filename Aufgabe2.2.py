print("Geben Sie die Punktkoordinaten der Strecke PQ an:\n")
p_x = input("x-Koordinate des Punktes P: ")
p_y = input("y-Koordinate des Punktes P: ")
q_x = input("x-Koordinate des Punktes Q: ")
q_y = input("y-Koordinate des Punktes Q: ")

p_x = int(p_x)
p_y = int(p_y)
q_x = int(q_x)
q_y = int(q_y)

m_x = (p_x + q_x)/2
m_y = (p_y + q_y)/2

print("\nDie Strecke mit den Endpunkten P(" + str(p_x) + "," + str(p_y) + ") und Q(" + str(q_x) + "," + str(q_y) + ")\nbesitzt den Mittelpunkt M(" + str(m_x) + "," + str(m_y) + ").")

if(m_x>0):
    print("Der Mittelpunkt befindet sich oberhalb der x-Achse")
elif(m_x==0):
    print("Der Mittelpunkt befindet sich auf der x-Achse")
elif(m_x<0):
    print("Der Mittelpunkt befindet sich unterhalb der x-Achse")

print("\nDie Berechnung wurde von Elyesa Sentürk durchgeführt")