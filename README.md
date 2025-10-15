# Log_File_Parser
Parser designed for use with Vivado log files from Simulation / Synthesis.

![Main Menu Image](https://github.com/tobywr/Log_File_Parser/blob/main/images/main_screen.png "Main Menu Image")

## Installing

This tool has currently only been tested on windows.

### Installing Tkinter

Tkinter is __required__ for the GUI to function.

To install Tkinter on linux run in the terminal:
```
$ sudo apt update
$ sudo apt install python3-tk
```
To verify installation, running : 
```
$ python3 -m tkinter
```

A GUI should appear, stating the version of tkinter installed. This validates that tkinter has been successfully installed.

### Running the parser file.

Download the main script, [`main_gui.py`](main_gui.py) and save to your computer.

Run the application by opening a terminal in the folder containing [`main_gui.py`](main_gui.py), and run the command:
```
python3 main_gui.py
```

A Window should appear showing an option to select a file.

## Using the Parser

### Select a log file to parse.

Click the ```Browse``` button in the main GUI window.

Select the .log file to parse for errors, warnings and timing summaries.

### Parsed output

Once a valid file is selected, it will be parsed for errors, warnings and timing summaries.

![Example Parsed output](https://github.com/tobywr/Log_File_Parser/blob/main/images/parsed_file_example.png "Example parsed output")

The refresh button can be used whenever a new test has been run in vivado, and you want to see the parsed summary of the same file. However, the new log ___must___ have the __exact__ same path as the previous log file that was parsed.