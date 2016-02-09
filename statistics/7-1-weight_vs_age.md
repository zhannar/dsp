[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

*Exercise 1   Using data from the NSFG, make a scatter plot of birth weight versus mother’s age.* 

*Plot percentiles of birth weight versus mother’s age.*

*Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?*

### A. Communicate the problem: 

This problem asks us the relationship between a baby's birthweight and the mother's age. 


### B. How you solved it: 

I solved this problem by making a regular scatter and a percentile plot of the two variables. In addition, I calculated Pearson's and Spearman's correlations.

### C. Solution 

The scatterplot does not reveal any strong relationship between the mother's age and the baby's birthweight. The baby's weight seems to hover between 6 and 8.5 lbs regardless of the mother's age (more visible in the hexbin scatterplot), and shows relatively similar variance outside of that interval. The percentile plot shows the baby's weight increasing slightly as the mom goes from 20 to 30 years old. There is some leveling off and discrpency across the percentiles when the mom is 30-35 years old, but all seem to show a decrease in baby weight for every year after the mom is 35.

The Pearson's Correlation is around 0.069 and Spearmon's Correlation is around 0.095; two fairly small numbers.

<hr>

### D. The Details:


##### Step 1: Import the required datasets.
```
import nsfg
import pandas as pd
import numpy as np
import thinkplot
import thinkstats2
import math

```

##### Step 2: Extract out the relevant time series.



```
preg = nsfg.ReadFemPreg()
#Get rid of the NA's s.t. calculating the means, covariance, and correlations can be possible.
preg = preg.dropna(subset=['totalwgt_lb', 'agepreg'])


baby_weight = preg["totalwgt_lb"]
mom_age = preg["agepreg"]

```

##### Step 3: Make scatterplot of mother's age and baby's birthweight.

```
alpha = 0.2

# Regular Scatterplot
thinkplot.Scatter(mom_age, baby_weight, alpha = alpha)
thinkplot.Show(xlabel='Moms age (yrs)',
                   ylabel='Babys Weight (lbs)',
                    xlim=[10, 45],
                     ylim=[0, 16],)                   
```
![alt text](weights_ages.png =400x350)

```
# Hexbin Scatterplot
thinkplot.HexBin(mom_age, baby_weight)
thinkplot.Show(xlabel='Moms age (yrs)',
                   ylabel='Babys Weight (lbs)',
                    xlim=[10, 45],
                     ylim=[0, 16],)
                                        
# Zoomed in version
thinkplot.HexBin(mom_age, baby_weight, bins = 100)
thinkplot.Show(xlabel='Moms age (yrs)',
                   ylabel='Babys Weight (lbs)',
                    xlim=[15, 40],
                     ylim=[5, 10],
              )
              
```
![alt text](weights_ages_hexbin.png =400x350)

![alt text](weights_ages_hexbin_detail.png =400x350)

##### Step 4: Make percentile plot of mother's age and baby's birthweight.


```
bins = np.arange(10, 50, 5)
indices = np.digitize(preg.agepreg, bins)
groups = preg.groupby(indices)
    
for i, group in groups:
    print(i, len(group))
    
ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     legend=True)

for percent in [25, 50, 75]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%s' % (percent)
        thinkplot.Plot(ages, weights, label=label)
```
![alt text](weights_ages_percentile.png =400x350)

##### Step 5: Define Covariance

```

def Cov(xs, ys, meanx=None, meany=None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)

    cov = np.dot(xs-meanx, ys-meany) / len(xs)
    return cov
```



##### Step 6: Define & Calculate Pearson's Correlation.


```
def PearsonCorr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx, varx = thinkstats2.MeanVar(xs)
    meany, vary = thinkstats2.MeanVar(ys)

    corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx * vary)
    return corr

print PearsonCorr(mom_age, baby_weight)
>>> 0.0688339703541
```
##### Step 7: Define & Calculate Spearman's correlations

```
def SpearmanCorr(xs, ys):
    xranks = pd.Series(xs).rank()
    yranks = pd.Series(ys).rank()
    return thinkstats2.Corr(xranks, yranks)
    
print SpearmanCorr(mom_age, baby_weight)
>>> 0.0946100410966
```
