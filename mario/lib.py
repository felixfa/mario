#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored

def try_me():
    name = input('What is your name? ')
    print()
    return f"It's me! {colored(name,'red')}!"
