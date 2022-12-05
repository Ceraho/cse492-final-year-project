#!/usr/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]
then
  pip install virtualenv
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
fi
source venv/bin/activate
pip install -r requirements.txt

if which python3 &>/dev/null; then
  python3 main.py
else
  if which python &>/dev/null; then
    python main.py
  else
    echo "Error: Python is not installed on this system"
    exit 1
  fi
fi
