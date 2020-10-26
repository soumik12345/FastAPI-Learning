# More on Routes (Ongoing)

As the title suggests, in this part we would explore more on routes, mainly path and query parameters.

## Simple Path Parameters

Before we create anymore routes, we would create a directory called `routes` inside `src/backend/api`. All subsequent 
routes would be created inside this directory. Let's create a file `items.py` inside this directory.

We can declare path *parameters* or *variables* with the same syntax used by Python format strings in the following way:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get('/items/{item_id}')
async def get_item(item_id):
    return {'item': item_id}
```

So, it's clear from the code that if we visit 
[http://localhost:8002/items/anything](http://localhost:8002/items/anything), we would get the response 
`{"item":"anything"}`.

Now, we must write testcases for this route. We know that the scenario is simple enough, such that if we pass anything
in the route, we would get back the same thing. However, while writing testcases, we must make sure that our testcases 
are robust enough so that not a single bug/destructive scenario can get past. Although, it is not possible to figure 
out all edge cases at a single attempt, when it comes to writing testcases, the more, the merrier.

We would now create a file `src/tests/test_items.py` for testing all item related routes. Let's write a simple testcase, such that we pass a deterministic numerical input as `item_id`:

```python
from string import digits

def test_get_item_int(test_backend):
    item_id = int(digits)
    response = test_backend.get('/items/{}'.format(item_id))
    assert response.status_code == 200
    assert response.json() == {'item': str(item_id)}
```

Similarly, we can write another testcase for a deterministic alpha-numerical input for `item_id`:

```python
from string import ascii_uppercase, digits, ascii_lowercase

def test_get_item_string(test_backend):
    item_id = ascii_uppercase + digits + ascii_lowercase
    response = test_backend.get('/items/{}'.format(item_id))
    assert response.status_code == 200
    assert response.json() == {'item': item_id}
```

Now, let's spice things up by writing 2 more testcases for random numerical values, one for floating point values and 
another for integer values:

```python
from random import randint, random

def test_get_item_random(test_backend):
    random_item_id = random()
    response = test_backend.get('/items/{}'.format(random_item_id))
    assert response.status_code == 200
    assert response.json() == {'item': str(random_item_id)}


def test_get_item_randint(test_backend):
    random_item_id = randint(-1000, 1000)
    response = test_backend.get('/items/{}'.format(random_item_id))
    assert response.status_code == 200
    assert response.json() == {'item': str(random_item_id)}
```

Last bit not the least, we would create a testcase for a random alphanumeric input:

```python
from random import choices, randint
from string import ascii_lowercase, ascii_uppercase, digits

def test_get_item_random_str(test_backend):
    random_item_id = ''.join(
        choices(
            ascii_uppercase + digits + ascii_lowercase,
            k=randint(10, 100)
        )
    )
    response = test_backend.get('/items/{}'.format(random_item_id))
    assert response.status_code == 200
    assert response.json() == {'item': random_item_id}
```

Now, lets run the testcases using `./scripts/run_tests.sh`. If all of them passes, we would get a prompt similar to the 
following:

```
======================================================================== test session starts ========================================================================
platform linux -- Python 3.8.1, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /usr/src/backend
collected 6 items                                                                                                                                                   

tests/test_items.py .....                                                                                                                                     [ 83%]
tests/test_ping.py .                                                                                                                                          [100%]

========================================================================= 6 passed in 0.10s =========================================================================
```
