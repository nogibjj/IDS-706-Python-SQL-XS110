
# World Population


## Data

The data is from kaggle [world population](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset). In this Dataset, we have Historical Population data for every Country/Territory in the world by different parameters like Area Size of the Country/Territory, Name of the Continent, Name of the Capital, Density, Population Growth Rate, Ranking based on Population, World Population Percentage, etc.

I downloaded `word_population.csv` from kaggle and uploaded it into this resporitory.

## Setup

I used week2 mini project as a template and made the following modifications: 

### 1. Update requirements.txt:
```
#script
polars
pyarrow
tabulate
```
### 2. Read data

Instead of using pd.read_csv, I use `pl.read_csv` to read `world_population.csv`


### 3. Update script.py

I updated the script.py using Polars for descriptive statistics to generate summary statistics (mean, median, standard deviation)

And I also created data visualization.

### 4. Generate report.md

Run ` make all` in terminal, I generated `report.md` automatically.

![Alt text](/image/image6.png)
## Data Visualization

I analysed the 234 countries' population in 2022, growth rate and Area(km²).

### 1. Summary statistics using the describe method

![Alt text](/image/image1.png)

### 2. Mean, Median and Mode

![Alt text](/image/image2.png)

### 3. Variance and standard deviation

![Alt text](/image/image3.png)

### 4. histogram of 2022 population

![Alt text](/image/population_histogram.png)

### 5. boxplot of 2022 population

![Alt text](/image/population_boxplot.png)