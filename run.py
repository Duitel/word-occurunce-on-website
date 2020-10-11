import argparse
import requests
from bs4 import BeautifulSoup
import re


def count_word_occurunce():
    pass


def count_letter_of_word_occurunce():
    pass


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
    3 count the word occurunces
    4 count the letter occurunces
    5 report the results

    Parameters
    ----------
    url : str, the url of the website to look upon.
    word : str, the word to search for.

    Returns
    -------
    None
    """
    print(url, word, case_sensitive)
    print("Step 0")
    case_sensitive = convert_case_sensitive_argument(case_sensitive=case_sensitive)
    print("Step 1")
    contents_text = get_webpage_contents(url=url)
    if not case_sensitive:
        contents_text.lower()
    print(contents_text)


if __name__ == "__main__":  # execute only if run as a script
    parser = argparse.ArgumentParser()

    # -ws URL -w WORD
    parser.add_argument("-ws", "--website", help="The website to look on")
    parser.add_argument("-w", "--word", help="The word to count")
    parser.add_argument("-c", "--case_sensitive",
                        help="Should the search be performed case sensitive or not? [0,false,False,1,true,True]")

    args = parser.parse_args()

    main(url=args.website, word=args.word, case_sensitive=args.case_sensitive)
