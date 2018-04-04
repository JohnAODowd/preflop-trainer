script = """
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
					//display_selection.addEventListener("submit",handle_display,false);
					document.getElementById("Fold").addEventListener("click", fold, false);
					document.getElementById("Call").addEventListener("click", call, false);

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
				
				function fold(event){
					console.log("fold");
					var percentage = parseInt(document.querySelector("#percentage").value);
					var range = document.querySelector('input[name="range"]:checked').value;
					if (range === "Custom"){
						var custom_val = document.querySelector('#custom_range').value;
						range = custom_val;
					}
					if (range < percentage) {
						document.getElementById("display_selection").style.color = "red";
					} else {
						document.getElementById("display_selection").style.color = "green";
					}
				}
				
				function call(event){
					console.log("call");
					var percentage = parseInt(document.querySelector("#percentage").value);
					var range = document.querySelector('input[name="range"]:checked').value;
					if (range === "Custom"){
						var custom_val = document.querySelector('#custom_range').value;
						range = custom_val;
					}
					if (range > percentage) {
						document.getElementById("display_selection").style.color = "green";
					} else {
						document.getElementById("display_selection").style.color = "red";
					}
				}
				
				
			})();
"""