# Interview Questions


```
Please select one of the questions below and write the code to solve it. Once you have a solution, please create a github repo and send it to julien@enzyme.com for review.

We are looking for:
- completeness
- style
- and testing.

## 1. Hash Compare

You have 2 hashes. You are looking for the difference between the 2. What was added or removed or if the hash is the same.
- Hash only have string keys
- Hash only have string, boolean, number, array or hash as value
- Compare should have an option for deep or shallow compare
- Compare should list the difference for keys and values
```


## Usage

Deep search (default):
```
python3 main.py '{...}' '{...}'
```

Shallow search (matches on type, not on value):
```
python3 main.py '{...}' '{...}' True
```

```
python3 main.py '{"first": {"second": {"third": "level"}}}' '{"first": {"second": {"third": 1,"fourth": [1,2]}}}'
python3 main.py '{"first": {"second": {"third": "level"}}}' '{"first": {"second": {"third": 1,"fourth": [1,2]}}}' 1
```

### Tests

There are some simple unit tests. They can be run with the following command:

```
python3 test_compare.py
```

# Author

Michael Burns <michael@mirwin.net>
