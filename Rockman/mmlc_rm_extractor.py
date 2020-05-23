#!/usr/bin/env python

# Mega Man Legacy Collection NES ROM Extractor v1.2.1R
# By HTV04

# IMPORTANT: This script is only compatible with v1.1.1.29 of the Windows version of the game.

# Based on anpage's script: https://gist.github.com/anpage/b895a34efb0bf1e4a9a4f52228067fa8

# iNES Headers for Rockman 1-6
HEADERS = [b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x10\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x20\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x20\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00']

# Offsets for each game's ROM in the .exe file
OFFSETS = [{'PRG': [0x512230, 0x20000], 'CHA': None},
           {'PRG': [0x2F20F0, 0x40000], 'CHA': None},
           {'PRG': [0x332130, 0x40000], 'CHA': [0x372130, 0x20000]},
           {'PRG': [0x392170, 0x80000], 'CHA': None},
           {'PRG': [0x4121B0, 0x40000], 'CHA': [0x4521B0, 0x40000]},
           {'PRG': [0x4921F0, 0x80000], 'CHA': None}]

if __name__ == '__main__':
    # Read in entire .exe file
    f = open("Proteus.exe", "rb")
    try:
        exe = f.read()
    finally:
        f.close()

    for i, game in enumerate(HEADERS):
        for section in ['PRG', 'CHA']:
            if OFFSETS[i][section]:
                start = OFFSETS[i][section][0]
                size = OFFSETS[i][section][1]
                end = start + size
                game += exe[start:end]
        if i == 0:
            out = open("Rockman.nes", "wb")
        if i == 1:  
            out = open("Rockman 2 - Dr Wily no Nazo.nes", "wb")
        if i == 2:  
            out = open("Rockman 3 - Dr Wily no Saigo!.nes", "wb")
        if i == 3:  
            out = open("Rockman 4 - Aratanaru Yabou!!.nes", "wb")
        if i == 4:  
            out = open("Rockman 5 - Blues no Wana!.nes", "wb")
        if i == 5:  
            out = open("Rockman 6 - Shijou Saidai no Tatakai!!.nes", "wb")
        try:
            out.write(game)
        finally:
            out.close()
