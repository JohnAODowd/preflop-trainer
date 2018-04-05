#!/usr/local/bin/python3

from cgi import FieldStorage
from os.path import join
from cgitb import enable
enable()

import reader
import js_hand
from format import format, jumble

form_data = FieldStorage()

if not form_data:
	exit(0)

range_val = form_data.getfirst("range")
type_val = form_data.getfirst("type")

path = join("orderings", type_val + ".txt")
file = open(path, "r")

rankings = reader.build(file)
percentage, hand = reader.random_val(rankings)
image_list = reader.convert_to_png(format(hand, jumble=True))

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
""")
print("""
			<script>	
""")
print(js_hand.script)
print("""
			</script>
        </head>
        <body>
			<form id="display_selection">
""")
for image in image_list :
        print('<img src="png-cards/' + image + '" style="width:100%;max-width:100px" border-radius="25px">')

print("""
            
            <p><span id="percentage" style="display:none">%s</span></p>
			<p><span id="range" style="display:none">%s</span></p>
			<p><span id="type" style="display:none">%s</span></p>
			<p>Answer</p>
                  <input type="button" name="Fold" id="Fold" value="Fold"> 
				  <input type="button" name="Call" id="Call" value="Call">
				  <input type="button" name="Next" id="Next" value="Next Hand" style="display:none">
			</form>
			
            </div>
        </body>
    </html> """ % (percentage, range_val, type_val))
