# External XSS Scripts Server

## What it does

I had to write a bunch of scripts for a certification training and I got tired of rewriting them. So I wrote a quick flask app server to just serve the scripts. 

## How to use it
You can point your xss to `http://serverip/xss.js?f=` and use the name (without the .js part) of the js script in static you want to use. 

## JS Scripts currently
* alert.js
    * Just a simple alert PoC
* cookies.js
    * Sends request to cookies endpoint with the document cookies
* keylogger.js
    * Sets up a key logger via JS. Best for stored XSS
* ld.js
    * Steals stored local Data
* sp.js
    * Creates a username and password field to exploit autofilled login information
