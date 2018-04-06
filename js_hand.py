script = """
<script>
(function(){
				var variant_selection;
				var range_selection;
				var display_selection;

				document.addEventListener("DOMContentLoaded",init,false);

				function init(){
					display_selection = document.querySelector("#display_selection");
					//display_selection.addEventListener("submit",handle_display,false);
					document.getElementById("Fold").addEventListener("click", fold, false);
					document.getElementById("Call").addEventListener("click", call, false);
					document.getElementById("Next").addEventListener("click", next, false);

				}	
				
				function fold(event){
					console.log("fold");
					var percentage = parseInt(document.querySelector("#percentage").innerHTML);
					var display_selection = document.getElementById("display_selection");
					var range = parseInt(document.querySelector("#range").innerHTML);
					
					var call_button = document.getElementById("Call");
					var fold_button = document.getElementById("Fold");
					var next_button = document.getElementById("Next");
					
					range = parseInt(range);
					
					if (range < percentage) {
						display_selection.style.color = "green";
					} else {
						display_selection.style.color = "red";
					}
					
					call_button.style.display = "none";
					fold_button.style.display = "none";
					next_button.style.display = "initial";
				}
				
				function call(event){
					console.log("call");
					var percentage = parseInt(document.querySelector("#percentage").innerHTML);
					var range = parseInt(document.querySelector("#range").innerHTML);
					var display_selection = document.getElementById("display_selection");
					
					var call_button = document.getElementById("Call");
					var fold_button = document.getElementById("Fold");
					var next_button = document.getElementById("Next");

					range = parseInt(range);
					
					if (range >= percentage) {
						display_selection.style.color = "green";
					} else {
						display_selection.style.color = "red";
					}
					
					call_button.style.display = "none";
					fold_button.style.display = "none";
					next_button.style.display = "initial";
					
				}
				
				function next(event){
					location.reload();
				}
				
			})();
</script>
"""