from typing import Dict, List

from api import check_blocks


def check(blocks: List[str], token: str) -> List[str]:
    """
        Puzzle solver
            Given an array of blocks (str), it sorts them
            based on feedback returned by the API
    """
    ordered_blocks = [True] + [False] * len(blocks[1:])
    for i in range(0, len(blocks)):
        for j in range(i+1, len(blocks)):
            if ordered_blocks[j] == True:
                continue
            together = check_blocks((blocks[i], blocks[j]), api_token=token)
            if together:
                temp = blocks[i+1]
                blocks[i+1] = blocks[j]
                blocks[j] = temp
                break

    return blocks

