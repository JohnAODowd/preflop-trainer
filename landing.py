#!/usr/local/bin/python3

import js_landing
import css

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
			
			<style>
""")
print(css.script)
print("""
			</style> 
			<script>	
""")
print(js_landing.script)
print("""
			</script>
        </head>
        <body>
			<div>
			
		    <form id="variant_selection">
			Select a variant: <br>
                <input type="radio" name="type" value="holdem_6handed"> Texas Hold'em  <br>
                <input type="radio" name="type" value="omaha_hi_6handed"> Pot-Limit Omaha <br>
                <input type="radio" name="type" value="omaha_hilo_6handed"> Pot-Limit Omaha Hi/Lo <br>
                <input type="radio" name="type" value="omaha_5card_9handed"> Big-O <br>
                <input type="submit" value="Next">
            </form>
			
            <form id="range_selection">
			Select a range: <br>
                <input type="radio" name="range" value="30"> Open from BTN (30%)         <br>
                <input type="radio" name="range" value="20"> Call open from BTN (20%)    <br>
                <input type="radio" name="range" value="15"> 3-bet in Position (15%)     <br>
                <input type="radio" name="range" value="10"> 3-bet out of Position (10%) <br>
                <input type="radio" name="range" value="Custom">   Custom 
                <input type="text"  name="custom_range" id="custom_range" size=5 /> % <br>
                <input type="submit" value="Next">
            </form>
			
			<form id="display_selection">
""")