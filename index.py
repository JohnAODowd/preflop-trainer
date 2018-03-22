#!/usr/local/bin/python3

import reader

print('Content-Type: text/html')
print("")
print("")

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <link rel="icon" href="favicon.ico">
            <meta charset="utf-8" />
            <title>PLO Trainer</title>
        </head>
        <body>
            <p>
                Hello, %s %s. You may go on your way.
            </p>
        </body>
    </html>""" % ("h","h"))
