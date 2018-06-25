#!/usr/bin/bash

sed -i "s|e1=environ.get('ENV1')|e1='Changed by start script'|"  /root/test_server/say_hello.py
