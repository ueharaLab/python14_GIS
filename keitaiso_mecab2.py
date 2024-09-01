import re
import sys
import MeCab
import pickle
import pandas as pd
import unicodedata
import codecs
    
fortravel_df = pd.read_csv('fortravel_flavor_texture.csv', encoding='ms932', sep=',',skiprows=0)

local_area=[]
for i,ft in fortravel_df.iterrows():    
    area = fortravel_df['area']
    area = area.split('(')[0]
    if '・' in area:
        area=area.split('・')[0]
    local_area.append([area])
fortravel_df['local_area'] =  local_area

with open('fortravel_flavor_texture2.pickle', 'wb') as ds:
    pickle.dump(fortravel_df, ds)




