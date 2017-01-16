<?php
  exec("sudo python /home/pi/smarthome/wf/web_coffee_mode_tee.py");
  header('Location: http://192.168.10.42/joomla/index.php/test');
?>
