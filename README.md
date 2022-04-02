# stack-y42
A stack data structure functionality in python.
In this project, I used pytest for testing the stack functionality.

## Requirements
* [Python 3.7+](https://www.python.org/downloads/)
* [Pytest 7.1+](https://docs.pytest.org/en/7.1.x/getting-started.html)


## Installation

### Project Requirements

Create a new virtualenv:

```
$ cd stack-y42/
$ python3 -m venv venv
```

In the root directory of the project, run below command in the terminal:

```
pip install -r requirements.txt
```

## Test

Run below command to test all code:

```
$ pytest
```

## Description

I used a `base` package for the project infrastructures, such as custom `exception`

so, I use the custom exception in other packages

```
from base.exceptions import NullElementException, EmptyStackException
```

and also I used a package for stack functionalities, Its name is `stacks`,

and a test file in the stacks package for stacks functionalities tests, Its name is `test_stacks.py`


## How to use it

if you want to use it, just import it

```
from stacks.stack import Stack

...


stack = Stack()

stack.push()
stack.pop()
stack.peek()
stack.empty()
stack.size()
```