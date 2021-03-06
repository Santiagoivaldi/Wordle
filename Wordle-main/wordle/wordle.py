import linecache
import sqlite3
import random
ganador = 0
conexion=sqlite3.connect("banana.db")
intentos = 0
palabra = conexion.execute("SELECT palabra FROM Palabras ORDER BY RANDOM() LIMIT 1; ")
import time
from threading import Timer
pala = palabra.fetchone()[0]

pal = list(pala)

a = 0
solucion = []
max = int(input("Ingresa numero de intentos: "))
start = time.perf_counter()
for i in pala:
    solucion.append(" ")
while a < max:
    intento = input("Ingresa una palabra: ").lower()
    while len(intento) != 5:
        print("La palabra tiene que ser de 5 letras")
        intento = input("Ingresa una palabra: ").lower()
    b = 0
    for i in pala:
        if list(intento)[b] == pal[b]:
            solucion[b] = "="
        elif list(intento)[b] in pala and intento.count(list(intento)[b]) <= pal.count(list(intento)[b]):
            solucion[b] = "-"
        else:
            solucion[b] = " "
        b += 1  

    print(list(intento))
    print(solucion)
    if solucion.count("=") == len(solucion):
            a = max
            end = time.perf_counter()
            ganador = 1
    if ganador == 0 and a == max-1:
        print("Perdiste, se te acabaron los intentos. La palabra era ", pala)
        print("Los mejores intentos fueron: ")
        print(conexion.execute("SELECT Usuario, Numero de intentos, Tiempo FROM Clasificaciones WHERE Palabra = '{pala}' ORDER BY Numero de intentos, Tiempo GROUP BY Usuario LIMIT 5;"))
        print("Los mejores tiempos fueron: ")
        print(conexion.execute("SELECT Usuario, Numero de intentos, Tiempo FROM Clasificaciones WHERE Palabra = '{pala}' ORDER BY Tiempo, Numero de intentos GROUP BY Usuario LIMIT 5;"))
    if ganador == 1:
        print("Felicidades, ganaste!")
        usuario = str(input("Ingresa tu usuario: "))
        conexion.execute("INSERT INTO Clasificacion (Usuario, Numero de intentos, Tiempo, Palabra) \ VALUES('{usuario}', {intentos}, {end}, '{pala}');")
        conexion.commit()
        print("Los mejores intentos fueron: ")
        print(conexion.execute("SELECT Usuario, Numero de intentos, Tiempo FROM Clasificaciones WHERE Palabra = '{pala}' ORDER BY Numero de intentos, Tiempo GROUP BY Usuario LIMIT 5;"))
        print("Los mejores tiempos fueron: ")
        print(conexion.execute("SELECT Usuario, Numero de intentos, Tiempo FROM Clasificaciones WHERE Palabra = '{pala}' ORDER BY Tiempo, Numero de intentos GROUP BY Usuario LIMIT 5;"))
    intentos += 1
    a += 1

tiempo = end - start
print("Tardaste ", tiempo, " segundos.")

def verificar():
    b = 0
    for i in palabra:
        if list(intento)[b] == pala[b]:
            solucion[b] = "="
        elif list(intento)[b] in palabra:
            solucion[b] = "-"
        b += 1
# reloj
from threading import Timer

class Tick_timer():
    def __init__(self, inte, fnc, arg = ()):     
        self.intervalo = inte
        self.argumentos = arg
        self.funcion = fnc
        self.contando = 1
    
    def timeout(self):
        self.contando = 0
        self.funcion(*self.argumentos)
        self.timer = Timer(self.intervalo, self.timeout)
        self.timer.daemon = True
        self.timer.start()
        self.contando = 1
        
    def start(self):
        self.timeout()
        
    def stop(self):
        if self.contando == 1:
            self.timer.cancel()
            self.contando = 1
            
def perder():
    print(f"Se acabo el tiempo")
    a = max
    
c = Tick_timer(300.0, perder)
c.start()

while True:
    pass
