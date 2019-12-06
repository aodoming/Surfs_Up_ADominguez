# Surfs_Up_ADominguez
### Investing in a "Surf n Shake" shop, by first running analytics on a weather data set of location.

##### Compare your findings between the month of June and December -seasonal data.
 
 ##### June Precipitation 
     count	1574.000000          
     mean	0.136360	             
     std	0.335731	               
     min	0.000000	              
     25%	0.000000	               
     50%	0.020000	               
     75%	0.120000             
     max	4.430000   
     
##### June Precipitation 	  tobs
count	1574.000000	       1700.000000
mean	  0.136360	         74.944118
std   	0.335731	         3.257417
min	   0.000000	         64.000000
25%	   0.000000	         73.000000
50%	   0.020000	         75.000000
75%	   0.120000    	     77.000000
max	   4.430000    	     85.000000
     
 ##### December Precipitation
    count	1405.000000
    mean	0.216819
    std	0.541399
    min	0.000000
    25%	0.000000
    50%	0.030000
    75%	0.150000
    max	6.420000



 ##### December Precipitation  tobs
count	 1405.000000	       1517.000000
mean	   0.216819	         71.041529
std	    0.541399	         3.745920
min    	0.000000	         56.000000
25%	    0.000000	         69.000000
50%	    0.030000	         71.000000
75%	    0.150000	         74.000000
max	    6.420000	         83.000000

June statistics for all stations, for all years had more precipitation amount than its equivalent in December.
But the mean, std, and max values were lower in June for all stations, for all years than in December's eqivalent in spite of the precipitation count for June.

For all the percentiles, but for the 25% values  which is zero for both months for all stations for all years, the 50%however, were high for June than in Dec.
Both months had no min values.


### Receommendations for further analysis
1) Calculate daily normals, ie. the average daily maximum (tmax) and minimum (tmin) temperatures for specific month & day.
2) Calculate rainfall per weather station for specific dates using the previous year's matching dates.
   And list the station, name, latitude, longitude, and elevation; sort desc order by precipitation amount. 
3) Do a temperature analysis by creating a function that will accept a start and end dates in the 
   format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.
