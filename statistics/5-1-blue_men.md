[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

*Exercise 1   In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.*

*In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com).* 

*What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.*

### A. Communicate the problem: 

This problem asks us to extrapolate from the BRFSS dataset to determine what percentage of the US male population fits the height criteria of the Blue Man Group.


### B. How you solved it: 

I solved this problem by assuming that heights are normally distributed and that BRFSS draws from that very same normal distribution and its summary statistics could be used to define the normal distribution's CDF.

### C. Solution 

Approximately 34% of the U.S. male population fall within the range required to perform within Blue Man Group.

<hr>

### D. The Details:


##### Step 1: Import the required datasets.
```
import scipy.stats

```

##### Step 2: Convert the Blue Man Group height criteria from inches to centimeters.

```
BMG_upper_limit = ((6 * 12) + 1) * 2.54
# This comes out to 185.42 cm

BMG_lower_limit = ((5 * 12) + 10) * 2.54
# This comes out to 177.8 cm
```

##### Step 3: Set up parameters for the normal distribution.

```
mu = 178
sigma = 7.7

```

##### Step 4: Get the CDF at 6'1" and 5'10".

```
upper_height_percentile = scipy.stats.norm.cdf(BMG_upper_limit, loc=mu, scale=sigma)

# This is equal to 0.83238586549630722. This means, the probability that a male is 6'1" or less is ~83%.

lower_height_percentile = scipy.stats.norm.cdf(BMG_lower_limit, loc=mu, scale=sigma)

# This is equal to 0.489639027865. This means, the probability that a male is 5'10" or less is ~49%.
```
##### Step 5: Find the percentage of males that are between 5'10" and 6'1".

```
upper_height_percentile - lower_height_percentile

# This is 0.34274683763147457 or roughly 34%
```
