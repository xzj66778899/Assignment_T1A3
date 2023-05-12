#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo "ERROR:
    Python3 not installed. 
    Enable to run the application, please refer to https://installpython3.com/ to install Python." >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py