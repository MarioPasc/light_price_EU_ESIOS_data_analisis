# Project: Electricity Spot Price Data Analysis

## Overview of the project 

In this project, I have collected information using the ESIOS API, performed data cleaning, processing, and visualization for the electricity spot price (SPOT) data in several European countries for the month of July. The countries analyzed include Reino Unido, Italia, Alemania, Francia, Paises Bajos, Portugal, Belgica, and España.

## Libraries Used

- json: Used to handle JSON data from the ESIOS API response.
- pandas (imported as pd): Utilized for data manipulation and analysis, including creating dataframes.
- os: Employed to handle file and directory operations, as well as reading files.
- numpy (imported as np): Utilized for mathematical and numerical operations on the data.
- matplotlib.pyplot (imported as plt): Used for data visualization, creating line plots and scatter plots.
- urllib.request (imported as urlreq): Used to fetch data from the ESIOS API using HTTP requests.
- datetime: Used to work with dates and times, especially in calculating the timeframe for the month of July.

## Data Collection

I used the ESIOS API along with urllib.request to fetch electricity spot price data for the specified countries during the month of July. The API provides real-time and historical data, which was essential for this analysis.

## Data Cleaning

Before starting the analysis, I performed data cleaning to handle missing or incorrect values, remove duplicates, and ensure the data was in a suitable format for further processing.

## Data Processing

After cleaning the data, I processed it using pandas and numpy to calculate relevant metrics, such as average spot price for each day in the month of July for the specified countries. I also performed any necessary data transformations to make the data ready for visualization.

## Data Visualization

Using matplotlib.pyplot, I created visualizations to present the average spot price trends for each country throughout the month of July. The visualizations include line plots and scatter plots, which provide insights into the fluctuation of electricity spot prices in the selected European countries.

## Conclusion

The analysis and visualizations revealed valuable insights into the electricity spot price trends in Reino Unido, Italia, Alemania, Francia, Paises Bajos, Portugal, Belgica, and España during the month of July. The project showcases the power of data analysis and visualization in understanding complex energy market dynamics.

### Plots

![Precio Luz Alemania](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Alemania.png)
![Precio Luz Bélgica](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-B%C3%A9lgica.png)
![Precio Luz España](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Espa%C3%B1a.png)
![Precio Luz Francia](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Francia.png)
![Precio Luz Italia](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Italia.png)
![Precio Luz Paises Bajos](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Pa%C3%ADses%20Bajos.png)
![Precio Luz Portugal](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Portugal.png)
![Precio Luz Reino Unido](https://github.com/Mawio02/light_price_EU_ESIOS_data_analisis/blob/main/precioluz-Reino%20Unido.png)


# What i've learned

## Overview

This project is a small learning exercise that I have undertaken to gain hands-on experience in handling various Python libraries for data analysis. Specifically, I have used json, pandas, os, numpy, matplotlib.pyplot, urllib.request, and datetime libraries to work with electricity spot price (SPOT) data for several European countries during the month of July. The countries analyzed include Reino Unido, Italia, Alemania, Francia, Paises Bajos, Portugal, Belgica, and España.

## Learning Goals

The primary objective of this project was to learn and practice the following skills:

1. Data Collection: Utilizing APIs (ESIOS API) to fetch real-time and historical data efficiently using urllib.request.

2. Data Cleaning: Implementing data cleaning techniques to handle missing values, duplicates, and data formatting issues.

3. Data Processing: Using pandas and numpy to process the data, calculate relevant metrics, and perform necessary data transformations.

4. Data Visualization: Employing matplotlib.pyplot to create visually appealing line plots and scatter plots for data representation.

5. Library Integration: Understanding how to integrate multiple libraries effectively to perform various tasks in the data analysis pipeline.

## Methodology

Throughout the project, I followed a step-by-step approach, starting from data collection using the ESIOS API and urllib.request, followed by data cleaning to ensure data quality. Next, I processed the data using pandas and numpy to calculate average spot prices for each day in July for the selected European countries. Finally, I visualized the results using matplotlib.pyplot to create insightful line plots and scatter plots.

## Conclusion

This learning project has provided me with valuable experience in handling real-world data and utilizing essential Python libraries for data analysis and visualization. By exploring electricity spot price data for multiple countries, I have gained insights into energy market trends and the importance of data analysis in decision-making.

## Future Learning

I plan to continue learning and exploring more advanced data analysis techniques, predictive modeling, and machine learning to further enhance my skills. Additionally, I aim to undertake more complex projects to solidify my understanding of data science concepts and best practices.
