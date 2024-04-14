#А және В екі бүтін сандар берілген.
# А<B болса, өсу ретімен немесе басқаша жағдайда кему ретімен А-дан В-ға дейінгі барлық сандарды басып шығарыңыз.

A = int(input("A: "))
B = int(input("B: "))
if A < B:# шарт тексеру
    #өсу ретімен лист шығару
    numbers_list = list(range(A, B+1))
    print( A, "дан", B, "ға дейінгі сандар өсу ретімен:")
    print(numbers_list)
elif A > B:
    #кему ретімен длист шығару
    numbers_list = list(range(A, B-1, -1))
    print( A, "дан", B, "ға дейінгі сандар кему ретімен:")
    print(numbers_list)
else:
    # тең болған жағдайда сол санды қайтарады
    numbers_list = list(range(A, B + 1))  # range() қолданып лист жасау
    print(A, "дан", B, "ға дейінгі сандар:")
    print(numbers_list)
