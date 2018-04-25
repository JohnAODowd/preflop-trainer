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
					//var percentage_msg = document.querySelector("#percentage_msg");
					//var percentage_sign = document.querySelector("#percentage_sign");
					
					var display_selection = document.getElementById("display_selection");
					var range = parseInt(document.querySelector("#range").innerHTML);
					
					var call_button = document.getElementById("Call");
					var fold_button = document.getElementById("Fold");
					var next_button = document.getElementById("Next");
					
					range = parseInt(range);
					
					if (range < percentage) {
						display_selection.style.backgroundColor = "#99EF93";
					} else {
						display_selection.style.backgroundColor = "#FFAAAA";
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
						display_selection.style.backgroundColor = "#99EF93";
					} else {
						display_selection.style.backgroundColor = "#FFAAAA";
					}
					
					call_button.style.display = "none";
					fold_button.style.display = "none";
					next_button.style.display = "initial";
				}
				
				function next(event){
					var request;
					var url = window.location.href;
					request = new XMLHttpRequest();
					request.addEventListener('readystatechange', function(){
						if ( request.readyState === 4 ) {
						// Check the request was successful
						if ( request.status === 200 ) {
							var html = document.querySelector("html");
							var trimmed_html = trim_html(request.responseText);
							html.innerHTML = trimmed_html;
							init();
						} else {
							next();
						}
					}
					}, false);
					request.open('GET', url, true);
					request.send(null);
					

				}
				
				function trim_html(str) {
					return str.replace(/<[/]?html>/gm, '');
				}
				
			})();
</script>
"""
