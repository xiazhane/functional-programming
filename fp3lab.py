def reverse_string(input_str):
    # Бірлескен жағдай: стрингді төменгі жазбалардан келесіге дейін аудару
    if len(input_str) <= 1:
        return input_str
    else:
        # Рекурсивті вызов: алдыңғы стрингді аудару және соңынан қатар тауып алу
        return reverse_string(input_str[1:]) + input_str[0]
# Пайдаланушыдан стрингді енгізу
user_input = input("Стрингді енгізіңіз: ")
# Стрингді аудару жасау
result = reverse_string(user_input)
# Нәтижені шығару
print("Аударылған стринг:", result)
