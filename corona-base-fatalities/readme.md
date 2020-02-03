# Base Fatalities Estimation

Using binomial distribution to estimate fatalities given # of cases.  

## Use-case

Two calculations are offered: 

### Base Fatalities

Given a base probability (e.g. JHU total), what is the likelihood that deaths are equal to or higher than the amount reported. 
![alt text](https://github.com/docligot/coronatracker-analytics/blob/master/corona-base-fatalities/base_fatalities.png "Base Fatalities")

### Likely Deaths

Given a base probability (e.g. JHU total), what is the likely number of deaths at various case level and probability. 
![alt text](https://github.com/docligot/coronatracker-analytics/blob/master/corona-base-fatalities/likely_deaths.png "Likely Deaths")


### Estimation

Given a base probability (e.g. JHU total), what case level justifies the current level of mortality in an area. 
![alt text](https://github.com/docligot/coronatracker-analytics/blob/master/corona-base-fatalities/illustration.png "Estimation")

* For example as of this writing, mainland China deaths are at 304 given 14k cases. There is also a death emergence in the Philippines with only 2 cases. Binomial test estimates the probability for these cases at 43% and 0.04% respectively. 

* Keeping base probability constant, it's possible to gross up case levels to justify the deaths at a higher probability. At 96%, cases in Mainland China are likely at 16,000 while Philippines should be 250 to justify deaths reported. 

## Calculation

Please find the spreadsheet [here](https://docs.google.com/spreadsheets/d/1LRuIBh5yRFRb8JiDAvMmY1Yuei_icbq2/edit#gid=95220160).

## Caveat

**Note: This calculation is speculative and should not be construed as official health advisory.**

## Contact Us

Message me on Linked-IN
* [Dominic Ligot](https://www.linkedin.com/in/docligot/)