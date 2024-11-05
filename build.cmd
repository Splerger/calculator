@echo off

cls

pyinstaller --onefile --icon=icon.ico --add-data="icon.ico;." --add-data="click.mp3;." .\calculator.pyw

start dist/calculator.exe
