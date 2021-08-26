# Dynamic DNS Updating App

Due to the nature of the dyanamic IP address of home networking services, the corresponding IP Address is updated and OpenVPN services are broken through this link. There are ways of keeping track of this via online services, but these services are not likely maintained. To do this ourselves, I'm making this script.

`pip install -r requirements.txt`

Include the proper API key from PushBullet.

Then run

`python GetIPFromWeb.py`