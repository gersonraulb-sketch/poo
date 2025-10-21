import time


def crono(func):
    def w(*a, **k):
        t = time.time()
        r = func(*a, **k)
        print(f"{func.__name__} {time.time()-t:.4f}s")
        return r
    return w
