import pandas as pd
from services.utility import Utility


elements = ["a", 1, 4, 5, "1", 7, 8, 4, 3, 0, "texto", None]

print([i for i in elements if i or i == 0])

elements = list(filter(lambda x: x or x == 0, elements))
print(elements)

print(Utility.is_numeric(0))

number_elements = list(filter(Utility.is_numeric, elements))
number_elements.sort()
print(number_elements)

sr = pd.Series(elements)
mode0 = int(sr.mode()[0])

print(isinstance(mode0, int))
