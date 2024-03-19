def suma_do_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = 10
wynik = suma_do_n(n)
print("Suma liczb od 1 do", n, "to:", wynik)
