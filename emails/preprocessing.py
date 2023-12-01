from string import punctuation, digits
import re
from nltk.corpus import stopwords, words
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class EmailCleaner:
    """Cleaner for e-mails, with a cleaning method that performs several steps:
    - remove HTML tags
    - lowercase all characters
    - remove non-english words
    - remove punctuation and digits
    - remove stopwords
    - lemmatize
    
    The last 3 steps are optional and can be turned off."""

    def __init__(self, 
                 remove_stopwords=True, 
                 remove_symbols=True,
                 lemmatize=True):
        
        self.remove_stopwords = remove_stopwords
        self.remove_symbols = remove_symbols
        self.lemmatize = lemmatize

        self.english_words = set(words.words())

        # optional
        self.stop_words = set(stopwords.words('english')) if remove_stopwords else None
        self.chars_to_remove = {ord(p): None for p in punctuation + digits} if remove_symbols else None
        self.lemmatizer = WordNetLemmatizer() if lemmatize else None

    def _lemmatize(self, word):
        """Lemmatize a token, whether it is a verb, noun, or adjective."""
        word = self.lemmatizer.lemmatize(word, pos='a')
        word = self.lemmatizer.lemmatize(word, pos='n')
        word = self.lemmatizer.lemmatize(word, pos='v')
        return word

    def clean(self, document):
        """Clean a document string and return a string of tokens"""
        document = document.replace('Subject:', '') # remove 'Subject:' string (present in every email)
        document = re.sub(r'<[^>]*>', '', document) # remove HTML tags
        document = document.lower()                 # lowercase all characters

        if self.remove_symbols:                     # remove punctuation and digits (if requested)
            document = document.translate(self.chars_to_remove)

        # clean words: remove stopwords, check if english word, lemmatize
        clean_words = []
        for word in word_tokenize(document):
            if self.remove_stopwords and word in self.stop_words:  # check whether is stop word (if requested)
                continue

            if word not in self.english_words:                     # check whether is english word
                continue

            if self.lemmatize:                                      # lemmatize (if requested)
                word = self._lemmatize(word)

            clean_words.append(word)

        return ' '.join(clean_words)