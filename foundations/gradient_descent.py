class Solution:
    # derviate of error function
    def df(self, x):
        return 2 * x
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Gradient descent alogorithm
        for i in range(iterations):
            der = self.df(init)
            init = init - learning_rate * der
        return round(init, 5)