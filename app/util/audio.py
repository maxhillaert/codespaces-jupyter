"""mp3 utilities"""

from pydub import AudioSegment

class Clip:
    """Clip class
    Args:
        start_min (int): start minute
        start_sec (int): start second
        end_min (int): end minute
        end_sec (int): end second
    """
    def __init__(self, start_min: int, start_sec: int, end_min: int, end_sec: int):
        self.start_min = start_min
        self.start_sec = start_sec
        self.end_min = end_min
        self.end_sec = end_sec

    def __str__(self):
        return f"Clip({self.start_min}:{self.start_sec} - {self.end_min}:{self.end_sec})"

    def __repr__(self):
        return self.__str__()


def cut_mp3(
        mp3_path: str,
        clip: Clip,
        output_path: str):
    """Cut a mp3 file
    Args:
        mp3_path (str): mp3 file path
        clip (Clip): clip
        output_path (str): output path
    """

    # Time to miliseconds
    start_time = clip.start_min*60*1000+clip.start_sec*1000
    end_time = clip.end_min*60*1000+clip.end_sec*1000

    # Opening file and extracting segment
    song = AudioSegment.from_mp3(mp3_path)
    extract = song[start_time:end_time]

    # Saving
    extract.export(output_path, format="mp3")
