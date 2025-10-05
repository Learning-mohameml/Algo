"""
There are light bulbs in a room, each initially off and with its switch by its side. 
The first person enters and flips every switch. 
The second person enters and flips every other switch. 
The third person enters and flips every third switch. 
This process continues until the 100-th person flips every 100-th switch, or the last switch.

How many lights are on?

"""





def run_algo(lights : list[int] , n : int, verbose : bool = False  ) -> list[int] :


    for number in range(1 , n + 1 , 1):

        for index , ele in enumerate(lights) :

            if (index + 1) % number == 0 : 
                lights[index] = "on" if ele == "off" else "off"
        if verbose : 
            print(f"{number}-th person ,  lights : {lights}")
            print(f"the number of light on is : {compute_lights_on(lights)}")


    return lights


def compute_lights_on(lights : list[int]) -> int : 
    n = 0 

    for light in lights :
        if light == "on":
            n += 1 
    return n 


if __name__ == "__main__":

    lights = run_algo(["off"]*100 , 100 , verbose=True)
    print(f"the number of light on is : {compute_lights_on(lights)}")


