# Description
## FriendSpaceBookPlusAllAccessRedPremium.com
Label: reversing

Having snooped around like the expert spy you were never trained to be, you found something that takes your interest: "Cookie/www.FriendSpaceBookPlusAllAccessRedPremium.com"  But unbeknownst to you, it was only the  700nm Wavelength herring rather than a delicious cookie that you could have found.   It looks exactly like a credential for another system.  You find yourself in search of a friendly book to read.

Having already spent some time trying to find a way to gain more intelligence... and learn about those fluffy creatures, you (several)-momentarily divert your attention here.  It's a place of all the individuals in the world sharing large amounts of data with one another. Strangely enough, all of the inhabitants seem to speak using this weird pictorial language. And there is hot disagreement over what the meaning of an eggplant is.

But not much Cauliflower here.  They must be very private creatures.  SarahH has left open some proprietary tools, surely running this will take you to them.  Decipher this language and move forth!

# Solution
The attachment is zip containing a `program` file and a `vm.py` file. Looking at the files, it appears that there is a stack based virtual machine implemented in `vm.py` which runs emoji based code located in `program`. If we just run the program `python3 vm.py program`, it begins to print out a url however it seems to stop after a bit. I initially thought that I would have to translate the program to figure out what it does and try to fix it however after waiting a bit, the program prints out more of the url. It seems that whatever the program is doing, takes longer and longer to calculate the result. After waiting long enough we can guess the url `http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com`.

The website appears to be a collection of pictures of cats. Each page has a picture and a set of links and each link leads to another page and so on. Using `scrapy`, I crawled all the links and downloaded all the images. Going through them, it doesn't look like any of the pictures have the flag in it, either in the image itself or in the binary. So maybe the guess is incorrect and there is still more in the url.

Taking a look at the program again, it seems like there are 3 phases of `🚛 🥇 1️⃣ 0️⃣ 1️⃣ 1️⃣ 4️⃣ 1️⃣ 0️⃣ 5️⃣ 8️⃣ ✋ 📥 🥇` instructions. Looking at the operations map, these instructions are creating and pushing the values of the first register onto the stack. Note that each block also ends with `🚛 🥈 7️⃣ 6️⃣ 5️⃣ ✋` which loads a value into the second register. If we work backwords by searching for all the print instructions (🎤), we can see that they all have a `xor (🌓)` instruction before it. So the first assumption is it is xoring each of the numbers in the stack and printing them out. Adding these lines `print("{} ^ {}\n".format(b, a))` to the `xor` function in the vm prints out

```
106 ^ 2 h
119 ^ 3 t
113 ^ 5 t
119 ^ 7 p
49 ^ 11
74 ^ 101
172 ^ 131
242 ^ 151
216 ^ 181
208 ^ 191
339 ^ 313
264 ^ 353
344 ^ 373
267 ^ 383
743 ^ 727
660 ^ 757
893 ^ 787
892 ^ 797
1007 ^ 919
975 ^ 929
```

The numbers on the left of the xor match the values pushed onto the stack. All 3 blocks are similar so we can assume that they all doing the same thing different numbers. And we can also guess that the numbers on the right have to be calculated and the time it takes to calculate those increase as the program goes on. We can also see that the numbers on the right are primes and that supports our theory that maybe we need to make the calculations more effecient. They seem to specific primes however, not just any prime number. There is an [online database for number sequences](oeis.org/) so we can just enter those numbers in there and we can see that they are [palindromic prime numbers](https://oeis.org/A002385). It even gives us a small list and algorithms to find them. Another observation is that the palindromes are in order, so now we can just calculate them and xor each one with the values. `extract-palindromes.py` outputs a list of palindromes in the `palindromes` file. Filtering the first 6 million primes is enough to get all the palindromes needed. `palindromes.py` reads the list of palindromes and xors them with the correct values.

The first chunk prints out `http://emoji-t0anaxnr3nacpt4na.web.ctfco` and we can see already, that the url is longer than the one we had earlier. We already know the rest of the url which is `mpetition.com/` and that matches the number of values in the next chunk. Use this, we can reverse it and double check that we are doing it correctly. If we try doing the same thing with the second chunk, it does not produce the same output. This is where the `🚛 🥈 9️⃣ 9️⃣ ✋` comes in. That value gives us the starting index - 1. Finally, the full url is `http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/` and we can get the flag `CTF{Peace_from_Cauli!}`.