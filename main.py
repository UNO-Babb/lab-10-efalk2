#MapPlot.py
#Name: Ella Falk
#Date: 4/16/25
#Assignment: Lab 10

import matplotlib.pyplot as plt
import numpy as np

import construction_spending
spending = construction_spending.get_spending()

numItems = len(spending)

for spot in range(numItems):
    year = spending[spot]["time"]["year"]
    commercial = spending[spot]["annual"]["combined"]["commercial"]
    educational = spending[spot]["annual"]["combined"]["educational"]
    healthcare = spending[spot]["annual"]["combined"]["health care"]
    power = spending[spot]["annual"]["combined"]["power"]
    manufacturing = spending[spot]["annual"]["combined"]["manufacturing"]

    

fig, ax = plt.subplots()

# Example data
industries = ('Commercial', 'Educational', 'Healthcare', 'Power', 'Manufacturing')
y_pos = np.arange(len(industries))
spent = (commercial, educational, healthcare, power, manufacturing)
error = np.random.rand(len(industries))

ax.barh(y_pos, spent, xerr=error, align='center')
ax.set_yticks(y_pos, labels=industries)
ax.set_xticks(spent)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Amount Spent')
ax.set_title('Public and Private Combined Annual Construction Spending')

plt.savefig("output")
