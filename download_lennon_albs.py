# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:49:58 2020

@author: Alec
"""


import processing


base_dir = 'C:\\Users\\Alec\\MyPython\\Beatles\\Lennon'


jl = {
      "Wedding Album":{ 
          "directory": base_dir+"\\WeddingAlbum\\dl",
          "link": "https://www.youtube.com/watch?v=9QHmH-V99SM&list=PLAC0F5FDA7FC92C00"
          },
      "John Lennon/Plastic Ono Band":{ 
          "directory": base_dir+"\\PlasticOnoBand\\dl",
          "link": "https://www.youtube.com/watch?v=3D0nMzHjMR8&list=PL6ogdCG3tAWis8381V3_hT6zlRmOVKJ_u"
          },
      "Imagine":{ 
          "directory": base_dir+"\\Imagine\\dl",
          "link": "https://www.youtube.com/watch?v=5pQ9To3DMuo&list=PLr99rnVSBqGAVbJuudUbRFGl-S1PuYs-5"
          },
      "Some Time In New York City":{ 
          "directory": base_dir+"\\SomeTimeInNYC\\dl",
          "link": "https://www.youtube.com/watch?v=j5RuCEhHcG4&list=PL2L2BDLggO-C-nBI9u5CzGcvgVmEb6P3-"
          },
      "Mind Games":{ 
          "directory": base_dir+"\\MindGames\\dl",
          "link": "https://www.youtube.com/watch?v=QLeObvcUii4&list=PL2L2BDLggO-Dl-zPw6xJxdlD12QYzjtWG"
          },
      "Walls And Bridges":{ 
          "directory": base_dir+"\\WallsAndBridges\\dl",
          "link": "https://www.youtube.com/watch?v=UwMHT6g8-Oo&list=PL5AC2065044F4F910"
          },
      "Rock n Roll":{ 
          "directory": base_dir+"\\RocknRoll\\dl",
          "link": "https://www.youtube.com/watch?v=S8huF2Jgn4c&list=PLgYjFliLpyxlcDf_MXyWdOwB70CdUBVZ2"
          },
      "DoubleFantasy":{ 
          "directory": base_dir+"\\DoubleFantasy\\dl",
          "link": "https://www.youtube.com/watch?v=jWG9KAgD6UA&list=PLXxyvjuk1a2Hukb43sf7F5LsMT-uwbJu0"
          },
      "Milk And Honey":{ 
          "directory": base_dir+"\\MilkAndHoney\\dl",
          "link": "https://www.youtube.com/watch?v=SJgn68PA8X0&list=PLi_eUMd6th2In2WoMzTaP7eMo2VQWaaw0"
          }
      }

jl2 = {
       "Walls And Bridges":{ 
          "directory": base_dir+"\\WallsAndBridges\\dl",
          "link": "https://www.youtube.com/watch?v=oQKTLI7IWWE&list=PLAKBCdHlMy48Jxm0uYfgSLq4M7oiOzuTk"
          },
      "Rock n Roll":{ 
          "directory": base_dir+"\\RocknRoll\\dl",
          "link": "https://www.youtube.com/watch?v=S8huF2Jgn4c&list=PLgYjFliLpyxlcDf_MXyWdOwB70CdUBVZ2"
          },
      "DoubleFantasy":{ 
          "directory": base_dir+"\\DoubleFantasy\\dl",
          "link": "https://www.youtube.com/watch?v=jWG9KAgD6UA&list=PLXxyvjuk1a2Hukb43sf7F5LsMT-uwbJu0"
          },
      "Milk And Honey":{ 
          "directory": base_dir+"\\MilkAndHoney\\dl",
          "link": "https://www.youtube.com/watch?v=SJgn68PA8X0&list=PLi_eUMd6th2In2WoMzTaP7eMo2VQWaaw0"
          }
      }


if __name__ == '__main__':

    # processing.download_albums(jl) # Failed as album had removed videos
    processing.download_albums(jl2)
    