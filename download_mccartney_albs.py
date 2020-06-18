# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:44:06 2020

@author: Alec
"""


import processing


base_dir = 'C:\\Users\\Alec\\MyPython\\Beatles\\mccartney'

dirs = ["McCartney", "Ram", "WildLife", "RedRoseSpeedway",
        "BandOnTheRun", "VenusAndMars", "SpeedOfSound",
        "LondonTown", "BackToTheEgg", "McCartney2",
        "TugOfWar", "PipesOfPeace", "RegardsToBroadStreet",
        "PressToPlay", "ChobaBCccp", "FlowersInTheDirt",
        "OffTheGround", "FlamingPie", "DrivingRain",
        "ChaosAndCreation", "MemoryAlmostFull", "New",
        "EgyptStation"
        ]

mcc ={
      "McCartney": {
        'directory': base_dir + "\\McCartney\\dl",
        "link": "https://www.youtube.com/watch?v=WrRCkQEw9Dk&list=PLF8D48517CE3EDCDF"
        },
      "Ram": {
        'directory': base_dir + "\\Ram\\dl",
        "link": "https://www.youtube.com/watch?v=OEs7rnICUGo&list=PLDqq8QTES5DPhFr7lLrs_OhEqvNqxNf8t"
        },
      "Wild Life": {
        'directory': base_dir + "\\WildLife\\dl",
        "link": "https://www.youtube.com/watch?v=caUwVC4MPFM&list=PLAACDEDF3E0339670"
        },
      "Red Rose Speedway": {
        'directory': base_dir + "\\RedRoseSpeedway\\dl",
        "link": "https://www.youtube.com/watch?v=7LvG5h1Z3Tg&list=PLA727A30DFD111A71"
        },
      "Band On The Run": {
        'directory': base_dir + "\\BandOnTheRun\\dl",
        "link": "https://www.youtube.com/watch?v=RjlvdcBAKdg&list=PL1LaNBcZk8V_VpnZuMyV_FlSyCNLlJc7G"
        },
      "Venus And Mars": {
        'directory': base_dir + "\\VenusAndMars\\dl",
        "link": "https://www.youtube.com/watch?v=NgmJktHe_XQ&list=PLrv5a_5drVgT6kEK-hHQYs-UaE9LyM7F-"
        },
      "Wings At The Speed Of Sound": {
        'directory': base_dir + "\\SpeedOfSound\\dl",
        "link": "https://www.youtube.com/watch?v=re61B8sKQWk&list=OLAK5uy_kO_5IMfTd0U2MQJEBCDef-ZfSrabA8WVk"
        },
      "London Town": {
        'directory': base_dir + "\\LondonTown\\dl",
        "link": "https://www.youtube.com/watch?v=5pvEOnnPjcw&list=PLi_eUMd6th2J5i8YDzNK1F0jffk9K8tr0"
        },
      "Back To The Egg": {
        'directory': base_dir + "\\BackToTheEgg\\dl",
        "link": "https://www.youtube.com/watch?v=UwtIZzOZbYk&list=OLAK5uy_mr_qBql4bcdeEe6TthXU8IS0yijo-brxY"
        },
      "McCartney 2": {
        'directory': base_dir + "\\McCartney2\\dl",
        "link": "https://www.youtube.com/watch?v=QX7NSdyr_4U&list=PLp8sncEUV-K7t-rt_Vgpmx2V0CV6RyGC5"
        },
      "Tug Of War": {
        'directory': base_dir + "\\TugOfWar\\dl",
        "link": "https://www.youtube.com/watch?v=X8eOTg1N_NI&list=OLAK5uy_kMuk0tK7-Ig9quNDZQRTfyBlAsC72P07w"
        },
      "Pipes Of Peace": {
        'directory': base_dir + "\\PipesOfPeace\\dl",
        "link": "https://www.youtube.com/watch?v=tP7ZtMLWxb4&list=PLXxwWIsQCmglE1zap0aNQqpQnbCkCohy9"
        },
      "Give My Regards To Broad Street": {
        'directory': base_dir + "\\RegardsToBroadStreet\\dl",
        "link": "https://www.youtube.com/watch?v=zEpqGPXBjD4&list=PL2aXYk9zKd22wm0umoFTLdJC7nMXDTT6p"
        },
      "Press To Play": {
        'directory': base_dir + "\\PressToPlay\\dl",
        "link": "https://www.youtube.com/watch?v=gxH6Kgul-Ss&list=OLAK5uy_kQqU81BqIIVOnNfm3lRI8bcdNwDFnZZZo"
        },
      "Choba B Cccp": {
        'directory': base_dir + "\\ChobaBCccp\\dl",
        "link": "https://www.youtube.com/watch?v=tFAT7nXYErk&list=OLAK5uy_n1BsnlALWXwR3FOo4cvT8S06pOtvvw_q0"
        },
      "Flowers In The Dirt": {
        'directory': base_dir + "\\FlowersInTheDirt\\dl",
        "link": "https://www.youtube.com/watch?v=6Ldqa29J3Y4&list=PLjpdZVAwBy004vwTpOt_tWjy0xNCVjun2"
        },
      "Off The Ground": {
        'directory': base_dir + "\\OffTheGround\\dl",
        "link": "https://www.youtube.com/watch?v=76zCEkqYy4I&list=OLAK5uy_n28Rz446O6iInNOgZmDNZNW2ZPFjIZ0B0"
        },
      "FlamingPie": {
        'directory': base_dir + "\\FlamingPie\\dl",
        "link": "https://www.youtube.com/watch?v=Q4qObxQL4x0&list=OLAK5uy_lf2Ris1H5-ZRrOC9TepxQL0q6CddAtyeI"
        },
      "Driving Rain": {
        'directory': base_dir + "\\DrivingRain\\dl",
        "link": "https://www.youtube.com/watch?v=JPSYGtskelw&list=PLED43AD334A2D5C0B"
        },
      "Chaos And Creation In The Backyard": {
        'directory': base_dir + "\\ChaosAndCreation\\dl",
        "link": "https://www.youtube.com/watch?v=KMaQtLMbzz8&list=OLAK5uy_lTjpalcx2wY_wX40c2TfpEiNlbLLdXFP4"
        },
      "Memory Almost Full": {
        'directory': base_dir + "\\MemoryAlmostFull\\dl",
        "link": "https://www.youtube.com/watch?v=IHyy-REXkB0&list=OLAK5uy_mrO1qYxPA2aNvvPzBJWtBKGcq7jA8rvWA"
        },
      "New": {
        'directory': base_dir + "\\New\\dl",
        "link": "https://www.youtube.com/watch?v=0lZ4Ke9vTng&list=PL-Mb0HW9SxmgiHdNPfH_hVr88sB9JjnvP"
        },
      "Egypt Station": {
        'directory': base_dir + "\\EgyptStation\\dl",
        "link": "https://www.youtube.com/watch?v=BLHeohkkuMo&list=PLoDV1tSqTU2yDObJcfLTK3-nDyTKiZo-U"
        }   
      }


if __name__ == '__main__':
    import os
    for d in dirs:
        os.mkdir(os.path.join(base_dir, d))
    
    processing.download_albums(mcc)
    