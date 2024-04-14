#Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз.
A = int(input("A: "))
B = int(input("B: "))
if A <= B:

    numbers_list = list(range(A, B + 1))#range() қолданып лист жасау
    print( A, "дан", B, "ға дейінгі сандар:")
    print(numbers_list)
else:
    print("Қате енгізілу.Шарт орындалмады.")
