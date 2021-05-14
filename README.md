# Cowid-Slot-Finder

This python selenium application will login and check for the open slots in Cowin application and will play music whenever there would be openslots.

## Replace comments and variables before run
- Open app.py
- On line 15, replace with your mobile number
- On line 47, replace with your area pincode

## Installation and Setup
Setup Virtualenv (Optional)
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtualenv.
```bash
pip install virtualenv

virtualenv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py
```
Setup without Virtualenv 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.
```bash
pip install -r requirements.txt

python app.py
```
## Prerequisites and Aim
- It uses Python 3.9.2. You will require Python (I have not tried it on older versions).
- It uses Selenium and Chrome to automate the task of searching for the open slots.
- My aim was to somehow eliminate/bypass the OTP authentication which wastes a lot of time while logging in. So, This program will authenticate once and will search for open slots in Loop, until Open slots found or the session fails.
- If sessions fail, you will require to run this program again. I have tried at max the session exists for 55 Min.
- If any of the terminating conditions found, it plays the audio (audio.mp3). You can replace it with any file you want.

## To-Dos and Known Issues
- Need a better way to eliminate/bypass OTP authentication.
- Sometimes, while selecting the people for the schedule, it fails (app.py, Line 32)
- Interruption with the browser can fail the program.
- Need a way to stop the audio, after you get attention. Or some better way to get notification.
## Contributing
Pull requests are welcome.
