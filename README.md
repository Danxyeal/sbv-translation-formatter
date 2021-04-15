# SBV File Translation Formatter
## WHAT
This script ensures the correct formatting is kept for sbv text after it is passed through a translator such as Google Translate or DeepL. It does not handle the translation because that would need to be done using an API, that costs per use.
## HOW
Note: Youtube Studio outputs sbv files for downloading subtitles - it is similar to srt or vtt.
1. Place two files in the directory with the script: one called "source.sbv" another called "target.sbv".
2. Run `python sbv-tf.py <name you want>`
3. Script will output correctly formatted sbv with the name you provided ready for importing into Youtube Studio.
