"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""

languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}

def sort1(lang):
    output = sorted(sorted(lang), key=lang.__getitem__)
    print("1.")
    for items in output:
        print("\t" + items)

def sort2(lang):
    output = sorted(sorted(lang), key=len)
    print("2.")
    for items in output:
        print("\t" + items)

def sort3(lang):
    output = sorted(sorted(lang), key=lambda x:x[-1].lower(), reverse=True)
    print("3.")
    for items in output:
        print("\t" + items)

def main():
    sort1(languages)
    sort2(languages)
    sort3(languages)

if __name__ == '__main__':
    main()

