#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
  echo "ERROR:
    Python not installed. 
    Enable to run the application, please refer to https://installpython3.com/ to install Python." >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
python3 main.py