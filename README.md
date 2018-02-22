# AppointmentSystem
A system which stores and displays appointments

## Instructions
This code works on both python 2.7.6 and 3.6.2 using Google Chrome.

Make sure you have the requirements

    pip install requirements.txt

Then call RestAPI.py

    python RestAPI.py

This will run in localhost:80 by default, so you just need to open your browser and enter `localhost`

Alternatively, you may edit the hostname, portnumber, and database file name. For more info:

    python RestAPI -h

## Known Issues
I deleted the fonts to satisfy GitHubs 100 file upload limit through the browser. Things may not be as beautiful as I like.

The description field may not work on Internet Explorer.

This was accomplished using only GET requests which is a bad practice. The Add Appointment functionality should be achieved using a POST request.

Vulnerable to SQL Injections (Needs sanitation)

## Credit and Sources
For better looking tables:
http://cssmenumaker.com/blog/stylish-css-tables-tutorial/

For general help with various html and css:
https://www.w3schools.com/

Author: John Skandalakis
