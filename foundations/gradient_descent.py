class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations<1:
            return round(init, 5)
        for i in range(iterations):
            f_x = 2 * init
            init -=  (learning_rate * f_x)
        return round(init, 5)
