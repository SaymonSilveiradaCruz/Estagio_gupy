
def fibonacci_sequence(max_value):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= max_value:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_fibonacci_number(number):
    sequence = fibonacci_sequence(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."
    
numero = 21

resultado = is_fibonacci_number(numero)
print(resultado)
