from const import *
import sys



foo_letters = ['u', 'd', 'x', 's', 'm', 'p', 'f']

vocabulary = []

text_values = {
    'prepositions': 0,
    'verbs': 0,
    'subj_verbs': 0,
    'pretty_nums': 0
}

def analyze_text(tokens):
    for token in tokens:
        is_prep(token)
        is_verb(token)
        is_pretty(token)

def is_prep(token):
    if(len(token) == 6 and 'u' not in token and token[-1] in foo_letters):
        update_dict('prepositions')
        vocabulary.append(token)


def is_verb(token):
    flag = False
    if(len(token) > 5 and token[-1] not in foo_letters):
        update_dict('verbs')
        flag = True
        if(token[0] not in foo_letters):
            update_dict('subj_verbs')
    
    if(flag):
        vocabulary.append(token)

def is_pretty(token):
    number = word_to_num(token)

    if(number >= 81827 and number % 3 == 0):
        update_dict('pretty_nums')


def word_to_num(token):
    num = 0
    base = 1
    for x in token:
        num += heru_digits[x] * base
        base *= 20
    return num



def update_dict(key):
    text_values[key] = text_values[key] + 1

def sort_vocab():
    eng_vocab = sorted(to_english(vocabulary))

    return to_heruglon(eng_vocab)

def to_english(vocab):
    eng = []
    for word in vocab:
        new_word = ''
        for x in range(len(word)):
            new_word += ordered_heruglon_english[word[x]]
        eng.append(new_word)
    return eng

def to_heruglon(vocab):
    her = []
    for word in vocab:
        new_word = ''
        for x in range(len(word)):
            new_word += ordered_english_heruglon[word[x]]
        her.append(new_word)
    return her


def main():
    if(len(sys.argv) == 2):
        try:
            file = open(sys.argv[1], 'r')
        except:
            print('File ' + sys.argv[1] + ' not found')
            sys.exit()
        
        text = file.read().split()


    else:
        print("Missing parameter")
        sys.exit()

    analyze_text(text)

    print('Preps: ', text_values['prepositions'])
    print('Verbs: ', text_values['verbs'])
    print('Subj verbs: ', text_values['subj_verbs'])
    print('Vocabulary list: ', sort_vocab())
    print('There are ', text_values['pretty_nums'], ' pretty numbers')
    

        

main()