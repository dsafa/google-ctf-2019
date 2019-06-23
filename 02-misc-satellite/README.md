Another attachment that is a zip file which contains a `README.pdf` and a `init_sat` binary. Opening the pdf shows some text and a picture containing the word `osmium`.
Running the binary shows a prompt asking for a satellite name. Enter `osmium` and it presents 3 choices. Entering `a` will print some information including a link to a google doc `https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E`. The doc contains a single string `VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==` which is base64 encoded which we can recognize by the characters and the `==` padding at the end. Decoding the string gives us
```
Username: wireshark-rocks
Password: start-sniffing!
```

So now with wireshark open, as we enter `a` again and look at the traffic, we can see the flag in the text sent over the network `CTF{4efcc72090af28fd33a2118985541f92e793477f}`