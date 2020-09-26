# Restaurant Ranking from TripAdvisor.

## Goal: to calculate MAE in RandomForestRegressor model of restaurant rating data with adding different parameters that can affect on rating.

#### Data contains 2  main work files: 
- main_task - train dataset, 
- kaggle_task - test dataset. 

#### And additional datasets as:
- Big Mac Index dataset: big_mac_full_index, BM - 2 csv files
- Cost_of_living_index

## Conclusions:
- All empty values were filled in, the data became complete.
- In dataframe were added these new parameteres:
rest_name, country, capital, sentiment, cuisine_qty, big_mac_price, days_past, living_cost_index, rent_index, rest_price_index, local_purchase_index.
- Added dummy variables cuisine, cities, countries for better MAE.
