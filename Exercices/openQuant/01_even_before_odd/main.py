"""
Open Quant : 
write a programme taht estimate the proba : 
P(X_1 even , X_2 even , X_3 even | B) B : the permutation of (1,2,3,4,5,6)
# math response : 1/20 
"""

import random 


def estimate_proba_even_beofre_odd(
    num_iter : int = 1_000_000
) -> float:

    roll_dice = lambda  : random.randint(1,6)

    valid_case = 0 

    for _ in range(num_iter):

        seen_faces = set()
        while True : 
            roll = roll_dice()
            seen_faces.add(roll)
            if roll % 2 == 1 and len(seen_faces) < 4 : 
                break

            if len(seen_faces) == 6 : 
                valid_case += 1 
                break 

    return valid_case / num_iter


print(f"estimate prob : {estimate_proba_even_beofre_odd()} , or exac_proba : {1/20}")

