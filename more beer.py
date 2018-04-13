#Learning thanks to Samuel lachance (kaggle.com)


import numpy as np
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

beer_recipe = pd.read_csv('recipeData.csv', index_col='BeerID', encoding='latin1')
beer_recipe.head()

ax = sns.countplot(x='BrewMethod', data=beer_recipe)
ax.set(title='Frequency table of possible values in BrewMethod')
sns.despine(left=True, bottom=True)


print('BrewMethod has {} null values'.format(beer_recipe.BrewMethod.isnull().sum()))
plt.show()
