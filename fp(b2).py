#Екі бүтін А және В саны берілген, A>B. А-дан В-ға дейінгі барлық тақ сандарды кему ретімен басып шығарыңыз.
# Бұл тапсырмада if операторынсыз орындай аласыз.
A = int(input("A: "))
B = int(input("B: "))

A -= A % 2 == 0

for i in range(A, B-1, -2):
    print(i)

