
import spacy
import subprocess
from string import punctuation

def extract_keywords(nlp, sequence : list = None):
    """ Takes a Spacy core language model,
    string sequence of text and optional
    list of special tags as arguments.
    
    If any of the words in the string are 
    in the list of special tags they are immediately 
    added to the result.  
    
    Arguments:
        sequence {str} -- string sequence to have keywords extracted from
    
    Keyword Arguments:
        tags {list} --  list of tags to be automatically added (default: {None})
    
    Returns:
        {list} -- list of the unique keywords extracted from a string
    """    
    result = []

    # custom list of part of speech tags we are interested in
    # we are interested in proper nouns, nouns, and adjectives
    # edit this list of POS tags according to your needs. 
    pos_tag = ['PROPN','NOUN','ADJ']

    # create a spacy doc object by calling the nlp object on the input sequence
    doc = nlp(sequence.lower())

    for chunk in doc.noun_chunks:
        final_chunk = ""
        for token in chunk:
            if (token.pos_ in pos_tag):
                final_chunk =  final_chunk + token.text + " "
        if final_chunk:
            result.append(final_chunk.strip())


    for token in doc:
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if (token.pos_ in pos_tag):
            result.append(token.text)
    return list(set(result))

if __name__ == "__main__":
  """
  install the langauge model using the subprocess package
  useful when hosting the service in the cloud as it prevents against
  us forgetting to do this via the CLI
  """
  subprocess.call("python -m spacy download en_core_web_sm",shell=True)

  # load the small english language model, 
  nlp = spacy.load("en_core_web_sm")

  print("Loaded language vocabulary")
  textFile = open('The Hunger Games.txt', 'r')
  
  text = ''
  for x in textFile:
      text+=x
  
  keywords = extract_keywords(nlp,text)
  
  print("keywords",keywords)
  print("Length of keywords",len(keywords))  
  print("Length of keywords",len(text.split(' ')))