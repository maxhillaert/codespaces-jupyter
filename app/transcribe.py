"""Blabl"""
#%%
from util.download import download_if_not_exist


URL = 'https://media.blubrry.com/takeituneasy/content.blubrry.com/takeituneasy/lex_ai_andrej_karpathy.mp3'

download_if_not_exist(URL, '../data/lex_ai_andrej_karpathy.mp3')

#%%s
