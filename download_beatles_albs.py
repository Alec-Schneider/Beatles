# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 08:48:00 2020

@author: Alec
"""
import processing
import os

base_dir = 'C:\\Users\\Alec\\MyPython\\Beatles\\Beatles'


down_dir = {
    "Sgt. Pepper's Lonely Hearts Club": {
        'directory': os.path.join(base_dir, 'SgtPepper\mp4'),
        'link': 'https://www.youtube.com/watch?v=VtXl8xAPAtA&list=PL3PhWT10BW3VDM5IcVodrdUpVIhU8f7Z-'
        },
    "Rubber Soul": {
        'directory': os.path.join(base_dir, 'RubberSoul\mp4'),
        'link': "https://www.youtube.com/watch?v=kfSQkZuIx84&list=OLAK5uy_lvTG69VbZm3r3r9crRBvT1Tj305YEbuaM"
        },
    "The White Album": {
        'directory': os.path.join(base_dir, 'WhiteAlbum\mp4'),
        'link': 'https://www.youtube.com/watch?v=0ArlUSVDQIw&list=PLycVTiaj8OI80AsTGjYJAPi7-i8kTH-Bq'
        },
    "Let it Be": {
        'directory': os.path.join(base_dir, 'LetItBe\mp4'),
        'link': "https://www.youtube.com/watch?v=cLQox8e9688&list=PLycVTiaj8OI-aOPBmpwUlhQp83Puf0hLX"
        },
    "Help!": {
        'directory': os.path.join(base_dir, 'Help!\mp4'),
        'link': "https://www.youtube.com/watch?v=MKUex3fci5c&list=PLycVTiaj8OI9JtydS7uKMO1FGl8UDBmcZ"
        },
    "Revolver": {
        'directory': os.path.join(base_dir, 'Revolver\mp4'),
        'link': "https://www.youtube.com/watch?v=l0zaebtU-CA&list=PLkLimRXN6NKyRHpZeZEoc8sz73S1-ddvX"
        },
    "A Hard Day's Night": {
        'directory': os.path.join(base_dir, 'HardDaysNight\mp4'),
        'link': "https://www.youtube.com/watch?v=zx2TFk0vh1I&list=PLycVTiaj8OI-HjTjakWPpJO9Y6kh1icp2"
        },
    "Please Please Me": {
        'directory': os.path.join(base_dir, 'PleasePleaseMe\mp4'),
        'link': "https://www.youtube.com/watch?v=oxwAB3SECtc&list=PLycVTiaj8OI9COuVDJdw_RdBWy11ALc4T"
        },
    "Magical Mystery Tour": {
        'directory': os.path.join(base_dir, 'MagicalMysteryTour\mp4'),
        'link': "https://www.youtube.com/watch?v=l8WMGBuNaus&list=PLycVTiaj8OI8F5vZlwv4NnvGwc84ITnW2"
        },
    "Beatles For Sale": {
        'directory': os.path.join(base_dir, 'BeatlesForSale\mp4'),
        'link': "https://www.youtube.com/watch?v=YgFo9STa70E&list=PLycVTiaj8OI-DkxXKgnI5w2PKgUKoPLQ8"
        },
    "With The Beatles": {
        'directory': os.path.join(base_dir, 'WithTheBeatles\mp4'),
        'link': "https://www.youtube.com/watch?v=UVKU6SevefY&list=PLycVTiaj8OI-XRoKhxMmBhnsefIc77M2_"
        },
    "Yellow Submarine": {
        'directory': os.path.join(base_dir, 'YellowSubmarine\mp4'),
        'link': "https://www.youtube.com/watch?v=ztHxu-13UqI&list=PLycVTiaj8OI-Ob2F_f7E7mq6XDfeYTYOP"
        }
    }

        
if __name__ == '__main__':
    processing.download_albums(down_dir)
    
    
