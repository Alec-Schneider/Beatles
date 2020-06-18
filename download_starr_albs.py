# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:40:34 2020

@author: Alec
"""

import processing

base_dir = 'C:\\Users\\Alec\\MyPython\\Beatles\\starr'

# =============================================================================
# dirs = ["SentimentalJourney", "BeaucoupsOfBlues", "Ringo",
#         "GoodnightVienna", "RingosRotogravure", "RingoThe4th",
#         "BadBoy", "SmellTheRoses", "OldWave", "TimeTakesTime",
#         "VerticalMan", "SantaClaus","RingoRama", "ChooseLove",
#         "Liverpool8", "YNot", "Ringo2012",
#         "PostcardsParadise", "GiveMoreLove", "WhatsMyName"
#         ]
# =============================================================================
dirs = ["SantaClaus","RingoRama", "ChooseLove",
        "Liverpool8", "YNot", "Ringo2012",
        "PostcardsParadise", "GiveMoreLove", "WhatsMyName"
        ]

rs = {
      "Sentimental Journey": {
        'directory': base_dir + "\\SentimentalJourney\\dl",
        "link": "https://www.youtube.com/watch?v=NLkGshFAglY&list=PLhhLsYaqc0dEYiNGluzGdTg5cRToyAqJe"
        },
      "Beaucoups Of Blues": {
        'directory': base_dir + "\\BeaucoupsOfBlues\\dl",
        "link": "https://www.youtube.com/watch?v=xLz9_aayHfc&list=OLAK5uy_nm_YgVkoaiWzXaHBXl_x2qIUSs_O-ykQk"
        },
      "Ringo": {
        'directory': base_dir + "\\Ringo\\dl",
        "link": "https://www.youtube.com/watch?v=mZ4EmA5X-PQ&list=PLCjLGgbfOxrzZSGPczYsCOaSclYGYquJw"
        },
      "Goodnight Vienna": {
        'directory': base_dir + "\\GoodnightVienna\\dl",
        "link": "https://www.youtube.com/watch?v=aeZfsbeBl9o&list=PLn0EQ6e8pil9cXodxjB-Q5ubtKOcrzw0f"
        },
      "Ringo's Rotogravure": {
        'directory': base_dir + "\\RingosRotogravure\\dl",
        "link": "https://www.youtube.com/watch?v=qOeOLKKt2PA&list=OLAK5uy_mhgfjF8oB9nUAi5RGDBFOPRH9vtUtM1Og"
        },
      "Ringo The 4th": {
        'directory': base_dir + "\\RingoThe4th\\dl",
        "link": "https://www.youtube.com/watch?v=hjmV0bKzUz4&list=OLAK5uy_lTOnNFYy16tWkRDBdGivL26D2bwX3bqbQ"
        },
      "Bad Boy": {
        'directory': base_dir + "\\BadBoy\\dl",
        "link": "https://www.youtube.com/watch?v=Fd2BQK4I0ws&list=PL7C3C0039597B5677"
        },
      "Stop And Smell The Roses": {
        'directory': base_dir + "\\SmellTheRoses\\dl",
        "link": "https://www.youtube.com/watch?v=FFFs9GpTURw&list=PL1C37C7CD85E85C27"
        },
      "Old Wave": {
        'directory': base_dir + "\\OldWave\\dl",
        "link": "https://www.youtube.com/watch?v=s3YeEAiXmgk&list=PLZCDbeZmzy0PZ_3ksv1PGeb1CxbAE--2p"
        },
      "Time Takes Time": {
        'directory': base_dir + "\\TimeTakesTime\\dl",
        "link": "https://www.youtube.com/watch?v=k_S77XSXDe8&list=OLAK5uy_n8kzQ4IoxMRKeEiWhBhHWHf-oQQkq-XEo"
        },
      "Vertical Man": {
        'directory': base_dir + "\\VerticalMan\\dl",
        "link": "https://www.youtube.com/watch?v=WEe9nmT9N1E&list=OLAK5uy_lMpGT0sV0JxB2usSFpnqcGiks0sdTvndk"
        },
      "I Wanna Be Santa Claus": {
        'directory': base_dir + "\\SantaClaus\\dl",
        "link": "https://www.youtube.com/watch?v=PQq0Wy7VKxk&list=OLAK5uy_kH9GzxxI8ZfizabXshunEjExk2od4i0GA"
        },
      "Ringo Rama": {
        'directory': base_dir + "\\RingoRama\\dl",
        "link": "https://www.youtube.com/watch?v=8UAD4Vq-U3Q&list=OLAK5uy_nDYIJwmZjAvqdfWEO0KzCSWu6qWa6ammU"
        },
      "Choose Love": {
        'directory': base_dir + "\\ChooseLove\\dl",
        "link": "https://www.youtube.com/watch?v=DWLDKiKQ9_8&list=OLAK5uy_kH-HVGBXpLWbDTiDxGwY8ZnVeJRgDT_k4"
        },
      "Liverpool 8": {
        'directory': base_dir + "\\Liverpool8\\dl",
        "link": "https://www.youtube.com/watch?v=emDgKWih9H0&list=OLAK5uy_lr7HsRR8_Cja_IrnZGm-K-9-rprQMFxIE"
        },
      "Y Not": {
        'directory': base_dir + "\\YNot\\dl",
        "link": "https://www.youtube.com/watch?v=YS4bKPJAfWU&list=PLDF9C2358A9F1AFE7"
        },
      "Ringo 2012": {
        'directory': base_dir + "\\Ringo2012\\dl",
        "link": "https://www.youtube.com/watch?v=HbOj5AIvcOA&list=PLn0EQ6e8pil-WAyTX6lPtDoXnKhdG4UDm"
        },
      "Postcards From Paradise": {
        'directory': base_dir + "\\PostcardsParadise\\dl",
        "link": "https://www.youtube.com/watch?v=ZCRsDd_GUKg&list=OLAK5uy_m2f0uG_el-AoQks6I8cDM-IiAooiFCUpo"
        },
      "Give More Love": {
        'directory': base_dir + "\\GiveMoreLove\\dl",
        "link": "https://www.youtube.com/watch?v=QeM1fRcqWl8&list=OLAK5uy_mF4oHXobFNpuYbtsJyu3Ig6KcW2BGzX2E"
        },
      "What's My Name": { 
        'directory': base_dir + "\\WhatsMyName\\dl",
        "link": "https://www.youtube.com/watch?v=IEUtRlopbS4&list=OLAK5uy_nAGgai5wLWymtpzo-OlHsJyNV168lv8bk"
        },
      "": {
        'directory': base_dir + "\\\\dl",
        "link": ""
        }      
      }


rs2 = {
       "I Wanna Be Santa Claus": {
        'directory': base_dir + "\\SantaClaus\\dl",
        "link": "https://www.youtube.com/watch?v=PQq0Wy7VKxk&list=OLAK5uy_kH9GzxxI8ZfizabXshunEjExk2od4i0GA"
        },
      "Ringo Rama": {
        'directory': base_dir + "\\RingoRama\\dl",
        "link": "https://www.youtube.com/watch?v=8UAD4Vq-U3Q&list=OLAK5uy_nDYIJwmZjAvqdfWEO0KzCSWu6qWa6ammU"
        },
      "Choose Love": {
        'directory': base_dir + "\\ChooseLove\\dl",
        "link": "https://www.youtube.com/watch?v=DWLDKiKQ9_8&list=OLAK5uy_kH-HVGBXpLWbDTiDxGwY8ZnVeJRgDT_k4"
        },
      "Liverpool 8": {
        'directory': base_dir + "\\Liverpool8\\dl",
        "link": "https://www.youtube.com/watch?v=emDgKWih9H0&list=OLAK5uy_lr7HsRR8_Cja_IrnZGm-K-9-rprQMFxIE"
        },
      "Y Not": {
        'directory': base_dir + "\\YNot\\dl",
        "link": "https://www.youtube.com/watch?v=YS4bKPJAfWU&list=PLDF9C2358A9F1AFE7"
        },
      "Ringo 2012": {
        'directory': base_dir + "\\Ringo2012\\dl",
        "link": "https://www.youtube.com/watch?v=HbOj5AIvcOA&list=PLn0EQ6e8pil-WAyTX6lPtDoXnKhdG4UDm"
        },
      "Postcards From Paradise": {
        'directory': base_dir + "\\PostcardsParadise\\dl",
        "link": "https://www.youtube.com/watch?v=ZCRsDd_GUKg&list=OLAK5uy_m2f0uG_el-AoQks6I8cDM-IiAooiFCUpo"
        },
      "Give More Love": {
        'directory': base_dir + "\\GiveMoreLove\\dl",
        "link": "https://www.youtube.com/watch?v=QeM1fRcqWl8&list=OLAK5uy_mF4oHXobFNpuYbtsJyu3Ig6KcW2BGzX2E"
        },
      "What's My Name": { 
        'directory': base_dir + "\\WhatsMyName\\dl",
        "link": "https://www.youtube.com/watch?v=IEUtRlopbS4&list=OLAK5uy_nAGgai5wLWymtpzo-OlHsJyNV168lv8bk"
        }    
      }


if __name__ == '__main__':
    import os
    # for d in dirs:
    #     os.mkdir(os.path.join(base_dir, d))
    
    # processing.download_albums(rs)
    # os.mkdir(os.path.join(base_dir, "SantaClaus"))
    processing.download_albums(rs2)
    