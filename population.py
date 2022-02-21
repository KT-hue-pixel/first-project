import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


population_df = pd.read_csv('C:\\Users\\Reggie\\Desktop\\vs code test project\\World Population.csv')
print(population_df)
# check the datatype
print(population_df.dtypes)
# drop data types not use
population_df.drop(population_df.columns[[0,4,5]],
                   axis=1, inplace= True)
print(population_df.columns)
# change the data types
population_df["Country"].astype('string')
population_df["Region"].astype('string')
print(population_df)
# merge a new dataset
urban_population_df = pd.read_csv('C:\\Users\\Reggie\\Desktop\\vs code test project\\WorldPopulationurban.csv')
print(urban_population_df)
print(urban_population_df.columns)
year = urban_population_df['Year']
world_population = urban_population_df['Population']
urban = urban_population_df['Urban']
urban_percent = urban_population_df['UrbanPerc']
population_df['Year'] = year
population_df['World Population'] = world_population
population_df['Urban'] = urban
population_df['Urban percentage'] = urban_percent
Pop_df = population_df.merge(year, on='Year')
print(Pop_df.head(10))
print(Pop_df.shape)
print(Pop_df.info())
print(Pop_df.describe())
print(Pop_df.columns)
print(Pop_df.columns[Pop_df.isna().any()])
# add new column
Pop_df['Country urban%'] = (Pop_df['Population'] /
                            Pop_df['World Population'][0]) * Pop_df['Urban percentage'][0]
Pop_df['Country Urban Population'] = Pop_df['Country urban%'] \
                                     * Pop_df['Population']
a = (Pop_df['World Population'][0]) - (Pop_df['Urban'][0])
b = Pop_df['Urban'][0]
c = Pop_df['Urban percentage'][0]
d = (a/b)*c
Pop_df['Country Rural% '] = (Pop_df['Population'] /
                             Pop_df['World Population'][0]) * d
Pop_df['Country Rural Population'] = Pop_df['Population'] * \
                                     Pop_df['Country Rural% ']
# analysis
total_population = Pop_df['Population'].sum()
print('the total population is', total_population)
rural_population_of_the_world = ((Pop_df['World Population'][0]) -
                                 (Pop_df['Urban'][0]))
print('the rural population for year 2020 is',
      rural_population_of_the_world)
population_per_region = Pop_df.groupby('Region')[['Population']].sum()
print('the population per regions ', population_per_region)
china_to_india= Pop_df['Population'][0]- Pop_df['Population'][1]
print('china has',china_to_india, 'people more than india')

print(Pop_df.dtypes)

# graphs
# line graph of the world population
sns.set_style('darkgrid')
plt.subplots(figsize=[10, 6])
plt.plot(Pop_df['Year'], Pop_df['World Population'], 'or')
plt.xlabel('Year')
plt.ylabel('World Population')
plt.title('World Population growth', fontsize=15)
plt.show()

# pie chart representing the  regions to their population
sns.set_style('whitegrid')
colors = sns.color_palette('bright')
plt.subplots(figsize=[10, 6])
labels = ["Africa", "Americas", "Asia", "Asia,Europe", "Europe",
          "Europe,Asia", "Oceania"]
data = Pop_df.groupby("Region")["Population"].sum()
plt.pie(data, colors=colors, labels=labels, autopct="%.1f%%",
        explode=[0.05]*7, pctdistance=0.5)
plt.title("Continental population", fontsize=15)
plt.show()

# bar chart
plt.subplots(figsize=[10, 6])
plt.title("Distribution of the population", fontsize=15)
plt.xlabel('Country')
plt.ylabel('Population')
plt.bar(Pop_df['Country'],Pop_df['Population'],color='red')
plt.bar(Pop_df['Country'],Pop_df['Country Urban Population'],color='blue')
plt.bar(Pop_df['Country'],Pop_df['Country Rural Population'],
        color='yellow')
plt.show()

# scatter plot of the urban to rural populace
plt.subplots(figsize=[10, 6])
plt.title("population relativity", fontsize=15)
sns.scatterplot(x=Pop_df['Country Rural Population'],
                y=Pop_df['Country Urban Population']
                ,hue=Pop_df['Population'],s=100)
plt.show()

print(Pop_df.dtypes)
# write tha data to a new csv file
Pop_df.to_csv('population.csv')

