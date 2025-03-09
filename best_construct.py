from typing import List
from copy import deepcopy
def best_construct(target_word: str, word_bank: List[str]) -> List[str]:
    """_Find the least amount of words in word_bank required to make a target word by concatenating them_

    Args:
        target_word (str): _A str to construct_
        word_bank (List[str]): _A list of str to choose from_

    Returns:
        List[str]: _A list containing str required to make target word_
    """
    #Declare a list and initialize it to None
    best: List[str] = [None for _ in range(len(target_word) + 1)]

    #Set the 0 index to empty list since a str with len 0 can be constructed by str in empty list
    best[0] = []

    #loop through the length of the target
    for index in range(len(target_word)):