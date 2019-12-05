# Surfs_Up_ADominguez
### Investing in a "Surf n Shake" shop, by first running analytics on a weather data set of location.


##### Compare your findings between the month of June and December -seasonal data.
 
 ##### June Precipitation 
     count	173.000000          
     mean	0.212312	             
     std	0.327195	               
     min	0.000000	              
     25%	0.010000	               
     50%	0.060000	               
     75%	0.280000             
     max	1.700000          

 ##### December Precipitation
    count	163.000000
    mean	0.401656
    std	1.164754
    min	0.000000
    25%	0.000000
    50%	0.050000
    75%	0.245000
    max	9.640000


June had more precipitation amount than December. But the mean, std, and max values were lower in June than in Dec in spite of the count.
All the percentile values however, were high for June than in Dec.
Both months had no min values.


### Receommendations for further analysis
1) Calculate daily normals, ie. the average daily maximum (tmax) and minimum (tmin) temperatures for specific month & day.
2) Calculate rainfall per weather station for specific dates using the previous year's matching dates.
   And list the station, name, latitude, longitude, and elevation; sort desc order by precipitation amount. 
3) Do a temperature analysis by creating a function that will accept a start and end dates in the 
   format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.
