from pyscript import document

name= "Esther Maeve D. Bae"
age= 15
height= 153
student= True
countries= ["Japan", "South Korea", "Canada"]
profile= {'color': 'brown', 'phone_brand': 'Apple', 'shoe_size': '6.5'}
favorite_fruits= {'Banana', 'Mango', 'Apple', 'Shine Musket', 'Peach'}
items= ("Airpods", "Skincare", "Speaker", "Braces", "Pajamas")

abtme =f"""
<p> Name: {name} </p>
<p> Age: {age} </p>
<p> Height: {height} </p>
<p> Student: {student} </p>
"""

addinfo =f"""
<p> Bucket List Destinations: {countries} </p>
<p> Profile: {profile} </p>
<p> Favorite Fruits: {favorite_fruits} </p>
<p> Items worth to splurge on: {items} </p>
"""
document.querySelector("#abtme").innerHTML = abtme
document.querySelector("#addinfo").innerHTML = addinfo