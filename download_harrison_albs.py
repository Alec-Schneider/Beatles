# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:10:59 2020

@author: Alec
"""


import processing

base_dir = 'C:\\Users\\Alec\\MyPython\\Beatles\\harrison'

dirs = ["AllMustPass", "MaterialWorld", "DarkHorse",
        "ExtraTexture" , "ThirtyThree", "GeorgeHarrison",
        "SomewhereEngland", "GoneTroppo", "CloudNine",
        "Brainwashed"
        ]

gh = {
      "All Things Must Pass": {
        "directory": base_dir + "\\AllMustPass\\dl",
        "link": "https://www.youtube.com/watch?v=A-AuNXBMSNU&list=PLhh2Mh7vZHr3QGsXXMvnBIjTZpKU5HEGo"
        },
      "Living In The Material World": {
        "directory": base_dir + "\\MaterialWorld\\dl",
        "link": "https://www.youtube.com/watch?v=zVXRVef2wpk&list=PLA0N6JK7gVyX-3fVHh84hBmDcCJ7Zo241"
        },
      "Dark Horse": {
        "directory": base_dir + "\\DarkHorse\\dl",
        "link": "https://www.youtube.com/watch?v=AOrZvkZMzsQ&list=PLmVVLc3PLstTaCFapCvIhhNDV8ipq4d4o"
        },
      "Extra Texture (Read All About It)": {
        "directory": base_dir + "\\ExtraTexture\\dl",
        "link": "https://www.youtube.com/watch?v=3xnTWee4eAI&list=OLAK5uy_lQWa097lxbJVPkZJBbDTMu63h83vWm7eM"
        },
      "Thirty Three & 1/3": {
        "directory": base_dir + "\\ThirtyThree\\dl",
        "link": "https://www.youtube.com/watch?v=ZuwCZE7g-EU&list=PL7JAhfh91roz3I5U3k_HEVM9B13kwq1HE"
        },
      "George Harrison": {
        "directory": base_dir + "\\GeorgeHarrison\\dl",
        "link": "https://www.youtube.com/watch?v=lg78Yy7iCTk&list=PLi_eUMd6th2J37cc3ArkI1v7V_rTPL1qi"
        },
      "Somewhere In England": {
        "directory": base_dir + "\\SomewhereEngland\\dl",
        "link": "https://www.youtube.com/watch?v=tje9TprpfLg&list=PLmVVLc3PLstSTZ6d8_0VafYoqb3QQ_16u"
        },
      "Gone Troppo": {
        "directory": base_dir + "\\GoneTroppo\\dl",
        "link": "https://www.youtube.com/watch?v=zO8aH-7a8cY&list=PLYq_mcte9NvC5JKi3U-lI8H-iTAJw5oAm"
        },
      "Cloud Nine": {
        "directory": base_dir + "\\CloudNine\\dl",
        "link": "https://www.youtube.com/watch?v=tolATD8g-fk&list=PLmVVLc3PLstSL9JJCUOxMmaLqEdT6me5b"
        },
      "Brainwashed": {
        "directory": base_dir + "\\Brainwashed\\dl",
        "link": "https://www.youtube.com/watch?v=r8fFdc-karA&list=OLAK5uy_lf7G3bqyM8UcGQXXdWW259_SYSFCFtaik"
        }
      }


if __name__ == '__main__':
    import os
    for d in dirs:
        os.mkdir(os.path.join(base_dir, d))
    
    processing.download_albums(gh)