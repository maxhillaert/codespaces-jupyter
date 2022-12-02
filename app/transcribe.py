"""Blabl"""
#%%
import pathlib
from util.download import download_if_not_exist


working_dir = pathlib.Path().resolve()

URL = 'https://media.blubrry.com/takeituneasy/content.blubrry.com/takeituneasy/lex_ai_andrej_karpathy.mp3'

download_if_not_exist(URL, f'{working_dir}/data/lex_ai_andrej_karpathy.mp3')

#%%s
