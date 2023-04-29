from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

def main():
    words = fetch_words()
    print_words(words)

"""
This controls when the above function is executed.
When words.py is run as a script from the terminal --> fetch_words() is called
When the words module is imported --> the function above is defined but the function is not called
"""
if __name__ == '__main__':
    main()
