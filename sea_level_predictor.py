import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)   
     # Create first line of best fit
    (slope, intercept, rvalue, pvalue, stderr) = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sealevel_pred = intercept + slope * range(1880, 2051, 1)
    plt.plot(range(1880, 2051, 1), sealevel_pred, color = "green")
    # Create second line of best fit
    (slope, intercept, rvalue, pvalue, stderr) = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    sealevel_pred = intercept + slope * range(2000, 2051, 1)
    plt.plot(range(2000, 2051, 1), sealevel_pred, color = "red")
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
