
import random
import math

def f(x):
    return x * x

def simulated_annealing(x, T, alpha):
    current = x
    best = x

    while T > 0.1:
        next_x = current + random.choice([-1, 1])
        delta = f(next_x) - f(current)

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = next_x

        if f(current) < f(best):
            best = current

        T = T * alpha

    return best

# Main program
x = int(input("Enter initial value: "))
T = float(input("Enter initial temperature: "))
alpha = float(input("Enter cooling rate (0 to 1): "))

if T <= 0 or not (0 < alpha < 1):
    print("Invalid input")
else:
    best = simulated_annealing(x, T, alpha)
    print("Best solution:", best)
    print("Minimum value:", f(best))
