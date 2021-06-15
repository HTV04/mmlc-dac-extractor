#!/usr/bin/env python3

# Disney Afternoon Collection Extractor v1.3.0
# By HTV04

# IMPORTANT: This script is currently only compatible with v1.0.0.42 of the Windows version of the game

# iNES Headers
HEADERS = [
    b'\x4E\x45\x53\x1A\x08\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'
]

# Offsets for each game's ROM in the executable
OFFSETS = [
    {'PRG': [0x7F2F30, 0x40000], 'CHA': None},
    {'PRG': [0x832F30, 0x40000], 'CHA': None},
    {'PRG': [0x792F30, 0x20000], 'CHA': [0x772F30, 0x20000]},
    {'PRG': [0x7B2F30, 0x20000], 'CHA': None},
    {'PRG': [0x7D2F30, 0x20000], 'CHA': None},
    {'PRG': [0x872F30, 0x40000], 'CHA': None}
]

# Game names
GAMES = [
    'Chip \'n Dale - Rescue Rangers',
    'Chip \'n Dale - Rescue Rangers 2',
    'Darkwing Duck',
    'DuckTales',
    'DuckTales 2',
    'TaleSpin'
]

if __name__ == '__main__':
    f = open("capcom_disney_afternoon.exe", "rb")
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
        
        out = open(GAMES[i] + " (Disney Afternoon Collection).nes", "wb")
        
        try:
            out.write(game)
        finally:
            out.close()
