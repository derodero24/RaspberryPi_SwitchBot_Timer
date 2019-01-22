# RaspberryPi_SwitchBot_Timer

Set a regular timer in SwitchBot.  
This program works with python3.6

1.  Install required libraries

```bash
sudo apt-get update
sudo apt-get install python-pexpect
sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev
sudo apt-get install libudev-dev libical-dev libreadline-dev
sudo pip install -r requirements.txt
```

2.  Identify Mac address of your SwitchBot by SwitchBot app or following commands

```bash
# 2.1. show Mac address list (finish by Control+C)
sudo hcitool lescan

# 2.2. Test Mac address (try pushing)
python check_address.py <Mac address>
```

3.  Edit set_timer.py and add Mac address and execution interval

4.  execute set_timer.py

```bash
python set_timer.py
```

5.  If you want to kill existing timer

```bash
# Check PID of existing timer
ps aux | grep python
# kill
kill <PID>
```
