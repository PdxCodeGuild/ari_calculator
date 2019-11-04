
import requests
import re

def count_characters(text):
    count = 0
    for char in text:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
            count += 1
    return count

    # return len(re.findall('\w', text))


def count_words(text):
    # text = text.replace('—', ' ')
    # text = text.replace('-', ' ')
    # print(text.split())
    # return len(text.split())

    return len(re.findall('[\w’]+', text))

def count_sentences(text):
    count = 0
    for char in text:
        if char in '.!?':
            count += 1
    return count

    #return len(re.findall('[\.?!]+', text))


def ari_from_url(url):
    
    regex_title = r"Title: ([\w ']+)"
    regex_author = r"Author: ([\w '.]+)"



    response = requests.get(url)
    text = response.text

    title = re.findall(regex_title, text)[0]
    author = re.findall(regex_author, text)[0]

    start_index = text.find('*** START OF THIS PROJECT GUTENBERG')
    start_index = text.find('\n', start_index)
    end_index = text.find('End of the Project Gutenberg')
    text = text[start_index:end_index]
    # print(text[:200])
    # print('-'*20)
    # print(text[len(text)-200:])


    n_characters = count_characters(text)
    n_words = count_words(text)
    n_sentences = count_sentences(text)

    ari = 4.71*(n_characters/n_words) + 0.5*(n_words/n_sentences)-21.43
    ari = int(ari + 0.5)
    if ari > 14:
        ari = 14

    ari_scale = {
        1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages': '6-7', 'grade_level': '1st Grade'},
        3: {'ages': '7-8', 'grade_level': '2nd Grade'},
        4: {'ages': '8-9', 'grade_level': '3rd Grade'},
        5: {'ages': '9-10', 'grade_level': '4th Grade'},
        6: {'ages': '10-11', 'grade_level': '5th Grade'},
        7: {'ages': '11-12', 'grade_level': '6th Grade'},
        8: {'ages': '12-13', 'grade_level': '7th Grade'},
        9: {'ages': '13-14', 'grade_level': '8th Grade'},
        10: {'ages': '14-15', 'grade_level': '9th Grade'},
        11: {'ages': '15-16', 'grade_level': '10th Grade'},
        12: {'ages': '16-17', 'grade_level': '11th Grade'},
        13: {'ages': '17-18', 'grade_level': '12th Grade'},
        14: {'ages': '18-22', 'grade_level': 'College'}
    }
    age_range = ari_scale[ari]['ages']
    grade_level = ari_scale[ari]['grade_level']


    # print(f'Title:      {title}')
    # print(f'Author:     {author}')
    # print(f'Characters: {n_characters}')
    # print(f'Words:      {n_words}')
    # print(f'Sentences:  {n_sentences}')
    # print(f'Ari:  {ari_scale[ari]}')
    
    return {
        'title': title,
        'author': author,
        'url': url,
        'n_characters': n_characters,
        'n_words': n_words,
        'n_sentences': n_sentences,
        'ari': ari,
        'age_range': age_range,
        'grade_level': grade_level
    }


if __name__ == '__main__':
    url = 'http://www.gutenberg.org/cache/epub/17192/pg17192.txt' # The Raven
    # url = 'http://www.gutenberg.org/cache/epub/60625/pg60625.txt' # Uncle Wiggley
    # url = 'https://www.gutenberg.org/files/60619/60619-0.txt' # Astronomy
    print(ari_from_url(url))