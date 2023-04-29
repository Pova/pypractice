import sys 
from urllib.request import urlopen

# url = 'http://sixty-north.com/c/t.txt'

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)

"""
This controls when the above function is executed.
When words.py is run as a script from the terminal --> fetch_words() is called
When the words module is imported --> the function above is defined but the function is not called
"""
if __name__ == '__main__':
    main(sys.argv[1])
