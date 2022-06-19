# this script will create an executable file named "main_app" 
#    from the python files and the item_config.yaml file
# the executable file will run automatically when rpi turnes on 
#    and when you run the alias "app" on the terminal

pyinstaller --onefile --noconsole rpi/main_app.py 
cp dist/main_app rpi
rm -r build
rm -r dist
rm main_app.spec