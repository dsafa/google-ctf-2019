This attachment is a zip file containing a `family.ntfs` and `note.txt` file. Opening the `family.ntfs` file in something like 7zip shows the contents of a windows filesystem. Most of the files are empty, but we if navigate to `Users/Family/Documents` there is a file called `credentials.txt`. Opening the text file shows `I keep pictures of my credentials in extended attributes.`. Searching for ntfs extended attributes did not give much information but I knew there was something called `alternate data streams`, so maybe it meant those. Checking the data streams was easy with powershell
```ps
Get-Item credentials.txt -stream *
```
With that command, we can see that there is in fact another steam called `FILE0`. We can then extract the steam contents into a .png file which reveals the flag `CTF{congratsyoufoundmycreds}`

The script `extract-stream.ps1` will extract the image from the file.