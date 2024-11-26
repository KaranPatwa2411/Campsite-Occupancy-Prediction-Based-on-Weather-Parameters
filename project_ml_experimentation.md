#### SER594: Experimentation  
#### Campsite Occupancy Prediction Based on Weather Parameters  
#### Karan Jignesh Patwa  
#### November 25, 2024

## Explainable Records  

### Record 1  
**Raw Data:**  
`3427, Sachsen-Anhalt, 2002-12-01, 376.0, -83.54485776805251, 1798.0, -72.56218525866015, 4.8, 0.863167, -1.37759, -3.5917, 6.682613, 1.681159, 1.681159, 0.0, 61.87814, 105.0073, -0.802782, 44.64121, 0.4408858, 0.3825625, 0.4208314, 2.642109, 0.3276615, 0.3276615, 0.0, 21.9368, 0.709275, 0.191727, 4.820003, 63.0, 21.0, 21.0, 4814.0, 21.0, -7.5, 47.9`  

**Prediction Explanation:**  
The model predicted 354.28 while the actual value was 376.00. Given that the data falls in winter in Sachsen-Anhalt, this could be a reasonable prediction as it is expected that fewer people would go camping at this time due to low temperatures. However, slight underprediction may be due to the extreme negative temperatures and high wind speeds during this period. 

### Record 2  
**Raw Data:**  
`2904, Bremen, 2007-04-01, 3260.557471264368, 0.0, 7015.16091954023, 0.0, 2.333720930232558, 17.9386, 11.96518, 5.281012, 0.0, 84.91645, 44.10886, 0.0, 2.753164, 74.06962, 13.42088, 246.5063, 0.1059762, 0.113866, 0.0908134, 0.0, 0.3675717, 0.1964494, 0.0, 0.473162, 0.254505, 0.0478047, 0.499959, 1.0, 2.074074074074074, 2.074074074074074, 413.7709497206704, 2.074074074074074, 5.05, 0.005012614045220539`  

**Prediction Explanation:**  
The model predicted the value 3260.56, which was the actual value. This sounds right with domain knowledge because, in Bremen, April is typically the beginning of spring, a period when camping site occupancy begins to rise significantly. The mild temperatures and absence of extreme weather conditions are reasons that align well with the model's output.

---

## Interesting Features  

### Feature A:  
**Feature:** Mean Air Temperature (mean_air_temp_mean)  

**Justification:** Temperature is one of the most important predictors of campsite use. Generally, with higher temperatures comes higher use of campsites, while very cold temperatures tend to keep them away. Mean air temperature directly correlates with human comfort during outdoor activities. 

### Feature B:  
**Feature:** Sunshine Duration (mean_sunshine_duration)  

**Justification:** Duration of sunshine is a very strong indicator of good weather, and good weather encourages outdoor camping activities. Extended hours of sunshine promotes visibility and comfort, which is crucial for the consideration of campsite arrival predictions. 

---

## Experiments  

### Varying A (Temperature)  
**Prediction Trend Seen:** As mean air temperature increases, campsite utilization increases linearly with more rapid growth in spring and summer. Very low temperatures show steep declines, which proves a good case for causality.  

### Varying B (Precipitation)  
**Prediction Trend Seen:** Improvement of sunshine duration comes with higher campsite arrivals; however, this effect diminishes when other weather conditions are unfavorable, hence showing that this is its secondary but complementary role.  

### Varying A and B Together  
**Prediction Trend Seen:** If both features rise, campsite utilisation increases exponentially. Favorable temperatures blended with lengthy sunshine hours create optimal conditions for camping.

### Varying A and B Inversely  
**Prediction Trend Seen:** Mixed trends are seen when either temperature rises while sunshine duration decreases, or vice versa. For example, campers will still come for warm yet cloudy conditions, but cold and sunny usually see lower utilization.
