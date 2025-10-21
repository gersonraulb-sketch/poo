class Mat:
    @staticmethod
    def sumar(a, b): return a+b

    @staticmethod
    def factorial(n):
        r = 1
        for i in range(2, n+1):
            r *= i
        return r
