[![Download font_lister](https://img.shields.io/sourceforge/dt/font-lister.svg)](https://sourceforge.net/projects/font-lister/files/latest/download) 
Python 3.11.1 | Optimised for Windows users

```
████████╗██╗  ██╗██╗███████╗    ██╗███████╗    ██████╗  ██████╗ ██╗     ██╗ ██████╗███████╗
╚══██╔══╝██║  ██║██║██╔════╝    ██║██╔════╝    ██╔══██╗██╔═══██╗██║     ██║██╔════╝██╔════╝
   ██║   ███████║██║███████╗    ██║███████╗    ██████╔╝██║   ██║██║     ██║██║     █████╗  
   ██║   ██╔══██║██║╚════██║    ██║╚════██║    ██╔═══╝ ██║   ██║██║     ██║██║     ██╔══╝  
   ██║   ██║  ██║██║███████║    ██║███████║    ██║     ╚██████╔╝███████╗██║╚██████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝╚══════╝
```


# Description

Whether you need to reuse it for programming, painting, or any other task that requires a PDF list of your fonts from a computer, this application is helpful.

[![Download font_lister](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/font-lister/files/latest/download)
![Capture d'écran 2023-03-18 022416](https://user-images.githubusercontent.com/92639080/226077059-ae75637e-5aad-4e02-944b-92f4ca3ba624.png)




# :scroll: License

This repository is released under the [MIT License](LICENSE). Please see the `LICENSE` file for more information.

# :question: Support & Questions

If you have any questions or need support, please feel free to open an issue or join my twitter.



```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```
Here's a tutorial explaining different ways to run the files:

# For **MAC** & **Linux** users:

Since this script is designed for Windows users, you should probably first improve the code.

However, here is the procedure to run the script:

* :computer:: [MAC] - https://macosx-faq.com/how-to-run-python-script/
* :keyboard: [LINUX] - open a terminal, then `cd` to the script's directory and type:

```
python script.pyw

```
(where `script.pyw` is obviously the name of the file you've downloaded)

# :desktop_computer: For **Microsoft** users:

Because this script is made by PyInstaller, it could be detected as malware. (sorry, but I will not spend money to just be approved by "security" software/websites, you have the code, and here are possibilities to help you run it:

## :point_right: 1. Run by simple click on `APPLICATION.exe`

The `.exe` file is a portable version created for Microsoft users with PyInstaller, allowing you to download and use this file alone, without any additional files.

If there is no `.exe` file available, it means that the application is stored in a directory, as a portable version is not provided. In this case, simply locate the `APP_NAME.exe` file within the directory and launch it with a single click. You can place the folder anywhere you like and create a shortcut to the executable file for easy access.

## :point_right: 2. Run with Python

`Python script` is a directory with the original script for python 3.11.

In case you have a lower version, you may have to download module imported not included with your version. Just read the first lines of the script in Alexandria with a notepad or whatever to find what's missing.

If you would like to run with python **YOU WILL NEED THE IMAGE .png PLACED IN THE SAME DIRECTORY OF THE RUNNING SCRIPT**.

Also, you can add a `w` to the extension (like `script.pyw`). It means `windowed mode`, to launch the python script without the CMD, but it's still a common python file.

## :point_right: 3. Compile the script by yourself

### Instructions :information_desk_person:

To create your own executable from the python file, you will need to install pyinstaller and python.

Here are the steps you should follow:

* Download python 3.11.1

Don't forget to add it to your path with the installer or in variables environment (so reboot your PC after the installation), here is the link: https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

* Open your CMD as an administrator and type the following command:

```
python -m pip install pyinstaller
```

* You can now run it using a ruby `.spec` file by entering the following command in the project directory:
`pyinstaller YOUR_FILE.spec`

Normally, I place a blank.spec file in the "script" folder, if there isn't one let's watch over here:

https://github.com/SECRET-GUEST/tiny-scripts/tree/ALL/useful%20for%20python/pyinstaller

*You can also run it directly with your OS, type the following command, replacing the file paths with your own:

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py
```
Here are the explanations of the different options:

- `--onefile`: creates a single executable that includes all dependencies.
- `--icon=icon.ico`: specifies the icon to use for the executable (replace icon.ico with the path to your icon file).
- `--add-data "path/to/file;folder_name"`: adds external files required by the program. The path to the file and the name of the folder in which the file will be extracted should be separated by a semicolon `;`. You can add multiple files by separating them with semicolons.

- `script.py`: specifies the name of your Python script.

- `--noconsole`: hides the console when the executable is run.

Make sure to replace the snipped parts with the names of your files and folders. Also note that the path should be specified based on the operating system you are working on.

After running this command, you should have a single executable that includes all dependencies, external files, and a custom icon, and does not show the console when running.

:point_down: Alternatively, you can also :point_down:

## :point_right: 4. Create a batch file to run

- [ ] Create a text file

- [ ] In the text file type and write (and change/complete the path, first is for python, 2nd is for script.py):

```
C:\YOUR PATH TO PYTHON\python.exe" "C:\**YOUR PATH TO THE SCRIPT**\script.pyw"
```


If Python is in the path, you can just:

```
python "C:\**YOUR PATH TO THE SCRIPT**\script.pyw"
```

- [ ] Rename the `new_file.txt` to `script.bat` then just click on it, and it will run the program


```
     _ ._  _ , _ ._            _ ._  _ , _ ._    _ ._  _ , _ ._      _ ._  _ , _ .__  _ , _ ._   ._  _ , _ ._   _ , _ ._   .---.  _ ._   _ , _ .__  _ , _ ._   ._  _ , _ ._      _ ._  _ , _ .__  _ , _ . .---<__. \ _
   (_ ' ( `  )_  .__)        (_ ' ( `  )_  .__ (_ ' ( `  )_  .__)  (_ '    ___   ._( `  )_  .__)  ( `  )_  .__)   )_  .__)/     \(_ ' (    )_  ._( `  )_  .__)  ( `  )_  .__)  (_ ' ( `  )_  ._( `` )_  . `---._  \ \ \
 ( (  (    )   `)  ) _)    ( (  (    )   `)  ) (  (    )   `)  ) _ (  (   (o o) )     )   `)  ) _    )   `)  ) _    `)  ) \.@-@./(  (    )   `)     )   `)  ) _    )   `)  ) _ (  (    )   `)         `) ` ),----`- `.))  
(__ (_   (_ . _) _) ,__)  (__ (_   (_ . _) _) _ (_   (_ . _) _) ,__ (_   (  V  ) _) (_ . _) _) ,_  (_ . _) _) ,_ . _) _) ,/`\_/`\ (_   (  . _) _) (_ . _) _) ,_  (_ . _) _) ,__ (_   (_ . _) _) (__. _) _)/ ,--.   )  |
    `~~`\ ' . /`~~`           `~~`\ ' . /`~~`   `~~`\ ' . /`~~`     `~~`/--m-m- ~~`\ ' . /`~~`   `\ ' . /`~~`  `\ ' . /  //  _  \\ ``\ '  . /`~~`\ ' . /`~~`   `\ ' . /`~~`     `~~`\ ' . /`~~`\ ' . /`~~/_/    >     |
         ;   ;                     ;   ;             ;   ;               ;   ;      ;   ;          ;   ;         ;   ;  | \     )|_   ;    ;      ;   ;          ;   ;               ;   ;      ;   ;    |,\__-'      |
         /   \                     /   \             /   \               /   \      /   \          /   \         /   \ /`\_`>  <_/ \  /    \      /   \          /   \               /   \      /   \     \__         \
________/_ __ \___________________/_ __ \___________/_ __ \______ __ ___/_ __ \____/_ __ \________/_ __ \_______/_ __ \\__/'---'\__/_/_  __ \____/_ __ \________/_ __ \_____ _______/_ __ \____/_ __ \____ __\___      )
```
