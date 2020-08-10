# Avocado-Classifier ![alt text](https://github.com/shannonjin/Avocado-Classifier/blob/master/Screen%20Shot%202020-08-10%20at%2012.50.04%20AM.png)

Avocadoes are a delicious but sometimes pricer grocery item! It's important to get the best bang for your buck! I've developed a centroid classifier algorithim for avocado prices.
Given the price of an avocado, my python script will guess the region in which the avocado is being retailed in. Find out if the avocado you're about to buy is being
priced fairly for your geographic area!

The dataset used for this project was downloaded from the Hass Avocado Board's website, and contains avocado prices from 2015-2018 from across the nation. Thank you to Justin Kiggins for making this dataset available on [kaggle](https://www.kaggle.com/neuromusic/avocado-prices)

## Components

1. Cleaning the data. While the Hass Avocado board's dataset contains sales info as well, we're only interested in the regions and the price of avocadoes
2. Compute centroid of avocado prices for each region
3. Train on the data and test on the data (split the Hass Avocado dataset, here we prefer to split 90% for training 10% for test)
4. Build a learning curve
5. Perform cross validation

Example of output during running: ![alt text](https://github.com/shannonjin/Avocado-Classifier/blob/master/Screen%20Shot%202020-08-10%20at%201.02.09%20AM.png)


## To do's

