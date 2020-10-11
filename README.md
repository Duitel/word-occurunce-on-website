# word-occurunce-on-website
A script to count how many times a word (could have been) occured on a webpage.

## To run the script
To run the script use your favorite terminal and type: 
```
python3.6 run.py -ws <URL> -w <WORD> -c <CASE_SENSITIVE>
```
Replace `<URL>`, `<WORD` and `CASE_SENSITIVE` with the webpage url, the word to search for and whether or not to search with case sensitivity or not. 

Possible values for `<CASE_SENSITIVE>` are `0`, `false`, `False` which are converted to `False` and `1`, `true`, `True` which are converted to True. All other values result in an error.
