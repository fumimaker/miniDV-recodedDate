# miniDV-recodedDate

When I digitised my miniDV tapes, I didn't have the date data, so when I uploaded them to a service like Google Photos, they were displayed as being from 2025, even though they were from a long time ago, so I made a tool to fix this problem.

reference below (Japanese)

https://fumimaker.net/entry/2025/01/04/011516



The procedure is as follows.

- AVI video
- Rename the file name to the date and time. Execute rename.py (for those who need it)
- Compress and encode the AVI video using any tool you like.
- Write the shooting date and time to the mp4 exif. Execute search_and_setExif.py

Since the AVI container does not have EXIF, there is a problem when storing it in the modern mp4 container. Therefore, I made it AVI → AVI with date → mp4 encoding → mp4 with EXIF.

The reason for making it AVI with date is because it is easy to understand. It is also fine to make it AVI → mp4 encoding → EXIF writing. I did it this way because I wanted to save the AVI file on the HDD for archiving.

# Note

**As this is important video data,** please check that there are no problems with the operation before executing the script. **Be sure to copy it first** and execute it in a test directory.

# requirements

Operating environment

- MacOS, Linux
  -  For Windows...using WSL may be the easiest way. If there is demand, I will also make a PS version. Since it is subprocess, it should work on Windows if you fix the path...I have not confirmed that it works.
- Python 3.10.12
  - I think it will work for anything.
- exiftool
- mediainfo

# Description



## rename.py

This script will change the file name to the recorded date by referring to the recorded date recorded in the AVI file.

`python rename.py "/path/to/your/video"/dir`

## serch_and_setExif.py

Use serch_and_setExif.py to find AVI and MP4 videos with the same file name, and use exiftool to write the extracted recorded date using mediainfo. It doesn't matter whether it's an avc (h.264) or heif (h.265) container, as long as it's an MP4 container. You will need to have Exiftool installed.

`python serch_and_setExif.py "/path/to/your/video"`
