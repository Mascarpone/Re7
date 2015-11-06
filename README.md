#RE7

##Install
Firstly, make you sure you installed the packet python-pip (http://pip.readthedocs.org/en/stable/installing/).
Pip is a module installer for python.

Now follow this tutorial: http://flask.pocoo.org/docs/0.10/installation/
You will use virtualenv, so the modules you're using are not installed on your current system, but only in a directory. The virtual-env module is often used in python, because it creates a very clean environnement not depending on the system.

Now if you want to run the project load your virtual environnement (where can install any module with pip):
    $ . /path_to_env/bin/activate

And run the server:
    $ python app.py

You can find the website on http://localhost:8000

#Git

The git equivalent to svn update is:
    $ git pull
Or, a safer way:
    $ git fetch #this lines retrieves the changes locally, but doesn't modify the current branch
    $ git merge #this line merges the previously fetched changes, and the current branch

The git equivalent to svn commit is:
    $ git commit -m <message> #commits only locally, can be done as many times as wanted
    $ git push # sends all previous commits to the server



##Some reading

http://flask.pocoo.org/docs/0.10/quickstart/

http://jinja.pocoo.org/docs/dev/templates/

http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf
