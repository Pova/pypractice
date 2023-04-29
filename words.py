"""
Retrieve and print words from a URL

Usage:

    python3 words.py <URL>

"""

import sys 
from urllib.request import urlopen


# url = 'http://sixty-north.com/c/t.txt'

def fetch_words(url):
    """Fetch a list of words from a url
    
    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        A list of strings containing the words from the document
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """print items from an iterable, one item per line
    
    Args:
        items: iterable series of printable objects
    
    Returns:
        None
    """
    for item in items:
        print(item)


def main(url):
    """Print each word (on a separate line) from a text document from the URL
    
    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        None
    """
    words = fetch_words(url)
    print_items(words)


"""
This controls when the above function is executed.
When words.py is run as a script from the terminal --> fetch_words() is called
When the words module is imported --> the function above is defined but the function is not called
"""
if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
