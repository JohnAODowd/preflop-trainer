script = """
<script>
(function(){
				var variant_selection;
				var range_selection;
				var hand_form;

				document.addEventListener("DOMContentLoaded",init,false);

				function init(){
					hand_form = document.querySelector("#hand_form");
					document.getElementById("Fold").addEventListener("click", fold, false);
					document.getElementById("Call").addEventListener("click", call, false);
					document.getElementById("Next").addEventListener("click", next, false);

				}	
				
				function fold(event){
					console.log("fold");
					var percentage = parseInt(document.querySelector("#percentage").innerHTML);
					var hand_form = document.getElementById("hand_form");
					var range = parseInt(document.querySelector("#range").innerHTML);
					
					var call_button = document.getElementById("Call");
					var fold_button = document.getElementById("Fold");
					var next_button = document.getElementById("Next");
					
					range = parseInt(range);
					
					if (range < percentage) {
						hand_form.style.color = "green";
					} else {
						hand_form.style.color = "red";
					}
					
					call_button.style.display = "none";
					fold_button.style.display = "none";
					next_button.style.display = "initial";
				}
				
				function call(event){
					console.log("call");
					var percentage = parseInt(document.querySelector("#percentage").innerHTML);
					var range = parseInt(document.querySelector("#range").innerHTML);
					var hand_form = document.getElementById("hand_form");
					
					var call_button = document.getElementById("Call");
					var fold_button = document.getElementById("Fold");
					var next_button = document.getElementById("Next");

					range = parseInt(range);
					
					if (range >= percentage) {
						hand_form.style.color = "green";
					} else {
						hand_form.style.color = "red";
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