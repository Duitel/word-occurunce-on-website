import argparse
import requests
from bs4 import BeautifulSoup
import re
from typing import List, Tuple
from collections import Counter


def get_occurunces_word_in_text(word: str, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
    """
    Get the top 10 occurunces of words in a text.

    Parameters
    ----------
    word : str, the word to search
    text : str, the text to search in
    top_n : int, the number of forms to return, defaults to 10

    Returns
    -------
    List[Tuple[str,int]], a list of the top n occurunces of a word in the text with the count of the word in that form.
    """
    matches = re.findall(f'\S*{word}\S*', text)
    # Count the occurunce per match and return the top N occurunces
    return Counter(matches).most_common(top_n)


def count_word_occurunce_in_text(word: str, text: str) -> int:
    """
    Count the number of matches of words in the text. The word may occur as a substring.

    Parameters
    ----------
    word : str, the word to search
    text: str, the text to search in

    Returns
    -------
    int, the number of occurunces of the word in the text
    """
    matches = re.findall(f'{word}', text)
    count = len(matches)
    return count


def count_character_of_word_occurunce_in_text(word: str, text: str):
    """
    Count the number of matches of words in the text. The word may occur as a substring.

    Parameters
    ----------
    word : str, the word to search
    text: str, the text to search in

    Returns
    -------
    int, the number of occurunces of the word in the text
    """
    char_count = Counter(text)
    return [(char, char_count[char]) for char in word]


def get_webpage_contents(url: str) -> str:
    """
    Get the text contents of the webpage.

    Parameters
    ----------
    url : str, the url of the webpage to get the content from.

    Returns
    -------
    str, the wepage contents
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    text = re.sub(r"\s{2,}", " ", text)
    return text


def convert_case_sensitive_argument(case_sensitive: str) -> bool:
    """
    Convert the case-sensitive argument to True or False.

    '0', 'false', 'False' are converted to False and '1', 'true', 'True' are converted to True. All other values result
    in raising an error.

    Parameters
    ----------
    case_sensitive : str, the argument to convert

    Returns
    -------
    the argument converted to a boolean
    """
    conversion_dict = {
        "0": False,
        "false": False,
        "False": False,
        "1": True,
        "true": True,
        "True": True
    }
    return conversion_dict[case_sensitive]


def main(url: str, word: str, case_sensitive: str) -> None:
    """Main function of the program. Calls the program functions in order:

    0 convert the case-sensitive argument
    1 get the webpage
    2 clean the webpage
    3 convert to case insensitive if wanted
    4 count the word occurunces & report the results
    5 count the letter occurunces & report the results

    Parameters
    ----------
    url : str, the url of the website to look upon.
    word : str, the word to search for.
    case_sensitive : str, whether or not to search case_sensitive

    Returns
    -------
    None
    """
    print(f"Given parameters:\n\turl : {url}, \n\tword : {word}, \n\tcase_sensitive : {case_sensitive}")

    print("Step 0: convert the case-sensitive argument")
    case_sensitive = convert_case_sensitive_argument(case_sensitive=case_sensitive)

    print("Step 1 & 2: get and clean the webpage")
    contents_text = get_webpage_contents(url=url)

    print("Step 3: convert to case insensitive if wanted")
    suffix = "wanted, thus leaving the text and the word in the original form and searching case sensitive."
    if not case_sensitive:
        suffix = "not wanted, thus converting the text and the word to lower case, and searching case INsensitive."
        contents_text = contents_text.lower()
        word = word.lower()
    print(f"\tCase sensitivity {suffix}")

    print("step 4: count the word occurunces & report the results")
    word = word.strip()
    number_word_occurunces = count_word_occurunce_in_text(word=word, text=contents_text)
    print(f"\tNumber of times the word is in the webpage:\n\t\t{number_word_occurunces}")
    top_n = 10
    word_occurunces = get_occurunces_word_in_text(word=word, text=contents_text, top_n=top_n)
    print(f"\tTop {top_n} word forms:")
    for word_form in word_occurunces:
        print(f"\t\t{word_form[0]} : {word_form[1]}")

    print("step 5: count the letter occurunces & report the results")
    character_occurunces = count_character_of_word_occurunce_in_text(word=word, text=contents_text)
    print(f"\tOccurunces of the character of the word (what could have been):")
    for character_occurunce in character_occurunces:
        print(f"\t\t{character_occurunce[0]} : {character_occurunce[1]}")
    print(
        f"\tThus the word could have occured for {min(character_occurunce[1] for character_occurunce in character_occurunces)}. This is an estimation since we neglected double characters in the word.")

    print("Script ended succesfully")


if __name__ == "__main__":  # execute only if run as a script
    parser = argparse.ArgumentParser()

    # -ws URL -w WORD
    parser.add_argument("-ws", "--website", help="The website to look on")
    parser.add_argument("-w", "--word", help="The word to count")
    parser.add_argument("-c", "--case_sensitive",
                        help="Should the search be performed case sensitive or not? [0,false,False,1,true,True]")

    args = parser.parse_args()

    main(url=args.website, word=args.word, case_sensitive=args.case_sensitive)
