import matplotlib.pyplot as plt
import numpy as np

#Wzięte z mojego Lab4, lekko zmienione by pasowało do moich potrzeb.
def najm (l):
    """
    Funkcja zwracająca największą wartość z wszystkich argumentów pozycyjnych. Najpierw sprawdza raz, czy pierwszy arguent jest liczbą, później
    :return x:
    """
    y=0
    x=0
    for a in range(len(l)):
        if y>=0:
            y=y+1
            if isinstance(l[0], (int, float)):
                x = float(l[0])
            else:
                print('Proszę podawać tylko liczby :(')
                break
        if isinstance(l[a], (int,float)):
            if float(l[a])<x:
                x=float(l[a])
        else:
            print('Proszę podawać tylko liczby :(')
            break
    return x
V=0
a=0
b=0.0001

#Słownik przyspieszeń grawitacyjnych wybranych ciał niebieskich
g={"Me":3.7,"W":8.87,"Z":9.807,"Ma":3.7,"K":1.622}

#Pobieranie danych od użytkownika, wybór prędkości początkowej, kąt rzutu, uwzględnienie oporu ośrodka
#wraz z wyborem jego wartości
#
#Naprawione błędy:
#-błąd gdy która kolwiek wartość jest ujemna (błąd występowałby przy liczeniu funckji)
#-błąd gdy która kolwiek wartość nie jest liczbą
#-błąd gdu podczas pierwszej próby pobrania danych uwzględniono opór ośrodka; wpisano nie poprawną wartość,
#a następnie przy następnej próbie wybrano opcję bez uwzględniania oporu środka
while V<=0 or a<=0 or b<=0:
    while True:
        try:
            V = float(input("Podaj wartość prędkości początkowej:\n"))
            a = float(input("Podaj kąt w stopniach:\n"))
            b = 0.0001
            p1 = input("Czy uwzględnić opór ośroldka? y/n:\n")
            if p1 == "y":
                b = float(input("Podaj wartość współczynnika oporu środka: \n"))
        except ValueError:
            print("Podana wartość nie jest liczbą.\t")
        else:
            break
    if V<=0 or a<=0 or b<=0:
            print('Wszystkie wartości muszą być dodatnie')

#Konwertowanie zmiennych wybranych przez użytkownika na zmienne potrzebne do obliczania funkcji
a=np.deg2rad(a)
Vx=V*np.cos(a)
Vy=V*np.sin(a)

#Wybór przez użytkownika na jakich ciałach niebieskich ma odbywać się rzut ukośny (przez wybór przyspieszeń)
#
#Naprawione błędy:
#-błąd w którym użytkownik wpisywał niepoprawne dane (dane spoza wyboru)
#-błąd w którym użytkownik powtarzał wybrane opcje
while True:
    W = []
    P = input("Na jakich ciałach niebieskich ma występować rzut? \nMerkury: Me \nWenus: W \nZiemia: Z \n\
Księżyc: K \nMars: Ma \nWybory oddzielaj spacjami ")
    P=P.split()
    for element in P:
        if element=='Me':
            W.append(g.get("Me"))
        elif element=='W':
            W.append(g.get("W"))
        elif element=='Z':
            W.append(g.get("Z"))
        elif element=='K':
            W.append(g.get("K"))
        elif element=='Ma':
            W.append(g.get("Ma"))
        else:
            W = []
            print("Wpisuj tylko skróty zachowując wielkość liter")
            break
        if P.count(element)!=1:
            W = []
            print("Nie powtarzaj wpisywancyh skrótów")
            break
    if len(W)==len(P):
        break

#Znajdywanie najmniejszego przyspieszenia z tych które wybrał użytkownik. Potrzebne do określenia
#wielkości wykresu (chcemy, największy wykres się zmieścił)
G=najm(W)
t=np.linspace(0,(np.log(((Vy*b+G)/G)**2)/b), 1000)

x=(Vx/b)*(1-np.exp(-b*t))
print(x.shape)
y=((Vy/b)+(9.807/(b**2)))*(1-(np.exp((-b)*t)))-((9.807*t)/b)
plt.plot(x,y,color='g',lw = 1, ls='-.',label='sin(x)')
plt.show()
