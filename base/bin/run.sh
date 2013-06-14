#!/bin/bash
source "$HOME/.pythonbrew/etc/bashrc"
VENV="Sagittarius"
PY="3.3.0"
pythonbrew use ${PY}
#echo "use ${PY}"
pythonbrew venv use ${VENV}
#echo "venv ${VENV}"
#shift 2
#echo "execute $@ in ${VENV}"
python boot.py $1
deactivate
pythonbrew off
