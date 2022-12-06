"""Blabl"""
# %%

import pathlib
from util.download import download_if_not_exist
from util.audio import cut_mp3, Clip
from util.transcription import deepgram_transcribe_upload_to_file


working_dir = pathlib.Path().resolve()
data_dir = working_dir / "data"
data_dir.mkdir(exist_ok=True)
audio_dir = data_dir / "audio"
audio_dir.mkdir(exist_ok=True)
transcript_dir = data_dir / "transcript"
transcript_dir.mkdir(exist_ok=True)


URL = 'https://media.blubrry.com/takeituneasy/content.blubrry.com/takeituneasy/lex_ai_andrej_karpathy.mp3'

audio_file = audio_dir / 'lex_ai_andrej_karpathy.mp3'
download_if_not_exist(URL, audio_file)

# %%s

audio_file_cut = audio_dir / 'lex_ai_andrej_karpathy_cut.mp3'
# cut_mp3(audio_file,
#         Clip(20, 0, 40, 0),
#         audio_file_cut)


# %%s

transcript_deepgram_dir = transcript_dir / "deepgram"
transcript_deepgram_dir.mkdir(exist_ok=True)

await deepgram_transcribe_upload_to_file(audio_file, transcript_deepgram_dir /  'lex_ai_andrej_karpathy.json')


print("Done")


# %%
