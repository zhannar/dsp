# Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)  

## Instructions

The ThinkStats book is approximately 200 pages in length.  It is recommended you read the entire book, particularly if you are less familiar with introductory statistical concepts.

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  You could import it, or you could write your own to practice python and develop a deeper understanding of the concept. 

Complete the following exercises along with the questions in this file. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

---

### Instructions for cloning the repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/prework  
(Windows):  C:/ds/metis/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/prework/ThinkStats2/code
```

---

###Required Exercises

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

###Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 

###Q5. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

###Q6. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

###Q7. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

<hr>
##### *My Answer:*

This question asks us, what is the probability that Elvis is an identical twin given knowledge that he was a twin. This is a conditional probability and merits the use of Bayes Theorem. As a reminder, **this is Bayes Theorem:**

![alt text](bayes.jpg =400x100)

**Step 1:** For our purposes, our variables are translated as as:

```
A = Elvis is an identical twin.
B = Elvis is a twin.
```
**Step 2:** Converting this into mathematical notation gives us:

```
P(A|B) = P(Elvis is an identical twin | Elvis is a twin)
```

**Step 3:** Now we use Bayes Theorem to get us...

```
P(A|B) = P(Elvis is a Twin | Elvis is an identical Twin) * P(Elvis is an Identical Twin) / P(Elvis is a Twin)
```

**Step 4:** First, we'll employ some common logic to simplify the calculations. The first conditional, P(B|A) or that probability that Elvis is a twin given that he's an identical twin is 1. 

```
P(A|B) = 1 * P(Elvis is an Identical Twin) / P(Elvis is a Twin)
```
**Step 5:** Secondly, we are given in the problem that the probability that someone is born an identical twin is 1/300. From that, we can extrapolate that knowing nothing else, the probability that Elvis were born an identical twin should also be 1/300. Thus, we fill in the second part of the numerator: 

```
P(A|B) = 1 * (1/300) / P(Elvis is a Twin)
```

**Step 6:** Thirdly, the denominator or P(B)=P(Elvis is a twin) requires us to us to make some conceptual assumptions: 

- there are only two ways of being a twin; one is either a fraternal twin or an identical twin.
- one cannot be both an identical and a fraternal twin (at least to the same person); they are mutually exclusive
- one cannot be a form of being a twin which is neither fraternal or identical / there are no other ways of being a twin.

All this leads us to realize that P(Elvis is a Twin) is equivalent to the mathematical concept of a union and gets translated as follows:


```
P(Elvis is a Twin) = The union of Elvis being an identical twin and Elvis being a fraternal twin minus the intersection of that being the case. 
```
That is.... 

```
P(Elvis is a Twin) = P(Elvis is Fraternal) + P(Elvis is Identical)
P(Elvis is a Twin) = (1/125) + 					(1/300)
P(Elvis is a Twin) = (12/1500) + 				(5/1500)
P(Elvis is a Twin) = (17/1500) 
```

So, plugging that into our headline equation and solving...

```
P(A|B) = 1 * (1/300) / P(Elvis is a Twin)
P(A|B) = 1 * (1/300) / (17/1500)
P(A|B) = 1500 / (300 * 17)
P(A|B) = 1500 / (300 * 17)
P(A|B) = 0.294

```
##### *Thus, the probability that Elvis was an identical twin given knowledge that he was a twin, is 29%.*

---

###Q8. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?


**Definitions of Probability: Objective vs. Subjective -** Neither approach is wrong or right. They are merely two sides of the same coin. If one is walking down the street and sees a giant turtle with a purple hat. One might ask, what's the probability of that event? The frequentist and Baysian approuches arise out of a foundamental difference in how they see probabilty of an event. The frequentists take their starting point with the giant turtle and his purple hat. The Baysians start with the person observing everything. For the frequentists, probabiilty comes from objective physical phenomina. Ergo, they'd say the giant turtle is "a result of sampling: observed frequencies of things in a sample." The Bayesians, on the other hand, think that probabilities are in the mind of the observer (subjective). Ergo, the giant turtle is a state of knowledge or confidence rather than an objective fact about the world (statistics/frequencies). 

**Defined by Goals, Not Methods:** Surely if they have these two radically different viewpoints, they will do different things. Not necessarily. The split between the frequentists and Baysian approuch to inference is defined by their **goals** and _**NOT**_ by their **methods.** This is very important. This means, that if you were to see a person performing this or that statistical method, that alone would not inform you of whether that analysis was being done in a baysian or a frequentist method. Each is instead defined by their **goals** and the kinds of statements they're interested in making. I will touch on the difference in goals later in the next section.

**Models and Parameters that Define Them** In both cases, the frequentist and Bayesian would desire to model the data or come up with a distribution to explain the observed data given a set of parameters. In both cases, the would likely want to specify those parameters by a method of greatest liklihood -- that is, choose the parameters which would have the greatest liklihood of producing the observed data. However, the way these parameters are interepreted is different. The frequentists view the parameters as fixed but not known. As a result, they envision if the situation/experiement were *repeated* multiple times, the underlying system is intrinsically deterministic/should stay the same and therefore produce the same results. As a result, they define their certainty in their estimates against the background of these repeated results.

The Bayesians however view the parameters as mere instantiations of random variables -- the system itself is random. As such, they cling tightly to the data they do have (data is fixed), and are more likely to vary their belief in what the underlying random process which produces it. The goal of Bayesian inference is thus to describe or analyze your degree of beliefs. 

The goal of frequentist inference is to come up with a frequency gaurantee or a confidence interval. This number, let's say 95%, is to be interpreted as holding true 95% of the time if the situation were repeated 100 times. The idea of repeatability of an event is highlighted. 

**I've summerized these and other nuances in a table:**

| Dimension | Frequentist		 | Bayesian |
| :------------ | :-----------------: | :------------: |
|*What's probability?* | A result of sampling: observed frequencies of things in a sample.| Bayesians think that probabilities are in the mind (subjective). They are states of knowledge or confidence rather than objective facts about the world (statistics/frequencies).|
|*Probability: Objective or Subjective?* | Objective | Subjective|
|*Focus is on:*         | the data        | the priors
|*Starts with a distribution (or a 'model' more generallly)?*         		| Yes        | Yes
|*Use liklihood implied by the data/model?* | Yes        | Yes
|*Data are...* | a repeatable random sample (there is frequency)|are observed from the realized sample |
|*Underlying parameters:* |remain constant during this repeatable process |unknown and described probabilistically|
|*Interpretation of Parameters*         | fixed but unknown quantities.         | Random Variables
|*What's fixed?* |Parameters |Data|
|*Answer Form:* | Answer is a confidence statement.      | Answer is a probability statement.
|*Interval:* | frequentist confidence interval        | Bayesian credible interval
|*Answer Example*         |  "With 95% confidence based on the data I observed, the population mean is between 2.3 and 4.2."          |"There is a 95% probability that the population mean is between 2.3 and 4.2 (given the data I observed)".  
|*Making Predictions (Joke)*         | "I threw this die twice and it came up 5 twice. So I conclude this die will always come up 5"        | "I threw this die five hundred times and it came up 5 every single time. I did start with a very strong bias towards the die being fair, though, so my expectation that the die will come up 5 if I throw it again is slightly more than 1/6."
|*Common Advocates* |Neymann, Person, Wald |Bayes, Laplace, de Finetti|

*References:*

- [Quora](https://www.quora.com/What-is-the-difference-between-Bayesian-and-frequentist-statisticians) 
- [Stack Overflow (Stats)](http://stats.stackexchange.com/questions/22/bayesian-and-frequentist-reasoning-in-plain-english) 
- [George Casella - U. of Florida - Class PDF](http://www.stat.ufl.edu/archived/casella/Talks/BayesRefresher.pdf) 
- [Normal Deviate Wordpress]( https://normaldeviate.wordpress.com/2012/11/17/what-is-bayesianfrequentist-inference/ ) 
- [Keith Weinstein](http://blog.keithw.org/2013/02/q-what-is-difference-between-bayesian.html) 


<!---
[comment]: <> (This is storing additional things I've written or consider adding to this.
Reference: http://stackoverflow.com/questions/4823468/comments-in-markdown


0) Ways to introduce my answer to the question and explain how i have explained.
##### *My Answer:*
While it may be possible to _**explain**_ the frequentist and Baysian views in a sentence or two, it's impossible for the reciever to truly _**understand**_ that answer in as short a period of time. To understand their meanings, the similarities, and the differences requires an iterative approuch that spans across different modes of explanations. 

This explanation will be roughly structured as follows:

1. Basic Definitions (Abstract)
2. Some Examples (Specific)
3. Highlighting similarities & Differences (Abstract)


### By a definition

1) Ways ot Introduce the Topic:

- "In this modern world, the notion of probability is unavoidable. Just as our civilizatio no longer operates in the geocentric mindset where the earth is the center of everything, we as individuals understand that we are the center of 
- We change as people
- Unlike the ameoba who has no history and can operate / respond to only things in their immediate environment, we humans understand that beside our present here and now, there are others and they themselves have a here and now, or alternatively that other presents have existed as well.
- If one takes the starting point of any problem for which one is using statistics, one faces the task of measurement and the notion of probability.
- If a tree falls in the forrest and no one is there to see it, did a tree fall. 
- The root of all scientific inquiry starts with an event observed by someone. If that someone 


2) what's missing.... EXAMPLES!! EXAMPLES!!! EXAMPLES!!!

Frequentists do not allow themselves to assign probability statements to parameters. 

Confidence Intervals Do Not Represent Degrees of Belief.
Posterior Intervals Do Not (In General) Have Frequency Coverage Properties.

3) This is a great example and should be reconsidered and analyzed further...:
http://blog.keithw.org/2013/02/q-what-is-difference-between-bayesian.html


### By an Example

Let's consider a few examples.

If you go into a doctor's office complaining of pain in your chest. The relevant question here is: what's causing your pain?

- **The Frequentist** looks at this by considering a population of people who are also exhibiting that particular sympton (chest pain). There are some number of different causes that's leading all the people in that population to exhibit that same symptom, and those causes pop up in different frequencies. 

### Description vs Prescription

| Statement | Truth or False| Explanation
| ----------- | -----------| -----------
| There are frequentist techniques and baysian techniques. | False| They are differentiated by their goals, not their methods
| Using Bayes Theorem/Rule is Bayesian Inference          | False| The former is a method/technique and is not sufficient to differentiate between approuches.
| Using Bayes Nets is Bayesian Inference        | False| The former is a method/technique and is not sufficient to differentiate between approuches.
| Center        | False| The former is a method/technique and is not sufficient to differentiate between approuches.

-->

---

###Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

###Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
###Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
###Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

## More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.







