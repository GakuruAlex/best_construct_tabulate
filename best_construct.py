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
    #Declare a table for the results and initialize it to None as a list
    best_table: List[str] = [None for _ in range(len(target_word) + 1)]

    #Set the 0 index to empty list since a str with len 0 can be constructed by str in empty list
    best_table[0] = []

    #loop through the length of the target_word
    for index in range(len(target_word)):
        #For each index of the target word, loop through the strs in the word bank
        for word in word_bank:
            #Check if a slice of the target from the current index and ending at the length of the current word is equal to the current word
            if best_table[index] != None and target_word[index: index + len(word)] == word:
                current_value = best_table[index][:]
                current_value.append(word)

                if best_table[index + len(word)] == None:
                    #If best_table for current word has None value , go ahead and save current_value  as its the current best
                    best_table[index + len(word)] = current_value
                else:
                    #If len of current_value is less than current saved soln,  overwrite saved soln
                    if len(current_value) < len(best_table[index + len(word)]):
                        best_table[index + len(word)] = current_value
    return best_table[len(target_word)]

def main()-> None:
    target_word: str = 'abcdef'
    word_bank: List[str] = ['ab', 'cd',  'c','f', 'abc', 'abcd']
    best_combo: List[str] = best_construct(target_word=target_word, word_bank=word_bank)
    print(f"Best combo of str in {word_bank} that can construct the word '{target_word}'  is {best_combo}")

if __name__ =="__main__":
    main()