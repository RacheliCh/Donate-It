# this script will create an executable file named "main_app" 
#    from the python files and the item_config.yaml file
# the executable file will run automatically when rpi turnes on 
#    and when you run the alias "app" on the terminal

rm -r main_app_rpi_executable
pyinstaller --onefile --noconsole rpi/main_app.py 
rm -r build
rm main_app.spec
mv dist main_app_rpi_executable
echo "cd" $(pwd) >> main_app_rpi_executable/run_main_app.sh
echo "./main_app_rpi_executable/main_app" >> main_app_rpi_executable/run_main_app.sh
chmod +x main_app_rpi_executable/run_main_app.sh