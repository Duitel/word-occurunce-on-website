#!/bin/sh

while true; do
  echo "What website you want to look on (please include http/https)?";
  read WEBSITE; #="http://www.python.org"

  echo "What word do you want to look up on website ${WEBSITE}?";
  read WORD;

  echo "Do yo want to perform the search case sensitive? [y/n]";
  read CASE_SENSITIVE;

  echo "Start script";
  echo;

  python3.6 run.py --website $WEBSITE --word $WORD --case_sensitive $CASE_SENSITIVE;

  echo;
done
