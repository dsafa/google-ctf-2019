# Description
## Arrival & Reconnaissance

Having successfully figured out this "coordinate" problem. The ship lurches forward violently into space. This is one of the moments when you realize that some kind of thought or plan would have been good, but typically for you and how you found yourself in this situation, you didn't think too much before acting. Only the stars themselves know where you'll end up.

After what seems like an eternity, or at least one full season of "Xenon's Next Top Galactic Overlord" you arrive in a system of 9 planetary bodies, though one of them is exceptionally small. You nostalgically remember playing explodatoid with your friends and hunting down planets like this. But this small planet registers a hive of noise and activity on your ships automated scanners. There's things there! Billions upon trillions of things, moving around, flying, swimming, sliding, falling.

Of particular interest may be the insect-like creatures flying around this planet, uniformly. One has the words "Osmium Satellites" written on it. Maybe this is a starting point to get to know what's ahead of you.

## Satellite
Label: networking

Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?

Find something to do that isn't staring at the Blue Planet.

# Solution
Another attachment that is a zip file which contains a `README.pdf` and a `init_sat` binary. Opening the pdf shows some text and a picture containing the word `osmium`.
Running the binary shows a prompt asking for a satellite name. Enter `osmium` and it presents 3 choices. Entering `a` will print some information including a link to a google doc `https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E`. The doc contains a single string `VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==` which is base64 encoded which we can recognize by the characters and the `==` padding at the end. Decoding the string gives us
```
Username: wireshark-rocks
Password: start-sniffing!
```

So now with wireshark open, as we enter `a` again and look at the traffic, we can see the flag in the text sent over the network `CTF{4efcc72090af28fd33a2118985541f92e793477f}`