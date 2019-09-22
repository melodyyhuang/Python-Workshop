

# Python Workshop Part 1

#### Installation 

Recommended: install the Anaconda Distribution (link: https://docs.anaconda.com/anaconda/). Please follow the Installation instructions for Python 3 and run the following examples in the Getting Started section (link: https://docs.anaconda.com/anaconda/user-guide/getting-started/). 

Note: you are free to use Python 2 or 3. However, the bootcamp examples will be done in Python 3. 

------

**Pedagogical Note:** Some of these questions will be harder than others. Try your best. The goal is to try and understand the problems, and learn how the basics of Python work. 

------

### Day 1 Basics

#### Exercise 1. 

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).



#### Exercise 2. 

Write a function that returns the maximum of two numbers.



#### Exercise 3. 

Write a function that takes in a list of values and returns `True` if the first element and last element are the same, and `False` otherwise. 



#### Exercise 4.

Recall the quadratic formula: 
$$
ax^2+bx+c = 0, \implies x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
Write two functions `quad_pos` and `quad_neg` that return the positive and negative root of the quadratic. The arguments in the function will be `a`, `b`, and `c`. 

Note: you may need to import the `math` library to access the `sqrt` function to help here.

Hint: In Python, to raise a quantity by power `n`, we use double asteriks: `**`. (For example, to raise 2 to the power of 2: `2**2`.)



#### Exercise 5.

Write a function to return the factorial of a given number (named `myFactorial`). (Do not use a built in function to calculate.)

Hint: Recall that the `range()` function will automatically begin indexing at zero. 



#### Exercise 6. 

Write a function `pig_latin` to translate each word from a sentence into pig latin. In other words, when given a word, the function will take the first vowell and move the first part of the word before the vowel to the end, and adds "ay" to it. 

For example:
“hello”:  ellohay
 “computer”: omputercay 
 “string”: ingstray 

Example usage: 

```python
print(pig_latin("hello"))
> "ellohay" 

print(pig_latin("hello world"))
> "ellohay orldway" 
```

Hint: it may be helpful to break this up into several steps. For example,first, find a way to first translate an individual word. Then find a way to parse strings into individual words.



#### Exercise 7.

In economics and life, we often need to solve for $x$ when some arbitrary $f(x) = 0$. 

Write a function such that: 
Given some $f(x)$, an initial guess $x_0$, and a desired tolerance for error $\varepsilon$ (where $|f(x)| \leq \varepsilon$), 
then the function will perform the following: 

1. Calculate the error of the guess $f(x_0)$. 
2. If the magnitude of the residual is less than or equal to the tolerance, then end. 
3. Calculate a correction to the guess and update the guess until it is within the tolerance. 

Newton's Method (link: [https://en.wikipedia.org/wiki/Newton%27s_method](https://en.wikipedia.org/wiki/Newton's_method)) is popular approach to perform such a calculation.

To help, I have provided some example functions and their first order derivative for you to use: 

```python 
import math 

def f1(x): 
    return((x*x)-1)
    
def df1(x): 
    return(2*x)
    
def f3(x): 
    return(math.sin(x))

def df3(x): 
    return(math.cos(x))

def f4(x): 
    return(math.log(x)-1)

def df4(x): 
    return(1/x) 
```



#### Exercise 8..

Write code that counts each term in a given document by looping through each word in the document. You may, for simplicity, assume that a document is represented in a string. Return the data in a dictionary form, where the keys are the words, and the values correspond to the counts. 

For example: 

```python
sample_string = "Hello my name is Melody."
term_count(sample_string)
> {Hello: 1, my: 1, name: 1, is: 1, Melody: 1}
```

Repeat the above, but this time use a dictionary based approach. 

Which method was faster? Why? 

Lastly, find the number of unique words in the string. 

(Continuing the above example...)

```python
unique_words(sample_string)
> 5
```

You may use the sample text here for the exercise: 

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```



