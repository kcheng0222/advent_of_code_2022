# Strategy

[Advent of Code - Day 7](https://adventofcode.com/2022/day/7)

Today's challenge is a big jump in difficulty from yesterday.

## In Simple Words

Given a series of shell commands, such as `ls` and `cd`, re-create the tree.

## My Approach

I wanted to create an easy to read and logical data structure. I decided to represent each folder using a dictionary, with keys such as `folderName` and `contents`. Inside this array `contents` would be a list of more dictionaries (folders).

Here is the file tree that my code generates. It is very readable and helped me make sure I was reading in the inputs correctly.

```python
[{
    'folderName': '/',
    'contents': [{
        'folderName': 'a',
        'contents': [{
            'folderName': 'e',
            'contents': [584]
        }, 29116, 2557, 62596]
    }, 14848514, 8504156, {
        'folderName': 'd',
        'contents': [4060174, 8033020, 5626152, 7214296]
    }]
}]
```
