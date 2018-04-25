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
            <title>Preflop Trainer</title>
""")
print(css.script)
print(js_landing.script)
print("""
			
        </head>
        <body>
			<div class="container">
		    <form id="variant_selection">
			<h2>Select a variant: </h2>
			<ul>
                <li>
					<input type="radio" name="type" id="1-option" value="holdem_6handed"> 
						<label for="1-option"> 
							Texas Hold'em 
						</label>  <div class="check"> </div> 
				</li>
                <li>
				<input type="radio" name="type" id="2-option" value="omaha_hi_6handed"> 
					<label for="2-option">
						Pot-Limit Omaha 
					</label>  <div class="check"> <div class="inside"> </div> </div> 
				</li>
                <li>
					<input type="radio" name="type" id="3-option" value="omaha_hilo_6handed"> 
						<label for="3-option">
							Pot-Limit Omaha Hi/Lo 
						</label> <div class="check"> <div class="inside"> </div> </div>
				</li>
                <li>
					<input type="radio" name="type" id="4-option" value="omaha_5card_9handed"> 
						<label for="4-option">
							Big-O 
						</label>  <div class="check"> <div class="inside"> </div> </div> 
				</li>
                
			
				<input type="submit" value="Next">
				</ul>
            </form>
			</div>
			
			<div class="container2">
            <form id="range_selection">
			<h2> Select a range: </h2>
			<ul>
                <li>
					<input type="radio" name="range" id="A-option" value="37"> 
						<label for="A-option">
							Open from BTN (37%)
						</label>  <div class="check"> </div>
				</li>
                <li> 
					<input type="radio" name="range" id="B-option" value="21">
						<label for="B-option">
							Call from BTN (21%)
						</label>  <div class="check"> <div class="inside"> </div> </div>
				</li>
                <li> 
					<input type="radio" name="range" id="C-option" value="16">
						<label for="C-option">
							3-bet in Position (16%)
						</label>  <div class="check"> <div class="inside"> </div> </div>
				</li>
                <li> 
					<input type="radio" name="range" id="D-option" value="9"> 
						<label for="D-option">
							3-bet out of Position (9%)
						</label>  <div class="check"> <div class="inside"> </div> </div>
				</li>
                <li> 
					<input type="radio" name="range" id="E-option" value="Custom">
					<label for="E-option"> Custom 
						<input type="text"  name="custom_range" id="custom_range" size=5 /> %
					</label>  <div class="check"> <div class="inside"> </div> </div>
				</li>
				
                <input type="submit" value="Next">
				
            </form>
			</div>
""")