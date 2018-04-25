script = """
<style>
#range_selection {
	display: none;
}

body, html{
  height: 100%;
  background: #FFF;
  font-family: 'Lato', sans-serif;
}

.container{
  display: block;
  position: relative;
  margin: 40px auto;
  height: auto;
  width: 350px;
  padding: 20px;
}

h2 {
	color: #0D0E0E;
}

.container ul{
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: auto;
}

ul li{
  color: #0D0E0E;
  display: block;
  position: relative;
  float: left;
  width: 100%;
  height: 100px;
	border-bottom: 1px solid #333;
}

ul li input[type=radio]{
  position: absolute;
  visibility: hidden;
}

ul li label{
  display: block;
  position: relative;
  font-weight: 300;
  font-size: 1.35em;
  padding: 25px 25px 25px 80px;
  margin: 10px auto;
  height: 30px;
  z-index: 9;
  cursor: pointer;
  -webkit-transition: all 0.25s linear;
}

ul li:hover label{
	color: #343736;
}

ul li .check{
  display: block;
  position: absolute;
  border: 5px solid #AAAAAA;
  border-radius: 100%;
  height: 25px;
  width: 25px;
  top: 30px;
  left: 20px;
	z-index: 5;
	transition: border .25s linear;
	-webkit-transition: border .25s linear;
}

ul li:hover .check {
  border: 5px solid #4D973E;
}

ul li .check::before {
  display: block;
  position: absolute;
	content: '';
  border-radius: 100%;
  height: 15px;
  width: 15px;
  top: 5px;
	left: 5px;
  margin: auto;
	transition: background 0.25s linear;
	-webkit-transition: background 0.25s linear;
}

input[type=radio]:checked ~ .check {
  border: 5px solid #4D973E;
}

input[type=radio]:checked ~ .check::before{
  background: #4D973E;
}

input[type=radio]:checked ~ label{
  color: #4D973E;
}

input[type=submit]{
	position: relative;
	appearance: none;
	background: rgba(0, 0, 0, .2);
	padding: .8em;
	width: 75%;
	border: none;
	cursor: pointer;
	outline: none;
	color: #0D0E0E;
	border-radius: 4px;
	transition: opacity .3s ease;
	
	margin-top: 5%;
	margin-left: 15%;
	margin-right: 10%;
}

.container2{
  display: block;
  position: relative;
  margin: 40px auto;
  height: auto;
  width: 420px;
  padding: 20px;
}


#percentage, #percentage_msg{
	 display:none;
}

#percentage_sign{
	 display:none;
}

#display_selection {
	border: 1px solid black;
	text-align: center;
}

.holdem_6handed {
	margin-left: 33%;
	margin-right: 33%;
	margin-top: 10%;
	padding-right: 5%;
	padding-left: 5%;
	padding-top: 5%;
	padding-bottom: 5%;
}

.omaha_hi_6handed, .omaha_hilo_6handed {
	margin-left: 28%;
	margin-right: 28%;
	margin-top: 10%;
	padding-right: 5%;
	padding-left: 5%;
	padding-top: 5%;
	padding-bottom: 5%;
}

.omaha_5card_9handed{
	margin-left: 25%;
	margin-right: 25%;
	margin-top: 10%;
	padding-right: 2%;
	padding-left: 2%;
	padding-top: 5%;
	padding-bottom: 5%;
}

#display_selection img {
	background-color: white;
	border: 2px ridge grey;
	box-shadow: 2px 2px #404040;
	width:100%;
	max-width:130px;
}

#Next {
	position: relative;
	appearance: none;
	background: rgba(0, 0, 0, .2);
	padding: .8em;
	width: 50%;
	border: none;
	cursor: pointer;
	outline: none;
	color: #0D0E0E;
	border-radius: 4px;
	transition: opacity .3s ease;
}

#Fold, #Call {
	position: relative;
	appearance: none;
	background: rgba(0, 0, 0, .2);
	padding: .8em;
	width: 25%;
	border: none;
	cursor: pointer;
	outline: none;
	color: #0D0E0E;
	border-radius: 4px;
	transition: opacity .3s ease;
}

#Fold:hover, #Call:hover, #Next:hover {
	background: dark-grey;
}

</style>
"""