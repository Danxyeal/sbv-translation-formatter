import sys
import os.path

SFN = 'source.sbv'
TFN = 'target.sbv'
if os.path.isfile(SFN) and os.path.isfile(TFN):
    with open('source.sbv') as f:
        source_text = f.read()

    with open('target.sbv') as f:
        target_text = f.read()
else:
    print('Files, "source.sbv" or "target.sbv" was not found. Exiting..')

print(source_text)
