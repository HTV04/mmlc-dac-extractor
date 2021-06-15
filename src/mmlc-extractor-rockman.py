#!/usr/bin/env python3

# Mega Man Legacy Collection Extractor - Rockman v1.3.0
# By HTV04

# IMPORTANT: This script is only compatible with v1.1.1.29 of the Windows version of the game

# iNES Headers
HEADERS = [
    b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x10\x10\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x20\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x10\x20\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00'
]

# Offsets for each game's ROM in the executable
OFFSETS = [
    [0x512230, 0x20000],
    [0x2F20F0, 0x40000],
    [0x332130, 0x60000],
    [0x392170, 0x80000],
    [0x4121B0, 0x80000],
    [0x4921F0, 0x80000]
]

# Game names
GAMES = [
    "Rockman",
    "Rockman 2 - Dr Wily no Nazo",
    "Rockman 3 - Dr Wily no Saigo!",
    "Rockman 4 - Aratanaru Yabou!!",
    "Rockman 5 - Blues no Wana!",
    "Rockman 6 - Shijou Saidai no Tatakai!!"
]

if __name__ == '__main__':
    f = open("Proteus.exe", "rb")
    try:
        exe = f.read()
    finally:
        f.close()

    for i, game in enumerate(HEADERS):
        start = OFFSETS[i][0][0]
        size = OFFSETS[i][1][1]
        end = start + size
        game += exe[start:end]
        
        out = open(GAMES[i] + ".nes", "wb")
        
        try:
            out.write(game)
        finally:
            out.close()
