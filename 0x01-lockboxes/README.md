this is a solution for the lockboxes problem

## Description
This is a simple Python script that solves the lockboxes problem. The lockboxes problem is a problem where you are given a list of lists, where each list represents a lockbox. Each lockbox contains keys to other lockboxes. The goal is to determine if all lockboxes can be opened.

## Logic
The logic is simple. I used a breadth-first search algorithm. We start by opening the first lockbox and checking if it contains keys to close other closed lockboxes. If it does, we open those lockboxes and check if they contain keys to other closed lockboxes. We continue this process until we have opened all lockboxes or we can't open any more lockboxes.

