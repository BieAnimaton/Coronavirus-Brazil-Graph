from matplotlib import pyplot as plt
from matplotlib.pyplot import figure as fg
fg(num=None, figsize=(10, 8))
import numpy as np
import pandas as pd

date_br = ()
cases_br = ()
dies = ()
max_view = 8000

data_br = pd.read_csv('data_brazil.csv')
date_br = data_br['date']
cases_br = data_br['cases']
dies_br = data_br['dies']

plt.plot(date_br, cases_br, 'b', label="")
plt.plot(date_br, cases_br, 'mo', label="Casos")
plt.plot(date_br, dies_br, 'b', label="")
plt.plot(date_br, dies_br, 'ro', label="Mortes")

plt.legend(prop={"size":15})
plt.xticks(rotation=45, fontsize=10)

ylabel = np.arange(0,max_view,500)
plt.yticks(ylabel)

ax = plt.gca()
ax.set_ylim([1,max_view])

plt.title("Avanço do Coronavirus no Brasil")
plt.grid(True)
#plt.show()
plt.savefig('coronavirus_brasil.jpg', dpi=500)
plt.savefig('coronavirus_brasil.pdf')