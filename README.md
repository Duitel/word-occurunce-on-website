# word-occurunce-on-website
A script to count how many times a word or (sub)string (could have been) occured on a webpage.

## To run the script
To run the script use your favorite terminal and type: 
```
python3.6 run.py -ws <URL> -w <WORD> -c <CASE_SENSITIVE>
```
Replace `<URL>`, `<WORD` and `CASE_SENSITIVE` with the webpage url, the word to search for and whether or not to search with case sensitivity or not. 

Possible values for `<CASE_SENSITIVE>` are `0`, `false`, `False`, `no`, `n` which are converted to `False` and `1`, `true`, `True`, `yes`, `y` which are converted to True. All other values result in an error.

## Example
For example the command `python3.6 run.py -ws https://www.python.org/ -w python -c 0` returned the following (the output counts could be different today depending on a update of the website.):

```
Given parameters:
	url : https://www.python.org/, 
	word : python, 
	case_sensitive : 0
Step 0: convert the case-sensitive argument
Step 1 & 2: get and clean the webpage
Step 3: convert to case insensitive if wanted
	Case sensitivity not wanted, thus converting the text and the word to lower case, and searching case INsensitive.
step 4: count the word occurunces & report the results
	Number of times the word is in the webpage:
		69
	Top 10 word forms:
		python : 55
		python. : 2
		python.org : 1
		python, : 1
		python!") : 1
		python! : 1
		python's : 1
		docs.python.org : 1
		jobs.python.org : 1
		(python : 1
step 5: count the letter occurunces & report the results
	Occurunces of the character of the word (what could have been):
		p : 222
		y : 144
		t : 454
		h : 158
		o : 425
		n : 428
	Thus the word could have occured for 144. This is an estimation since we neglected double characters in the word.
Script ended succesfully
```
 
 ## Run with shell script
 It is also possible to use the shell script, `start_and_loop_run_script.sh`, to gather the parameters and run the python script `run.py`.
 