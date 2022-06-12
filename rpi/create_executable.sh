# this script will create an executable file named "main_app" 
#    from the python files and the item_config.yaml file
# the executable file will run automatically when rpi turnes on 
#    and when you run the alias "app" on the terminal

pyinstaller --onefile --noconsole /home/pi/Documents/project/Donate-It/rpi/main_app.py 
cp /home/pi/Documents/project/Donate-It/rpi/dist/main_app /home/pi/Documents/project/Donate-It/rpi
rm -r /home/pi/Documents/project/Donate-It/rpi/build
rm -r /home/pi/Documents/project/Donate-It/rpi/dist
rm /home/pi/Documents/project/Donate-It/rpi/main_app.spec