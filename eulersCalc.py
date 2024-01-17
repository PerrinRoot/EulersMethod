import numpy as np
import matplotlib.pyplot as plt

def euler_method(func, y_initial, x_initial, x_final, h):
    x_values = np.arange(x_initial, x_final + h, h)
    y_values = [y_initial]

    for x in x_values[:-1]:
        y_initial = y_initial + h * func(x, y_initial)
        y_values.append(y_initial)

    return x_values, y_values

def process_math_functions(ode_str):
    math_functions = ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt']
    for func in math_functions:
        if func in ode_str:
            ode_str = ode_str.replace(func, f"np.{func}")

    return ode_str

def validate_input(x_initial, x_final, h):
    if h <= 0:
        raise ValueError("Invalid input: Step size (h) should be positive.")
    if x_initial >= x_final:
        raise ValueError("Invalid input: x final should be greater than x initial.")

def main():
    try:
        ode_str = input("Enter dy/dx (e.g. x + y): ")
        ode_str = process_math_functions(ode_str)
        ode_func = eval(f"lambda x, y: {ode_str}")  

        x_initial = float(input("Enter x initial: "))
        x_final = float(input("Enter x final: "))
        y_initial = float(input("Enter the initial value of y: "))
        h = float(input("Enter the step size: "))

        validate_input(x_initial, x_final, h)

        x_values, y_values = euler_method(ode_func, y_initial, x_initial, x_final, h)
        y_values = [y - y_values[0] for y in y_values]

  
        plt.plot(x_values, y_values, label='Numerical Solution')
        plt.title('Numerical Solution using Numerical Method')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError as ve:
        print(f"ValueError: {ve}")
        print("Check imput and try again")
    except Exception as e:
        print(f"Error: {e}")
        print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()
