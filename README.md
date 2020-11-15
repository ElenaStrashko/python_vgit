# PYTHON_VGIT

### RUNNING
To run this application you should add in your program argparser and enter the following line in terminal(Linux):
```
	python3 <name_of_your_app.py> -v version

```
Also if you want to see version and commit in terminal, you should use function show() in your application.
Example:
```
    import argparse
    import vgit


    ap = argparse.ArgumentParser()
    ap.add_argument('-v', action=print(vgit.show())))
    
```
This program show you information(tag, commit and changes, that should be commited) in terminal.


### RULES
For correct result of the application you must follow this rules:
```
    1. For import this library you should have folder vgit in your project's main directory.
And then use: import vgit.
    2. If you cloned vgit in /modules you must have emty/not empty file __init.py__ in /modules. And
use: from modules import vgit
    3. You mustn't delete file VERSION from /vgit
    4. Don't forget push your tags.
```


### A FEW WORDS ABOUT THE APPLICATION
This application is a library for python projects. It helps developers follow tags, commits and changes, that should be commited.
