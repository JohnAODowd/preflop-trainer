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
        """ )
      
for image in reader.image_list :
      print('<img src="png-cards/' + image + '" style="width:100%;max-width:100px" border-radius="25px">')


print("""
            </p>
            <p> Percentage: %s </p>

            <form>
                  <input type="submit" value="Fold"> <input type="submit" value="Call">
            </form>
            
        </body>
    </html> """ % (reader.value[0]))