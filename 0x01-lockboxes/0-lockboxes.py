#!/usr/bin/python3

'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
'''


def join(list_1, list_2):
    '''return a list of elements '''
    result = []
    for elem in list_2:
        result += list_1[elem]
    return result


def canUnlockAll(boxes):
    ''' return T if all boxes can be opened else, F '''
    boxes = boxes if boxes and isinstance(boxes, list) else []
    idx = 0
    total = list(set(boxes[0]) | {0})
    can_open = True
    while can_open:
        can_open = False
        for i in join(boxes, total[idx:]):
            if i not in total:
                total.append(i)
                idx += 1
                can_open = True
    return len(total) == len(boxes)


if __name__ == '__main__':
    canUnlockAll = __import__('0-lockboxes').canUnlockAll

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
