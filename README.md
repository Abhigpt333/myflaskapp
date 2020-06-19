This is a python flask app running on port 5000
We can register with new user and then login to access the items and can logoutafter performing our tasks.
To dockerize it we have to create two containers linked to each other.
One will be for python flask having all the files and running on container port 5000
The other one will be of postgres which will be running on container port 5432 and host port 54320
