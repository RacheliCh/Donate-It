# this script will create an executable file named "main_app" 
#    from the python files and the item_config.yaml file
# the executable file will run automatically when rpi turnes on 
#    and when you run the alias "app" on the terminal
cd /home/pi/Documents/project/Donate-It
pyinstaller main_app.py 
cp dist/main_app/main_app /home/pi/Documents/project/Donate-It
rm -r /home/pi/Documents/project/Donate-It/build
rm -r /home/pi/Documents/project/Donate-It/dist
rm /home/pi/Documents/project/Donate-It/main_app.spec