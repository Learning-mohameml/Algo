#!/usr/bin/env python3

"""
f_0 = f_1 = 1 

f_n = f_{n-1} + f_{n-2} for all n >= 2 

"""


# méthode naive 



def fibo(n) :
    if n == 0 or n ==  1 : 
        return 1 
    res = fibo(n - 1) + fibo(n - 2)
    return res 





# méthode Bottom-up 

def fibo_bottom_up(n):
    if n == 0 or n == 1 :
        return 1 
    fib = [1]*(n+ 1) 

    for i in range(2 , n + 1) : 
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]


def fibo_optim_bottom_up(n):
    if n == 0 or n == 1 :
        return 1 
    prev , curr = 1 , 1 

    for _ in range(2 , n + 1) : 
        temp = curr 
        curr = curr + prev 
        prev = temp 

    return curr 





# méthode Top-down 

def fibo_top_down(n : int) -> int : 

    cache : dict[int , int] = {
        0 : 1 , 
        1 : 1 
    }

    def _fibo(n : int) -> int : 
        if n in cache : 
            return cache[n]
        res = _fibo(n - 1) + _fibo(n - 2)
        cache[n] = res 

        return res 

    return _fibo(n)


if __name__ == "__main__":

    def run_tests():
        funcs = [
            fibo,
            fibo_bottom_up,
            fibo_optim_bottom_up,
            fibo_top_down,
        ]

        # Tests de base
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        for n, exp in enumerate(expected):
            for f in funcs:
                res = f(n)
                assert res == exp, f"{f.__name__}({n}) = {res}, expected {exp}"

        # Tests croisés (cohérence entre implémentations)
        for n in range(0, 15):
            values = [f(n) for f in funcs]
            assert all(v == values[0] for v in values), (
                f"Incohérence pour n={n}: {values}"
            )

        print("✅ Tous les tests Fibonacci ont réussi !")

    run_tests()
