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
			
			<style>
				#range_selection {
					display: none;
				}
				
				#display_selection {
					display: none;
				}
				
			</style>
			
			<script>
			(function(){
				var variant_selection;
				var range_selection;
				var display_selection;

				document.addEventListener("DOMContentLoaded",init,false);

				function init(){
					variant_selection = document.querySelector("#variant_selection");
					range_selection = document.querySelector("#range_selection");
					display_selection = document.querySelector("#display_selection");
					variant_selection.addEventListener("submit",handle_variant,false);
					range_selection.addEventListener("submit",handle_range,false);
					display_selection.addEventListener("submit",handle_display,false);
				}

				function handle_variant(event){
					event.preventDefault();
					variant_selection.style.display = "none";
					range_selection.style.display = "initial";
				}
				
				function handle_range(event){
					event.preventDefault();
					range_selection.style.display = "none";
					display_selection.style.display = "initial";
				}		
				function handle_display(event){
					event.preventDefault();
					var type = document.querySelector('input[name="type"]:checked').value;
					var range = document.querySelector('input[name="range"]:checked').value;
					if (range === "Custom"){
						var custom_val = document.querySelector('#custom_range').value;
						range = custom_val;
					}
					//var call_or_fold = event.originalEvent.explicitOriginalTarget;
					// grab data from all forms and send to server
					console.log(type);
					console.log(range);
					console.log(event);
				}	
			})();	
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
                <input type="text"  name="custom_range" id="custom_range"  /> % <br>
                <input type="submit" value="Back"> <input type="submit" value="Next">
            </form>
			
			<form id="display_selection">
""")
for image in reader.image_list :
        print('<img src="png-cards/' + image + '" style="width:100%;max-width:100px" border-radius="25px">')
				
print("""
            </p>
            <p> Percentage: %s </p>
                  <input type="submit" name="Fold" value="Fold"> <input type="submit" name="Call" id="Call" value="Call">
            </form>
			
            </div>
        </body>
    </html> """ % (reader.value[0]))
