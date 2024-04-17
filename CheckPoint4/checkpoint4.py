# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
# list
plantas_medicinales=["milenrama","angelica","bardana","vulneraria"]
print(plantas_medicinales)

#tuple
plantas_ornamentales=('petunia', 'camelia', 'verbena','azalea')
print (plantas_ornamentales)

#float
sale_price=12.99
print(sale_price)

#integer
id_planta=120
print(id_planta)

#decimal
from decimal import Decimal
comision=Decimal('0.15')
print(comision)

#dictionary
familia = {
    'milenrama': 'asteraceae',
    'angelica' : 'umbelliferae',
    'bardana' : 'compositae',
    'vulneraria': 'leguminosae'
}
print(familia)

#Exercise 2: Round your float up.
import math
print(math.ceil(sale_price))

#Exercise 3: Get the square root of your float.
print(math.sqrt(sale_price))

#Exercise 4: Select the first element from your dictionary.
print(list(familia)[0])

#Exercise 5: Select the second element from your tuple.
print(plantas_ornamentales[1])

#Exercise 6: Add an element to the end of your list.
plantas_medicinales.extend(['cardo'])
print(plantas_medicinales)

#Exercise 7: Replace the first element in your list.
plantas_medicinales[0]='zanahoria'
print(plantas_medicinales)

#Exercise 8: Sort your list alphabetically.
plantas_medicinales.sort()
print(plantas_medicinales)

#Exercise 9: Use reassignment to add an element to your tuple.
plantas_ornamentales += ('rosa',)
print(plantas_ornamentales)

