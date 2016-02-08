[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

*Exercise 1:  Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.*

*Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.*

*Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.*

*Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb."*


### A. Communicate the problem: 
This problem serves to raise the importance of how a distribution might become biased depending on the source of the of the information. In this case, we're interested particularly in the difference between the size of a household (restricted to just the # of kids) compared from when we get the information from the mother's vs. from their kids 


### B. How you solved it: 

I solved this problem by extracting the actual distribution of the number of children in a household as reported by the mothers reporting to the HSFG. I then derive from that another distribution which serves to mimic what the distribution would look like if we surveyed the children themselves. I plot the two distributions and compare their means.

### C. Solution 

As is visible in the two distributions, the biased distribution overrepresents larger families. The mean of the actual distribution is nearly 1 child per household, but the distribution as reported from the kids point of view sets the mean closer to 2.4 kids per household.

This helps show that while the mother is able to provide an all-encomposing number, when kids are surveyed they obviously underrepresent the households with 0 kids (there are no kids to represent them) and overrepresent households with multiple kids (because siblings get counted multiple times.)

<hr>

### D. The Details:


##### Step 1: Import the required datasets.
```
import thinkplot
import thinkstats2
import chap01soln
resp = chap01soln.ReadFemResp()
```

##### Step 2: Construct the actual distribution of the number of children under 18 in the household.

```
kids_hh = resp.numkdhh
actual_dist = thinkstats2.Pmf(kids_hh, label='actual')
```

##### Step 3: Construct the biased distribution if we sampled the children.

```
# Define function for converting from actual to biased/observed distribution
# (From book)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


biased_dist = BiasPmf(actual_dist, label='observed')
```

##### Step 4: Plot the two distributions together
```
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_dist, biased_dist])
thinkplot.Show()
```

![alt text](biased.png =400x350)

##### Step 5: Calculate the means of the two distributions.
```
print actual_dist.Mean()
>>> 1.02420515504
print biased_dist.Mean()
>>> 2.40367910066
```
