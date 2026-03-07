
"""
I will be doing a text processing and 15 frequent word analysis on the book frankenstain by mary shelly
I chose it because it is a classic novel and i have read it before. i am interested in seeing which words are most commonly
 used in the book and how they contribute to the overall themes and tone of the story. 
I want to atleast cover the 1st chapter of the book and analyze the text to find the most frequent words 
and their significance in the context of the story.
the text url:https://www.gutenberg.org/cache/epub/84/pg84.txt
"""

import operator

# Function to fetch data from chapter 1 of the book
def fetch_text(raw_url):
  """Fetch text from the given URL and return only Chapter 1.
  Detailed explanation: This function takes a URL as input, 
  checks if the text has already been cached locally, and if not, 
  it fetches the text from the URL and saves it to a local cache file.
  It then extracts and returns only Chapter 1 from the full text.
  Parameters:
    raw_url (str): The URL to fetch the text from.
    Returns:
    str: Chapter 1 text from the fetched content. If an error occurs, returns an empty string."""
  import requests
  from pathlib import Path
  import hashlib

  CACHE_DIR = Path("cs_110_content/text_cache")
  CACHE_DIR.mkdir(parents=True, exist_ok=True)

  def _url_to_filename(url):
    """Generate a cache filename from a URL hash."""
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    return CACHE_DIR / f"{url_hash}.txt"

  cache_path = _url_to_filename(raw_url)

  SUCCESS_MSG = "✅ Text fetched."
  FAILURE_MSG = "❌ Failed to fetch text."
  try:
    if not cache_path.exists():
      response = requests.get(raw_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
      response.raise_for_status()
      text_data = response.text
      cache_path.write_text(text_data, encoding="utf-8")
    print(SUCCESS_MSG)
    full_text = cache_path.read_text(encoding="utf-8")
    
    # Extract only Chapter 1
    chapter_1_start = full_text.find("CHAPTER I")
    if chapter_1_start == -1:
      chapter_1_start = full_text.find("Chapter I")
    if chapter_1_start == -1:
      chapter_1_start = 0
    
    chapter_2_start = full_text.find("CHAPTER II", chapter_1_start)
    if chapter_2_start == -1:
      chapter_2_start = full_text.find("Chapter II", chapter_1_start)
    if chapter_2_start == -1:
      chapter_2_start = len(full_text)
    
    return full_text[chapter_1_start:chapter_2_start]

  except Exception as e:
    print(FAILURE_MSG)
    print(f"Error: {e}")
    return ""

# Save the URL in a variable
Frankenstein= "https://www.gutenberg.org/cache/epub/84/pg84.txt"

# Fetch the text
frankenstein_text = fetch_text(Frankenstein)

# Using spaCy for advanced text processing
import spacy

nlp = spacy.load('en_core_web_sm')

def word_tokenization_normalization(text):
    """Tokenize and normalize the text using spaCy.Detailed explanation: Lowercases and lemmatizes text, filtering out stop words,
punctuation, numbers, and tokens shorter than 3 characters.

Parameters:

text (str): Raw input text to tokenize and normalize.
Returns:

list: A list of normalized word strings (lemmas).
"""
    

    text = text.lower() # lowercase
    doc = nlp(text)     # loading text into model

    words_normalized = []
    for word in doc:
        if word.text != '\n' \
        and not word.is_stop \
        and not word.is_punct \
        and not word.like_num \
        and len(word.text.strip()) > 2:
            word_lemmatized = str(word.lemma_)
            words_normalized.append(word_lemmatized)

    return words_normalized


def word_count(word_list):
    """Count the frequency of each word in the list.
    Detailed explanation: Lowercases each word and accumulates occurrence counts in a dictionary.

Parameters:

word_list (list): List of word strings to count.
Returns:

dict: Mapping from word (str) to count (int).
"""
    word_counts = {}
    for word in word_list:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
    return word_counts


def print_top_15_frequent_words(word_counts):
    """Print the top 15 most frequent words and their counts.
Detailed explanation: Sorts the word/count dictionary by count in descending order,
extracts the top 15 pairs, and prints each in "word: count" format.

Parameters:

word_counts (dict): Mapping from word (str) to count (int).
Returns:

None: Prints the top 15 word/count pairs to standard output.
"""
    sorted_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_15_words = list(sorted_word_counts.items())[:15]  # Get the top 15 words and counts
    for word, count in top_15_words:
        print(f"{word}: {count}")

def top_10_frequentverbs(doc):
    """Print the top 10 verbs in the text."""
    counts = {}

    for t in doc:
        if t.pos_ == "VERB" and t.is_alpha:
            lemma = t.lemma_.lower()
            counts[lemma] = counts.get(lemma, 0) + 1

    top10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop 10 Verbs:\n")
    for verb, c in top10:
        print(f"{verb}: {c}")

     
words_normalized = word_tokenization_normalization(frankenstein_text)
print(words_normalized)
new_counts = word_count(words_normalized)
print(new_counts)

print("Top 15 Frequent Words:")
print_top_15_frequent_words(new_counts)

print("\nTop 10 Frequent Verbs:")
top_10_frequentverbs(nlp(frankenstein_text))

"""
the top 15 frequently occurring words in the text are very relevant words to the the books narrative. See the book talks of resurrecting life that came from a place of childhood imagination
with victor frankenstain being the main character who is obsessed with the idea of creating life. with his father being second because he helped support frankenstein in his scientific pursuits
Life is also the main premise of the book, because its a story about a monstrosoity coming life. With the rest of the words being used to imply his life from childhood to adulthood. His friend to is also another scharacter 
who is a close friend of victor frankenstain and is also a victim of the monster. The word "one" is also used frequently because it is used to refer to the monster as a singular entity.
though some words are most used as filler to help him convey his thoughts and feelins to the reader. i think the word usage can imply a mans life as it kind of speaks on words relative to someones story of life. like a narrative from third person.
defintley though the genre does not seem gothic more of a lifestyle novel.
"""
"""
so i added the top frequent verbs to helps me interpret the book, bceause when last rembering the book. It entails a 
lot of action especially to frankensteins actions which helps describe his obsessions with lively senses. which the 10 words defintley explain
that he defines his senses and starts entailing a narrative of discovery in tuned with life.
"""


