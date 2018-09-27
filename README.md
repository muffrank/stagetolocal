# stagetolocal

A great library to load staging data into local applications.

 **Installation**

``git clone https://github.com/muffrank/stagetolocal.git`` 

Open *stage.py* and replace these lines:

``HEADERS = {'Authorization': 'Token 0814886fb6a7e1247ad149dc62f662c4ef296962'};``
  
``COOKIES = dict(csrftoken='xEtbanbIamMfpI0VHHV3Bhde6fOPg8tX',sessionid='5i0h3br0jfaq2n7cnggakphz3gf302qu')``
  
``PORT = 5000``

``STAGE_URL = "http://example.com/"``


 **Run**

``python stage.py``