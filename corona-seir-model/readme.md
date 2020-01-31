# Wuhan Outbound Flights Analysis
### Analyzing outbound flights from Wuhan Tianhe airport WUH ZHHH of a single day

### Data
- Each record is a receiver message json row
- Data contains only messages received on 2 Jan 2020

### Exploratory analysis
*flights outbound of Wuhan*
- Top flight counts to destination countries
- Top flight counts to domestic destinations (in China)
- Number of flights to SG
- Operator and model of flights to SG
- Estimated number of passengers from Wuhan arrived to SG between 2 Jan to 23 Jan 2020

*flights inbound to Singapore from domestic chinese cities*
- Top chinese cities to SG with most number of flights
- Top operating airline to SG
- Top model of airplanes to SG
- Estimated number of total imported infection excluding cancelled flights on any single day

### Simulation Model
The model employed is a SEIR epidemic model without vitals where S stands for susceptible, E for exposed, I for infected and R for recovered

#### Model conclusions
By 13 March, if the spread of virus is not controlled, the model suggests a total of almost 1 million patients infected with Wuhan virus in SG.

Limitations: 
The SEIR model excludes possible imported infections from flights that were in operation before the lockdown of Wuhan Tianhe airport and the official cancellation of airline TR121 by Scoot on 23 Jan 2020. Hence, the initial infected population, I0, could be underestimated.

The model also misses out on possible imported infections from flights that are not in the list of domestic airport locations (as shown earlier) with flights from Wuhan aiport. No official ceasation of flights has been announced by the airlines companies running them till date yet.

The deterministic SEIR model assumes a constant rate of spread, beta, of the virus which can take on different values when depending on the density of population.
