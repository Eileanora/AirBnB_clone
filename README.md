<h1>AirBnB - the console</h1>
<h2>Discription</h2>
<p>This is the first step towards building our first full web application: the AirBnB clone.</p>
<p>In this part, we worked on the backend part while creating a console as an interface for abstraction between the user and the program.</p>
<p>This console was made with only specidic commands available to manage the objects of the backend part of the project</p>

<h2>Installation</h2>
<li>Clone this repository in your terminal:</li>

```
git clone https://github.com/Eileanora/AirBnB_clone
```
<li> Access AirBnB directory:</li>
<li> now you can run the console in two modes:
<ul>
<li>Interactive mode: ./console</li>
<li>Non-interactive mode: echo "your command" | ./console.py</li>
</ul>
</li>
example:

```
echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

<h2> Commands </h2>
<p>Here are the commands available in the console:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Usage</th>
<th>Example</th>
<th>Other Syntax</th>
</tr>
</thead>
<tbody>
<tr>
<td>help</td>
<td>Display help</td>
<td>help</td>
</tr>
<tr>
<td>quit</td>
<td>Quit command to exit the program</td>

<td>quit</td>
</tr>
<tr>
<td>EOF</td>
<td>Quit command to exit the program</td>
<td>EOF</td>
</tr>
<tr>
<td>create</td>
<td>Create a new instance of BaseModel, save it (to the JSON file) and print the id</td>
<td>create BaseModel</td>
<td>BaseModel.create()</td>
</tr>
<tr>
<td>show</td>
<td>Prints the string representation of an instance based on the class name and id</td>
<td>show BaseModel 1234-1234-1234</td>
<td>BaseModel.show(1234-1234-1234)</td>
</tr>
<tr>
<td>destroy</td>
<td>Deletes an instance based on the class name and id (save the change into the JSON file)</td>
<td>destroy BaseModel 1234-1234-1234</td>
<td>BaseModel.destroy(1234-1234-1234)</td>
</tr>
<tr>
<td>all</td>
<td>Prints all string representation of all instances based or not on the class name</td>
<td>all BaseModel</td>
<td>BaseModel.all()</td>
</tr>
<tr>
<td>update</td>
<td>Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)</td>
<td>update BaseModel 1234-1234-1234 email "btats@btats.com"</td>
<td>BaseModel.update(1234-1234-1234, email, "btats@btats.com" "</td>
</tr>
<tr>
<td>count</td>
<td>Retrieves the number of instances of a class</td>
<td>Count BaseModel</td>
<td>BaseModel.count()</td>
</tr>
</tbody>
</table>


<h2>Objects and Classes</h2>
<p>Here are the classes that we worked on:</p>
<table>
<thead>
<tr>
<th>Class</th>
<th>Attributes</th>
<th>Methods</th>
</tr>
</thead>
<tbody>
<tr>
<td>BaseModel</td>
<td>id, created_at, updated_at</td>
<td>save(), to_dict()</td>
</tr>
<tr>
<td>User</td>
<td>email, password, first_name, last_name</td>
<td></td>
</tr>
<tr>
<td>State</td>
<td>name</td>
<td></td>
</tr>
<tr>
<td>City</td>
<td>state_id, name</td>
<td></td>
</tr>
<tr>
<td>Amenity</td>
<td>name</td>
<td></td>
</tr>
<tr>
<td>Place</td>
<td>city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids</td>
<td></td>
</tr>
<tr>
<td>Review</td>
<td>place_id, user_id, text</td>
<td></td>
</tr>
</tbody>
</table>
<p><strong>All classes inherit from BaseModel</strong></p>

<h2>Authors</h2>
<p>Yasmeen Hany</p>
<p> Alaa Ayman</p>
