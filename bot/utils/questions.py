import random

def generate_task():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    answer = a + b
    return f"{a} + {b} = ?", str(answer)
