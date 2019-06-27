# Description
## Crypto Caulingo
Label: crypto

Well you've done it, you're now an admin of the Cookie World Order. The clandestine organisation that seeks to control the world through a series of artfully placed tasty treats, bringing folks back in to their idea of what a utopian society would look like. Strangely enough, the webcam data is being fed to understand the properties of the entities you had originally seen. They seem to be speaking back into the camera (an unadvertised microphone) but it's hard to understand what they want. You must- if nothing else ever was important in your life, you must make contact with these beautiful creatures! Also, what exactly is a "cauliflower"?

# Solution
This task has a zip attachment which contains a `msg.txt` and a `project_dc.pdf` file. The msg.txt gives us 3 values: `n`, `e` and `msg`. Looking the the pdf, it seems that we have to decrypt the message which was encrypted with rsa. Now I need a refresher on RSA, below is a really quick summary from [1] and its better to read the actual source.

- It is easy to find two distinct large primes `p` and `q`
- It is easy to multiply two large primes together, calculating `n = p * q`
- However, given `n`, it is difficult to factor out `p` and `q`
- Given `a`,`n` and `e` , with `0 < a < n` and `e > 1`, calculating `a`<sup>`e`</sup>`mod(n)` is easy.
- But inversely, given `a`<sup>`e`</sup>`mod(n)`, `e` and `n`, it is difficult to calculate `a`.
- However, if the multiplicative inverse of `e modulo ϕ(n)=(q−1)(p−1)`, labelled `d`, is given, then the previous calculation is easy. (The multiplicative inverse satisfies `e⋅d=1(modϕ(n))`)
- And finally, calculating `d` from only `n` and `e` is difficult, but easy if the factorization of `n = p * q` is known.

Now I have not fully wrapped my head around RSA so I'm just kinda reading up and trying to figure things out at this point. One thing I found when doing research was this database [factordb](http://factordb.com/index.php). Using that site, we dont find our `n` but it's still good to know. Other things to note is that using the value of e = `65537` is a standard. Lets take a look at the constraints we have: `|A × P - B × Q| < 10_000` and `1 ≤ A,B ≤ 1000`. In my research I also came accross this repo [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) which contained scripts to help with these types of problems. In that repo there was a list of attacks and one of them was `Fermat's factorisation for close p and q`. That sounds similar to our situation where `P` and `Q` are close. `Fermat's factorization method factors N into p and q very quickly if p and q share half of their leading bits, i.e., if the gap between p and q is below the square root of p.`[5]. I tried it but it took a long time to run and didn't seem to work so I probably have something wrong. I tried a few other attempts but this task I couldn't really figure out so I would like to revisit it some time.


- [[1] Basics of Cryptography Part I: RSA Encryption and Decryption](https://sahandsaba.com/cryptography-rsa-part-1.html)
- [[2] RSA Algorithm](https://www.di-mgt.com.au/rsa_alg.html)
- [[3] Khan academy](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/rsa-encryption-part-4)
- [[4] Khan academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses)
- [[5] Fermat's fatorisation](https://facthacks.cr.yp.to/fermat.html)