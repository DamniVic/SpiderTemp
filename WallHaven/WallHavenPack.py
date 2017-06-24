#!/usr/bin/python3
# -*- coding:utf-8 -*-
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        '-F', 'WallHaven.py'
    ]
    run(opts)
