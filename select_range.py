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
            Select a range: <br>
            <form>
                <input type="radio" name="range" value="30"> Open from BTN (30%)         <br>
                <input type="radio" name="range" value="20"> Call open from BTN (20%)    <br>
                <input type="radio" name="range" value="15"> 3-bet in Position (15%)     <br>
                <input type="radio" name="range" value="10"> 3-bet out of Position (10%) <br>
                <input type="radio" name="range" value="">   Custom 
                <input type="text"  name="range"  /> % <br>
                <input type="submit" value="Back"> <input type="submit" value="Next">
            </form>

        </body>
    </html> """)
