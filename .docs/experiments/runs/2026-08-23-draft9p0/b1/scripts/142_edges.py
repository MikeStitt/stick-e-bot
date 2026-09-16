import sys, numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    img = gui.probe(page)
    print("shape", img.shape)
    # background of the canvas is near-white; sketch lines are dark/blue.
    sub = img[490:550, 930:1130]
    if sub.ndim == 3:
        sub = sub[:, :, :3]
    dark = (sub.astype(int).sum(axis=2) < 600)
    cols = dark.sum(axis=0)
    for i, c in enumerate(cols):
        if c >= 8:
            print("col x=", 930 + i, "count", c)
    rows = dark.sum(axis=1)
    for i, r in enumerate(rows):
        if r >= 40:
            print("row y=", 490 + i, "count", r)
