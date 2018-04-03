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
            <form>
                <input type="radio" name="type" value="holdem_6handed"> Texas Hold'em  <br>
                <input type="radio" name="type" value="omaha_hi_6handed"> Pot-Limit Omaha <br>
                <input type="radio" name="type" value="omaha_hilo_6handed"> Pot-Limit Omaha Hi/Lo <br>
                <input type="radio" name="type" value="omaha_5card_9handed"> Big-O <br>
                <input type="submit" value="Next">
            </form>
        </body>
    </html> """)
