# clock4h

[中文](./README_zh-cn.md)

#### description
this is a `have a rest` remind clock , use `apscheduler` and `customtkinter` complete, also inside a time-select component based on
tkinter.


#### build yourself

##### 1.1 find customtkinte path

as you know, this app used customtkinte,so its packages should be incloud. you can find description at [CustomTkinter-Packaging](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)


use this command to find ` <your customtkinter packages path >`
 
```bash
pip install customtkinte
```
the example is my path `c:\users\35238\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages\customtkinter;customtkinter\`  you hava to find it like that.


##### 1.1 package
There are two ways to choose, exe and onedir
```bash
//exe(onefile)
<your pyinstaller path>pyinstaller --noconfirm --onefile --windowed --distpath "<your source path>\target\dist\" --workpath "<your source path>\target\build\" --specpath "<your source path>\target\spec\" --add-data "<your customtkinter packages path >\customtkinter;customtkinter\" "<your source path>\clock.py"

//onedir
<your pyinstaller path>pyinstaller --noconfirm --onedir --windowed --distpath "<your source path>\target\dist\" --workpath "<your source path>\target\build\" --specpath "<your source path>\target\spec\" --add-data "<your customtkinter packages path >\customtkinter;customtkinter\" "<your source path>\clock.py"
```