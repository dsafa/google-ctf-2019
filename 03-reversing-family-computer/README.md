# Description
## Home Computer
Label: forensics

Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."

Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.

So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.

# Solution
This attachment is a zip file containing a `family.ntfs` and `note.txt` file. Opening the `family.ntfs` file in something like 7zip shows the contents of a windows filesystem. Most of the files are empty, but we if navigate to `Users/Family/Documents` there is a file called `credentials.txt`. Opening the text file shows `I keep pictures of my credentials in extended attributes.`. Searching for ntfs extended attributes did not give much information but I knew there was something called `alternate data streams`, so maybe it meant those. Checking the data streams was easy with powershell
```ps
Get-Item credentials.txt -stream *
```
With that command, we can see that there is in fact another steam called `FILE0`. We can then extract the steam contents into a .png file which reveals the flag `CTF{congratsyoufoundmycreds}`

The script `extract-stream.ps1` will extract the image from the file.