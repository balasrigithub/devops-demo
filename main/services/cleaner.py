# Author Joey Whelan
""" Text cleaner
"""

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer 
from string import punctuation

stop_words = stopwords.words('english')
tag_dict = {
    "J": wordnet.ADJ,
    "N": wordnet.NOUN,
    "V": wordnet.VERB,
    "R": wordnet.ADV
}
lemmatizer: WordNetLemmatizer = WordNetLemmatizer()

def clean(text):
    """ Function that implements a pipeline for tokenizing and cleaning text

        Parameters
        ----------
        text : plain text to be tokenized and cleaned

        Returns
        -------
        Tokenized, cleaned text
    """      
    if isinstance(text, str):
        tokens = word_tokenize(text.translate(str.maketrans('', '', punctuation)).lower())
        tokens = [token for token in tokens if token.isalpha() and not token in stop_words]
        tokens = pos_tag(tokens)
        lemmas = []
    
        for token in tokens:
            tag = tag_dict.get(token[1][0].upper(), wordnet.NOUN)
            lemmas.append(lemmatizer.lemmatize(token[0], tag))
        return lemmas
    else:
        return None
 

if __name__ == "__main__":
    text = "A Lemma helps to bring words to their dictionary form. \
        It is applied to nouns by default. It is more accurate as it uses more informed analysis to create groups \
            of words with similar meanings based on the context, so it is complex and takes more time. This is used \
                where we need to retain the contextual information."
    print(clean(text)) 