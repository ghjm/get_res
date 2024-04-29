#!/bin/env python3
from pathlib import Path


def getResDirs(path):
    p = Path(path)
    r = list(p.glob(".RES", case_sensitive=False))
    if r:
        yield p.absolute()
        for sub in p.iterdir():
            if sub.is_dir():
                yield from getResDirs(sub.absolute())


for d in getResDirs("test"):
    print(d)
