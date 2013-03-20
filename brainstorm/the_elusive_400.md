
Early in this project, I ran into a rather mysterious problem trying to fetch data from The Pirate Bay.

At first, every attempt to pull data from The Pirate Bay resulted in a 400 error (bad request).
I thought this was a result of robot protection, and started spoofing headers.
After playing around with it for a while, I came up with the corrent set of headers to fool TPB, or so I thought.
I had been working at school, which meant tethering off of my phone.

When I got home, all of my requests suddently started returning 400s again. Shit.
I tried again with my phone, and it worked.
It wasn't just my home network either.
Using StudentRND's network I got the same error code.

What.

I took a closer look at TPB. Here's their `robots.txt`.

```
User-Agent: *
Allow: /
Sitemap: http://thepiratebay.se/sitemap-googlish.xml.gz
```

Everything checks out, they shouldn't be blocking robots.

Same computer, same code, different networks. There must be something with the networks.

Perhaps the mobile site is different?
I seem to still get the desktop site so that shouldn't be an issue.

Really, I have no clue. Perhaps it's some nuance of tethering?
I've resorted to using a mirror, but seriously want to figure out why this is happening.
To Stack Overflow!
