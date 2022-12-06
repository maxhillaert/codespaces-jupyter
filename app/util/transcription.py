"""Transcription Services"""
import json
from pathlib import Path
from deepgram import Deepgram

DEEPGRAM_API_KEY = '615a3e49d579e123e5ce17ba5a2c78e5f763576f'
deepgram_options = {'punctuate': True, 'diarize': True, 'ner': True, 'tier':'enhanced' , 'model': 'meeting'}

async def deepgram_transcribe_url_to_file( url:str, output_file: str):
    """Transcribe audio from a URL to a file
    Args:
        url (str): url of audio file
        output_file (str): output file
    """
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    
    response = await dg_client.transcription.prerecorded(source={'url': url}, options=deepgram_options)
    with open(output_file, 'w', encoding='UTF-8') as outfile:
        json.dump(response, outfile, indent=4)


async def deepgram_transcribe_upload_to_file(audio_file: Path, output_file: Path):
    """Transcribe audio from a file to a file

    Args:
        audio_file (str): audio file path
        output_file (str): output file path
    """
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    with open(audio_file, 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = await dg_client.transcription.prerecorded(source, options=deepgram_options)
        with open(output_file, 'w', encoding='UTF-8') as outfile:
            print(f"Writing to file: {output_file}")
            json.dump(response, outfile, indent=4)
        output_file_text = output_file.with_suffix('.txt')
        with open(output_file_text, 'w', encoding='UTF-8') as outfile:
            print(f"Writing to file: {output_file_text}"  )
            outfile.write(response['results']['channels'][0]['alternatives'][0]['transcript'])

