# Download Helper

Helper Python scripts used when downloading files.

## Script

### `make_batchlist.py`

Makes batch list used with youtube-dl. Some might prefer to used this instead of downloading directly through the `youtube_d` import with Python.
Example of usage:

`youtube-dl -f "bestaudio/best" -v -x --audio-format vorbis --audio-quality 0 --batch-file batchlist.txt -o "Files/File_%(autonumber)1d.%(ext)s"`

Downloads from URLs in the batch list and outputs them to the folder `Files/` path.
