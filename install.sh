#!/bin/bash
python -m venv ./.venv
./.venv/bin/pip install flask flask-autoindex
./.venv/bin/python ./start_update_server.py
