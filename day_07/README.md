# Strategy

[Advent of Code - Day 7](https://adventofcode.com/2022/day/7)

Today's challenge is a big jump in difficulty from yesterday.

## In Simple Words

Given a series of shell commands, such as `ls` and `cd`, re-create the tree.

## My Approach

I realized the importance of creating an easy to read and logical data structure. I decided to represent each folder using a dictionary, with keys such as `folderName` and `contents`. Inside this array `contents` would be a list of more dictionaries (folders). Here is what my array ultimately looks like after my code parses. It is very readable.

```
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
