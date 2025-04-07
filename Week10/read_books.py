# NOT TESTED AT ALL

from urllib.request import urlopen

def readFileURLString(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)
    return decoded_html

# data_str = readFileURLString('https://www.gutenberg.org/cache/epub/75772/pg75772.txt')
# print(data_str)

# dont run this again VVV

d = {'finnish gibberish' : 'https://www.gutenberg.org/cache/epub/75772/pg75772.txt',
             'spanish gibberish' : 'https://www.gutenberg.org/cache/epub/75775/pg75775.txt',
             'middle english' : 'http://gutenberg.org/cache/epub/8102/pg8102.txt',
             'czech this out ' : 'https://www.gutenberg.org/cache/epub/34225/pg34225.txt',
             }

for book in d:
    output_file = open(book + '.txt','w',encoding='UTF8')
    output_file.write(readFileURLString(d[book]))
    output_file.close()

# gutenburg.org is a bunch of free books as url

'''
--> the function reads the file from a url into a string and return the string
--> pick 5 books
--> read 4 of the 5 books by using their url and the provided function
--> write each of the books into a seperate file (only the story, exclude front matter and end matter)
    make sure to open your file for writing with encoding = 'UTF8'
--> the fifth book don't read or write to a file

using try except do the following for all 5 stories
--> read number of words per story
--> find frequency of each word in the file
--> number of paragraphs (seperated by '' lines)
--> number of sentences
--> length of longest word/smallest word/avg word length
--> most common vowel
-->average usage of punctuation marks for every 100 sentences?
'''

for book in d.keys():
    input_file = open(book + '.txt','r',encoding='UTF8')
    i = 0
    story = []
    for line in input_file:
        i += 1
        story.append(line.rstrip())
        if 'START OF THE PROJECT GUTENBERG' in line:
            start = i
        if 'END OF THE PROJECT GUTENBERG' in line:
            end = i
    story = story[start:end]
    input_file.close()

    output_file = open(book + '.txt','w',encoding ='UTF8')   
    for line in story:
        output_file.write(line + '\n')
    output_file.close() 

# now all files are written and non story sections are omitted

texts = ['czech this out .txt','finnish gibberish.txt','middle english.txt','spanish gibberish.txt','missingbook.txt']

for text in texts:
    try:
        input_file = open(text,'r',encoding = 'UTF8')
    except FileNotFoundError:
        print(f'book: {text[0:text.find('.')]}')
        print(f'{text} not found')
    else:
        on_text = False
        word_count = 0
        paragraphs_count = 0
        words_d = {}
        longest_word = ''
        shortest_word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        avg_word_length = 0
        vowels = {'a': 0,'e': 0,'i': 0, 'o':0, 'u': 0, 'y': 0}
        for line in input_file:

            previous_state = on_text
            if line != '\n':
                on_text = True
            elif line == '\n':
                on_text = False
            if previous_state == False and on_text == True:
                paragraphs_count +=1

            line = line.rstrip().split(' ')
            if line != ['']:
                while '' in line:
                    line.remove('')

                for word in line:
                    if word.isalpha():
                        if word not in words_d and word.isalpha():
                            words_d[word] = 0
                        if word.isalpha():
                            words_d[word] += 1
                        if len(word) < len(shortest_word):
                            shortest_word = word
                        if len(word) > len(longest_word):
                            longest_word = word
                        avg_word_length += len(word)
                        word_count += 1
                        for char in word:
                            if char in vowels.keys():
                                vowels[char] += 1

        print(f'book: {text[0:text.find('.')]}')
        print(f'word count: {word_count}')
        # for word in words_d.keys():
        #     print(word,words_d[word])
        print(f'paragraph count: {paragraphs_count}')
        print(f'longest word: {longest_word}, length: {len(longest_word)}')
        print(f'shortest word: {shortest_word}, length: {len(shortest_word)}')
        print(f'avg word length: {avg_word_length // word_count}')
        most_common_vowel = 'a'
        for vowel in vowels:
            if vowels[vowel] > vowels[most_common_vowel]:
                most_common_vowel = vowel
        print(f'most common vowel: {most_common_vowel,vowels[most_common_vowel]}')
        input_file.close()
