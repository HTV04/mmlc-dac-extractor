# MMLC-NES-ROM-Extractor (v1.2.1)
Extracts Mega Man 1-6 NES ROMs from the Mega Man Legacy Collection (Windows).
- Rockman 1-6 ROMs can also be extracted.

Based on anpage's script: https://gist.github.com/anpage/b895a34efb0bf1e4a9a4f52228067fa8

I made a modified version of their script because it was outdated.

Hashes for the ROMs can be found here, courtesy of niemand:
* Mega Man: https://datomatic.no-intro.org/?page=show_record&s=45&n=2847
* Mega Man 2: https://datomatic.no-intro.org/?page=show_record&s=45&n=2848
* Mega Man 3: https://datomatic.no-intro.org/?page=show_record&s=45&n=2849
* Mega Man 4: https://datomatic.no-intro.org/?page=show_record&s=45&n=2850
* Mega Man 5: https://datomatic.no-intro.org/?page=show_record&s=45&n=2851
* Mega Man 6: https://datomatic.no-intro.org/?page=show_record&s=45&n=2852

From here on, the Mega Man Legacy Collection will be referred to as the MMLC for simplicity.

## How to use
- Make sure the latest version of Python 3 is installed at https://python.org.
- Place "mmlc_mm_extractor.py" (or "mmlc_rm_extractor.py" if extracting Rockman ROMs) in the same directory as the MMLC executable (Proteus.exe).
  - **IMPORTANT:** Make sure that the Proteus.exe version is "v1.1.1.29" (you can check this in the file's properties).
  - For good measure, verify the integrity of your MMLC installation via Steam.
- Run the script. ROMs named Mega Man followed by their respective numbers (except for the first Mega Man, which won't be followed by a number) will appear in the same directory, followed by an .nes extension.
  - If using the Rockman extractor script, ROMs named Rockman followed by their respective numbers and subtitles (execpt for the first Rockman, which won't be followed by a number nor a subtitle) will appear in the same directory, followed by an .nes extension.
- These ROMs can be played in NES emulators.

## Q&A
### Why would I want to use this instead of just pirating the original games?
In the case of the Mega Man ROMs, they aren't identical to the original games. All references to Nintendo have been removed, among other unknown changes. In other words, they're perfect for a ROM collection.

The Rockman ROMs are identical to the original games, however, and a script is included for experimental reasons.

### Will this modify the MMLC in any way?
Not at all! The MMLC executable will be completely unaffected after the script is run.

### Are the MMLC ROMs compatible with ROM hacks?
No, the modified ROMs included with the MMLC are not compatible with ROM hacks. However, I included .ips patches that make the ROMs identical to the original games (with Nintendo references), which in turn makes the games compatible with ROM hacks for them. I would recommend making backup copies of the extracted ROMs before patching them, as there may be other changes to the ROMs that I am unaware of. You can apply the .ips using Lunar IPS https://fusoya.eludevisibility.org/lips/ (**beware that applying the patches directly without making backups will overwrite the original ROMs!**).

As for the Rockman ROMs, they are completely identical to the original games and don't need any patching whatsoever.

### There's a bug with the scripts/patches.
Post an issue describing the problem and I'll try to fix it. **Please elaborate.**

### Help! An update released for the MMLC and the script doesn't output valid ROMs anymore!
This is probably due to the offsets for the ROMs shifting. No worries, just post an issue and I'll try to fix it.

### ***Bonus:*** What's "data.pie?"
"data.pie" is an encrypted zip folder containing several assets for the MMLC. If you would like to access it (for example, if you want to use the box art), follow these steps:

**(NOTE: The following steps are intended to be done on Windows (10). I cannot guarantee the steps will the same for other operating systems.)**

- Download the latest version of 7-Zip here (the built-in extractor for Windows doesn't support passwords): https://www.7-zip.org/
- After installing 7-Zip, **copy the "data.pie" file in the MMLC directory to a different location**.
- Rename the **copied file** to "data.zip." Make sure you have file extensions enabled.
- Right-click on the zip file, and click on "7-Zip > Extract files..."
- Click "OK."
- When prompted, enter this password: P091uWEdwe4lI6StDNMNlkodPGvJ38bL3HW6t3BCMYdFi83FXKu7k0NsHP8caDKS
- Enjoy!
