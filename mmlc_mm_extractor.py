#!/usr/bin/env python

# Program for extracting the NES roms of each Mega Man game in the Mega Man Legacy Collection for PC
# Original by anpage
# Modified by HTV04

# iNES Headers for Mega Man 1-6
HEADERS = [b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x10\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x20\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00']

# Offsets for each game's ROM in the .exe file
# v1.1.1.29         OFFSET     SIZE             OFFSET      SIZE
OFFSETS = [{'PRG': [0x2AEEB0, 0x20000], 'CHA': None},
           {'PRG': [0x8ED70, 0x40000], 'CHA': None},
           {'PRG': [0xCEDB0, 0x40000], 'CHA': [0x10EDB0, 0x20000]},
           {'PRG': [0x12EDF0, 0x80000], 'CHA': None},
           {'PRG': [0x1AEE30, 0x40000], 'CHA': [0x1EEE30, 0x40000]},
           {'PRG': [0x22EE70, 0x80000], 'CHA': None}]

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
          out = open("Mega Man.nes", "wb")
        else:  
          out = open("Mega Man " + str(i+1) + ".nes", "wb")
        try:
            out.write(game)
        finally:
            out.close()
