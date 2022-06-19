# Donate-It
***IOT project***\
\
Secondhand Clothing – Made Easy

## Description
This project aims to make donating and shopping for secondhand clothes easier.\
After taking a picture of an item using a special stand, it will be automatically uploaded to an [online clothing catalog](https://donateit100.wixsite.com/donate-it).\
The stand includes a touch screen and is not PC-based, so it simple to use by everyone.\
It is possible to customimze items' description fields - see instructions below.
This project uses Google Cloud Firebase Database to store item images and information about it. The RPi uploads the image to Firebase Storage and uploads the information to Firebase Firestore. The website loads the images and the information from Firebase to it's own database and displays it in the store gallery.

## Hardware
### What You'll Need
1. Raspberry Pi 4 (with a Camera Module port) + power adapter
2. Raspberry Pi 7-inch touchscreen display
3. Raspberry Pi Camera Module
4. Thermal Printer + power adapter + USB cable
5. 2 Ribbon cables
6. 4 Jampers

### Connecting Everything
1. Install Raspberry Pi OS: use this [link](https://www.raspberrypi.com/documentation/computers/getting-started.html) for full instructions.
2. Install on-screen keyboard on Raspberry Pi:
    ```
    sudo apt-get update
    sudo apt-get install matchbox-keyboard
    ```
3. Connect the camera to the Raspberry Pi: use this [link](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1) for full instructions.
4. Connect the touchscreen display to the Raspberry Pi: use this [link](https://www.raspberrypi.com/documentation/accessories/display.html) for full instructions.
5. Connect the thermal printer to the Raspberry Pi using an USB cable.\
   Make sure it's connected and recognized: `ls -l /dev/tty`\
   Make sure to give it the required permissions: `sudo chmod 777 /dev/usb/lp0`

## How To Run The App
1. Clone this project to the Raspberry Pi.
2. run:
    ```
    cd <path_to_the_root_folder_of_the_cloned_project>
    chmod +x main_app_rpi_executable/run_main_app.sh
    ./main_app_rpi_executable/run_main_app.sh
    ```

## Customize Items' Description Fields
You can costumize items' description fields as you wish. In order to do that follow the next steps:
1. Clone this project to the Raspberry Pi.
2. Install the python requirements. To do so run the following:
    ```
    pip install -r requirements.txt
    ```
    ***Recommended:*** use a virtual environment, to do so run the following from root folder:
    ```
    pip install virtualenv
    virtualenv <name>
    source <name>/bin/activate
    ```
3. Change the `items_config.yaml` file in `rpi` folder as you wish.\
    ***Note:*** keep the files structure as is and do not change the `Type` and `Price` fields names.
4. Create a new executable file and execute the program:
    ```
    chmod +x create_executable
    ./create_executable.sh
    ```
    ***Note:*** if you use virtual environment, run this stage after activating it.
    
## Create Shortcuts For Running The App
#### 1. Create an alias for the bash terminal:
1. Run `nano ~/.bashrc`
2. Add at the end of the file: `alias app="<path>/main_app_rpi_executable/run_main_app.sh"`
3. Save and reboot.
#### 2. Run the app automatically when the RPi turns on:
1. Run `nano ~/.config/lxsession/LXDE-pi/autostart`
2. Add the line `<path>/main_app_rpi_executable/run_main_app.sh`\
***Note:*** this file will run instead of the original RPi autostart command. In order to make your desktop appear make sure to add the following lines
before the one you added in the previous step:
    ```
    @lxpanel --profile LXDE-pi
    @pcmanfm --desktop --profile LXDE-pi
    @xscreensaver -no-splash
    ```
3. Save and reboot.
    
## Our website
https://donateit100.wixsite.com/donate-it

## Authors
@ dinaa12\
@ RacheliCh\
@ maya-st
