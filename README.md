# MMLC-ROM-Extractor
Extracts Mega Man 1-6 ROMs from Mega Man Legacy Collection (MMLC) (Windows only).
Based on anpage's script: https://gist.github.com/anpage/b895a34efb0bf1e4a9a4f52228067fa8

## How to use
- Make sure the latest version of Python 3 is installed at https://python.org.
- Place "mmlc_mm_extractor.py" in the same direcotry as the MMLC executable (Proteus.exe).
  - **IMPORTANT:** Make sure that the Proteus.exe version is "v1.1.1.29" (you can check this in the file's properties).
  - For good measure, verify the integrity of your MMLC installation via Steam.
- Run the script. ROMs named Mega Man followed by their respective numbers (except for the first Mega Man, which won't be followed by a number) will appear in the same directory, followed by a .nes extension.
- These ROMs can be played in NES emulators.

## Q&A
### Will this modify MMLC in any way?
Not at all! The MMLC executable will be completely unaffected after the script is run.

### Are the ROMs identical to the original games?
Other than all references to Nintendo being removed, the ROMs are identical.

### Are the ROMs compatible with ROM hacks?
Unfortunately, due to the changes I mentioned before, the ROMs won't work correctly with ROM hacks. However, I included an .ips patch for Mega Man 2 that makes it identical to the original game (with Nintendo references), which in turn makes the game compatible with ROM hacks for it. I plan to add more patches for the other Mega Man games later.

### There's a bug with the script.
Post an issue describing the problem and I'll try to fix it. **Please elaborate.**

### Help! An update released for MMLC and the script doesn't output valid ROMs anymore!
This is probably due to the offsets for the ROMs shifting. No worries, just post an issue and I'll try to fix it. I'll also add the first and last hex rows for each game later, in case you would like to try and find them.

## To-do
- Add another script for Rockman ROMs (too lazy right now).
- Add patches for other Mega Man and Rockman ROMs.
