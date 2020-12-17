from fuzzywuzzy import process
from fuzzywuzzy.fuzz import ratio

def get_fuzzy_similarity(token = None, dictionary = None):
    """Returns similar words and similarity scores for a given token
    from a provided dictionary of words
    
    Keyword Arguments:
        token {str} -- the reference word (default: {None})
        dictionary {list} -- the list of target words (default: {None})
    
    Returns:
        [list] -- a list of tuples in the form `(matched_word, similarity score)`
    """    

    if token and dictionary:
        return process.extractBests(token, dictionary, scorer= ratio, score_cutoff=70)
    else:
        return []
        
if __name__ == "__main__":
  # toy dictionary of words we will query our mispelt input against
  word_dictionary = ['medium','twitter','google','linkedIn','facebook']
  
  # print the results of the fuzzy match search
  print(get_fuzzy_similarity('mediaum',word_dictionary))