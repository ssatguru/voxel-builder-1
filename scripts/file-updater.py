"""
    # File Updater
    # CMD: file-updater.py <path-to-vox-file>
"""

import os
import sys


def patch360(path): # add ',true' to every line
    with open(path.replace('.vox', '-new.vox'), 'w') as outfile:
        with open(path, 'r') as infile:
            for line in infile:
                if line.startswith('#'):
                    outfile.write(line) # ignored
                elif line.startswith('data:'):
                    outfile.write(line) # ignored
                else:
                    outfile.write(line.rstrip('\n') + ',true\n')


def patcher(path):
    with open(path, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.startswith('#'):
                pass
            elif line.startswith('data:'):
                pass
            else:
                # detect 3.6.0
                if line.endswith(',true') or line.endswith(',false'):
                    print('File format is already up-to-date.')
                    sys.exit()
                else: # apply 3.6.0
                    patch360(path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('file-updater.py <path-to-vox-file>')
        sys.exit()
    path = sys.argv[1]

    if os.path.isfile(path):
        patcher(path)
    else:
        print('Error: File not exist')
