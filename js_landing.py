script = """
<script>
(function(){
				var variant_selection;
				var range_selection;

				document.addEventListener("DOMContentLoaded",init,false);

				function init(){
					variant_selection = document.querySelector("#variant_selection");
					range_selection = document.querySelector("#range_selection");
					variant_selection.addEventListener("submit",handle_variant,false);
					range_selection.addEventListener("submit",handle_range,false);
				}

				function handle_variant(event){
					event.preventDefault();
					variant_selection.style.display = "none";
					range_selection.style.display = "initial";
				}
				
				function handle_range(event){
					event.preventDefault();
					range_selection.style.display = "none";
					
					relocate();
				}	
				
				function relocate(){
					var type = document.querySelector('input[name="type"]:checked').value;
					var range = document.querySelector('input[name="range"]:checked').value;
					if (range === "Custom"){
						var custom_val = document.querySelector('#custom_range').value;
						range = custom_val;
					}
					//var call_or_fold = event.originalEvent.explicitOriginalTarget;
					// grab data from all forms and send to server
					window.location.href = "hand.py?type=" + type + "&range=" + range;
					console.log(type);
					console.log(range);
					console.log(event);
				}	
			})();
</script>
"""