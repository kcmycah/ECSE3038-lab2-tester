# ECSE3038_lab2

Design project that will be used to manage a system that monitors the status of a set of electronically measured water tanks. The embedded circuit attached to each water tank will measure the height of the water in the tank and report on the tank's current occupancy as a percentage of its maximum capacity.
The requirement is to design a RESTful API that allows each IoT enabled water tank to interface with a server so that the measure values can be represented visually on a web page.
The API should also support the maintenance of a simple user profile. The server should be able to perform the actions of a simple HTTP web server. The server should be able to perform actions on a resource such as Create, Read, Update and Delete. This is to be done without the use of a database.

The required Attributes are:

Profile

- Username
- Favourite color
- Role

Tank

- Tank id (automatically Incremented)
- Tank location description
- Percent full
- Latitude
- Longitude
