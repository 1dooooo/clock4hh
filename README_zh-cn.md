# clock4hh

[English](./README.md)


#### description
这是一个定时提醒的时钟程序, 使用 `apscheduler` 和 `customtkinter`完成, 同时也包含了一个基于 `tkinter` 的 `时间选择`的组件。




#### build yourself

##### 1.1 find customtkinte path

如你所知，这个应用程序使用了 customtkinter，所以它的包应该是 incloud。 你可以在 [CustomTkinter-Packaging](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging) 找到描述

使用此命令查找` <your customtkinter packages path >`
 
```bash
pip install customtkinte
```
the example is my path `c:\users\35238\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages\customtkinter;customtkinter\`  you hava to find it like that.


##### 1.1 package
有两种方式选择，exe和onedir
```bash
//exe(onefile)
<your pyinstaller path>pyinstaller --noconfirm --onefile --windowed --distpath "<your source path>\target\dist\" --workpath "<your source path>\target\build\" --specpath "<your source path>\target\spec\" --add-data "<your customtkinter packages path >\customtkinter;customtkinter\" "<your source path>\clock.py"

//onedir
<your pyinstaller path>pyinstaller --noconfirm --onedir --windowed --distpath "<your source path>\target\dist\" --workpath "<your source path>\target\build\" --specpath "<your source path>\target\spec\" --add-data "<your customtkinter packages path >\customtkinter;customtkinter\" "<your source path>\clock.py"
```