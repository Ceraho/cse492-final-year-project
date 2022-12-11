#!/usr/bin/bash

if which python3 &>/dev/null; then
  if which virtualenv > /dev/null; then
    # virtualenv is installed, so do something
    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    python3 main.py
    exit 1
  else
    # virtualenv is not installed, so do something else
    pip install virtualenv
    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    python3 main.py
    exit 1
  fi
else
  if which python &>/dev/null; then
    if which virtualenv > /dev/null; then
      # virtualenv is installed, so do something
      virtualenv venv
      . venv/bin/activate
      pip install -r requirements.txt
      python main.py
      exit 1
    else
      # virtualenv is not installed, so do something else
      pip install virtualenv
      virtualenv venv
      . venv/bin/activate
      pip install -r requirements.txt
      python main.py
      exit 1
    fi
  else
    echo "Error: Python is not installed on this system, please install python 3.X.X on your system!"
    exit 1
  fi
fi
