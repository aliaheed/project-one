Wildfires Project

Team Members: Shannon Agresto, Ali Aheed Quadri, Michael Levandoski, Victor Yamaykin	

Description: Wildfires have been in the news several times a year. We will look at data from 1992 to 2015 to answer the following questions. 

Research Questions: Where and when do most wildfires occur?  Has there been a significant increase in wildfires in recent years? Is that an indication of climate change?
 
We’ll take a look at the following datasets:

Using wildfire data from Kaggle, we’ll summarize the top causes of wildfires, the number of wildfires by month and year. 
What longitude/latitude has had the most wildfires? What time of year? By state? By size of wildfire?
We’ll check into Reddit for posts about wildfires 
 
Steps to data processing with python, pandas, gmaps, etc: 
1. 	Convert sqlite to usable dataframe (Pandas DF)
a. 	Filter by lat/lng – choose a simple random sample?
2. 	Use plotly to generate maps 
a. 	Collect weather data and map of US
3. 	Stretch bonus goal --- check Reddit API for posts
a. 	Check if there are trending topics about wildfires

Data visualizations with python and matplotlib:  
1. 	Pie chart (1):
a. 	Top 10 common causes of wildfires
2. 	Bar chart of top 10 states (1)
3. 	Line graph: (1)
a. 	Number of wildfires across 1992 to 2015  
4. 	Scatter plots: (2) for 10 states
a. 	Number of wildfires by latitude and longitude
B.	Number of wildfires by max temp and average rainfall. 
5. 	maps: (1) -- (use plotly API and command line to make gif of maps):
a. 	the number of wildfires for each state over each year 
