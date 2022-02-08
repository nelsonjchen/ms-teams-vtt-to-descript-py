import sys

import webvtt

import re

from gooey import Gooey, GooeyParser



def process_vtt(path):
    for caption in webvtt.read(path):
        speaker = "Unknown"
        speaker_search = re.search('<v (.+?)>', caption.raw_text)
        if speaker_search:
            speaker = speaker_search[1]
        print(f"{speaker}: {caption.text}")


@Gooey
def main():
    parser = GooeyParser(description="Microsoft VTT to Descript Transcript Helper")
    parser.add_argument('filename', widget="FileChooser")
    args = parser.parse_args()
    if args:
        process_vtt(parser.filename)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
