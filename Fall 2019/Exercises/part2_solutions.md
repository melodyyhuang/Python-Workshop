

# Python Workshop - Part 2

#### Part 2 - NumPy 

##### Exercise 1. 

Find indices of non-zero elements from the following vector: $[1,2,0,0,4,0]$. 

```python
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
```



##### Exercise 2. 

Create a $3 \times 3$ identity matrix. 

```python
Z = np.eye(3)
print(Z)
```



##### Exercise 3. 

Normalize a $5\times5$ random matrix. 

```python
Z = np.random.random((5,5))
Z = (Z - np.mean(Z)) / (np.std(Z))
print(Z)
```



##### Exercise 4. 

Let's examine the following vectors: 

$$X = \begin{bmatrix} 1 \\\ 2 \\\ 3 \end{bmatrix},~Y = \begin{bmatrix} 4 \\\ 5 \\  6 \end{bmatrix}  $$

Compute the inner product between $X$ and $Y$. 

```python
X = np.array([1,2,3])
Y = np.array([4,5,6])
print(np.dot(X, Y))
```



##### Exercise 5. 

Given two random arrays, return only the common values between the two arrays.

```python
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
```



##### Exercise 6.

Given two random arrays, how do we know if they are equal? What if we want to know if the values are close enough? 

```python
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)

# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)
```



##### Exercise 7.

Consider a random $10 \times 2$ matrix representing cartesian coordinates, convert them to polar coordinates.

```python
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)
```



##### Exercise 8. 

Using the same $10 \times 2$ matrix of Cartesian coordinates from the previous problem, find the point-by-point distances. 

```python
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
X = X.reshape(10,1)
Y = Y.reshape(10,1)
distances = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(distances)
```



##### Exercise 9. 

The `np` function `np.sign` takes an array and returns an array of the same size, but with $-1$'s and $1$'s to represent the sign of the different elements. Without using the `np.sign` function, how would you do this? 

```python 
x = np.array([1, 3, 5, 0, -1, -7, 0, 5])
r1 = np.sign(x)
r2 = np.copy(x)
r2[r2 > 0] = 1
r2[r2 < 0] = -1
#Check: 
np.array_equal(r1, r2)
```



##### Exercise 10.

Return the diagonal elements of a dot product between two arbitrary $5 \times 5$ matrices.

```python
A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))
np.diag(np.dot(A, B))

#A faster solution: 
np.sum(A * B.T, axis=1)
```



##### Exercise 11. 

Write a function to calculate a moving average using a sliding window over an array. The function should take in an array and the length of the window as inputs. 

```python
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
Z = np.arange(20)
print(moving_average(Z, n=3))
```



##### Exercise 12. 

Find the most frequent value in an array. (Hint: the function `np.bincount` may be helpful here.)

```python
Z = np.random.randint(0,10,50)
print(np.bincount(Z).argmax())
```



##### Exercise 13. 

Consider a one-dimensional simple random walk. The random walk begins at 0 and can take a step forward ($+1$), or step backward ($-1$), with equal probability. Implement a simple random walk with $1000$ steps. First do this using a for-loop, and then write a version without using any for-loops. 

Hint: For the second part, it may be helpful to think about what each step of the random walk consists of. You may find the `.cumsum` function useful. 

 Finally, plot the random walk to visualize. (Use the library `matplotlib.plot` for plotting. [Link](https://matplotlib.org/) to documentation.)

```python
#Using a for loop: 
import random 
position = 0
walk = [position] steps = 1000
for i in xrange(steps):
step = 1 if random.randint(0, 1) else -1 position += step
walk.append(position)

#Without using a for loop: 
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

#Plot
import matplotlib.pyplot as plot
plt.plot(walk)
plt.show()
```



##### Exercise 14. 

Once you have done this, compute useful statistics, such as the minimum and maximum values of the walk. Additionally, something we often care about is something known as the first crossing time, which is the step at which the random walk reaches a particular distance away from the origin for the first time. Write a function that will return such this value. (For example, if we care about the value of 10, we want to find the first time the walk exceeds either 10 or -10.) 

Hint: it may be helpful to remember that when dealing with booleans, `TRUE` values are represented as larger than `FALSE` values. 

```python
print(walk.min())
print(walk.max())

def first_crossing_time(walk, value): 
  return((np.abs(walk) >= value).argmax())
```



##### Exercise 15. 

Simulate 5000 random walks all at once (all of 1000 steps). Calculate the max and min values obtained over all the walks, as well as the average minimum crossing time to 30 or -30. Plot a histogram of the minimum crossing times.

```python
#Simulate walks
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) 
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)

#Compute min/max values: 
walks.max()
walks.min()

#Compute minimum crossing time 
hits30 = (np.abs(walks) >= 30).any(1)
hits30.sum() #How many hit 30 or -30
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()
```

------

#### Part 3 - Pandas

##### Exercise 1. 

Consider the following dictionary: 

```python
import numpy as np
import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 
                   'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```

a. Create a DataFrame from this dictionary `data`, with the index as `labels`. 

```python
df = pd.DataFrame(data, index=labels)
```

b. Then display summary of the basic information about the DataFrame and the data. 

```python
df.describe()
```

c. Return the first 3 rows of the DataFrame.

```python
df.head(3)
```

d. Select just the `animal` and `age` columns of the DataFrame. 

```python
df[['animal', 'age']]
#Alternatively: 
df.loc[:, ['animal', 'age']]
```

e. Select only the rows where the number of visits is greater than 3.

```python
df[df['visits'] > 3]
```

f. Select the rows where the age is missing, i.e. is `NaN`.

```python
df[df['age'].isnull()]
```

g. Select the rows where the animal is a cat and the age is less than 3.

```python
df[(df['animal'] == 'cat') & (df['age'] < 3)]
```

h. Calculate the sum of all visits (the total number of visits).

```python
df['visits'].sum()
```

i. Calculate the mean age for each different animal in `df`. (Hint: use `groupby`)

```python
df.groupby('animal')['age'].mean()
```



##### Exercise 2. 

Consider the following DataFrame: 

```python 
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})
```

Part of data analysis is understanding how to clean data to get it in a form that you can use. 

a. Interpolate the missing values under the `FlightNumber` column. (Hint: use the `interpolate` function.)

```python
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
```

b. Split the `From_To column` into two separate columns (`From` and `To`). Split each string on the underscore delimiter `_` to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

```python
temp = df.From_To.str.split('_', expand=**True**)
temp.columns = ['From', 'To']
```

c. Standardize the strings in the city names so that the first letter is uppercase and rest are lower case (i.e., "MAdrid" should be "Madrid").

```python
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
```



##### Exercise 3. 

Pandas also allows you to do cool things like import data from Yahoo Finance. 

Here is some example code:

```python
import pandas.io.data as web

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
	all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
```

a. Compute the percent changes of the prices. 

```python
returns = price.pct_change() 
print(returns.tail())
```

b. Calculate the covariance and correlation matrices of these stocks. 

```python 
returns.cov()
returns.corr() 
```
