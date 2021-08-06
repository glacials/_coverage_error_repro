#!/bin/bash
set -euxo pipefail

pip install -r requirements.txt
pyarmor obfuscate __init__.py
coverage run -m pytest test_witness.py