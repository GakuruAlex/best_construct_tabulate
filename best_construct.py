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