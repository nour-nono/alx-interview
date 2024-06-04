#!/usr/bin/python3
"""LockBoxes Challenge"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    Args:
        boxes: list of lists
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    # if boxes is None or not isinstance(boxes, list)\
    #    or any([1 for x in boxes if not isinstance(x, list)]):
    #     return True
    if len(boxes) < 2:
        return True
    queue = set([0])
    boxes_state = [0 for x in boxes]
    while len(queue):
        current = queue.pop()
        if boxes_state[current] == 1 and current < len(boxes):
            continue
        for x in boxes[current]:
            if boxes_state[x] == 0:
                queue.add(x)
        boxes_state[current] = 1
    return 0 not in boxes_state
