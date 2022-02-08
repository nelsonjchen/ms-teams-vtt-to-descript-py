import sys

import webvtt

import re


def process_vtt(path):
    for caption in webvtt.read(path):
        speaker = "Unknown"
        speaker_search = re.search('<v (.+?)>', caption.raw_text)
        if speaker_search:
            speaker = speaker_search[1]
        print(f"{speaker}: {caption.text}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_vtt(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
