# Python - Object-relational Mapping :computer:

![Image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230417%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230417T154520Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4170673e22e5b05254bc92e02c5c8e4eac35b91b673b01b6e88fd6ee7c8f81c0)

The aim of this project is to be conversant with an Object-relational mapper (ORM).
The module MySQLdb will be used as an interface to MySQL.
The module SQLAlchemy will be used as an ORM.

## Learning Objectives :bookmark_tabs:

* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Table of contents
Files | Description
----- | -----------
[0-select_states.py](./0-select_states.py) | Python script that lists all ```states``` from the database ```hbtn_0e_0_usa```
[1-filter_states.py](./1-filter_states.py) | Python script that lists all ```states``` with a ```name``` starting with ```N``` (upper N) from the database ```hbtn_0e_0_usa```
[2-my_filter_states.py](./2-my_filter_states.py) | Python script that takes in an argument and displays all values in the ```states``` table of ```hbtn_0e_0_usa``` where ```name``` matches the argument
[3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | Python script that takes in arguments and displays all values in the states table of ```hbtn_0e_0_usa``` where ```name``` matches the argument and is MySQL injection free
[4-cities_by_state.py](./4-cities_by_state.py) | Python script that lists all ```cities``` from the database ```hbtn_0e_4_usa```
[5-filter_cities.py](./5-filter_cities.py) | Python script that takes in the name of a state as an argument and lists all ```cities``` of that state, using the database ```hbtn_0e_4_usa```
[model_state.py](./model_state.py) | python file that contains the class definition of a ```State``` and an instance ```Base = declarative_base()```
[6-model_state.py](./6-model_state.py) | python file that creates State objects for the database ```hbtn_0e_6_usa```
[7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Python script that lists all ```State``` objects from the database ```hbtn_0e_6_usa```
[8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Python script that prints the first ```State``` object from the database ```hbtn_0e_6_usa```
[9-model_state_filter_a.py](./9-model_state_filter_a.py) | Python script that lists all ```State``` objects that contain the letter a from the database ```hbtn_0e_6_usa```
[10-model_state_my_get.py](./10-model_state_my_get.py) | Python script that prints the ```State``` object with the ```name``` passed as argument from the database ```hbtn_0e_6_usa```
[11-model_state_insert.py](./11-model_state_insert.py) | Python script that adds the ```State``` object “Louisiana” to the database ```hbtn_0e_6_usa```
[12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | Python script that changes the name of a ```State``` object from the database ```hbtn_0e_6_usa```
[13-model_state_delete_a.py](./13-model_state_delete_a.py) | Python script that deletes all ```State``` objects with a name containing the letter a from the database ```hbtn_0e_6_usa```
[model_city.py](./model_city.py) | Python file that contains the class definition of a ```City```
[14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) | Python script that prints all ```City``` objects from the database ```hbtn_0e_14_usa```
[tests](./tests) | This folder entails all the respective MySQL scripts for the tasks

## Bugs :loudspeaker:

No known bugs.

## Authors :black_nib:

**Paul Njuga** [Github](https://github.com/Paul-Njuga)
