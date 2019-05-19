#!/usr/bin/env python
# -*- coding: utf-8

from pathlib import Path
import shutil


def show_files(path: str, patten: str):
    p = Path(path)
    return p.rglob(patten)


def change_file(file, suffix: str):
    p = Path(file)
    g = p.with_suffix(suffix)
    shutil.move(p, g)


for file in show_files('/tmp', '*.htm'):
    change_file(file, '.html')
