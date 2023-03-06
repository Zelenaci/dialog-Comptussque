import numpy as np

x = np.linspace(0, 100, 100)

with open("data.txt", "a") as file:
    for i in x:
        file.write(f"{i} {(2*np.pi*np.radians(i))**np.e}\n")
