# ghost-chatbot-Api

This is a python API designed to eliminate the preliminary procedures executed when using GHOST(General Holistic Organism Scripting Tool), providing smooth interaction between the Relex server and Guile.

**Requirements**

you need to install the following before running this Api and check that all these are working prefectly
    
    1 OPENCOG (cogutil, atomspace and opencog)
    
    2 Relex Server
    
    3 Guile
    

**How to Run this**

1 Download or clone this projects in the directory you want

2 run StartServer.py as python

3 Then run StartServer.py in any of IDE or in Terminal as  _python StartServer.py_

4 Finally run apighost.py in any of your python IDE or in another Terminal as _python apighost.py_ in the beginning there is only one data that is parsed which is _(ghost-parse "u: (hi robot) hello human")_ so you can check it by typing _hi robot_ only then if you want to parse your own data you can type _(ghost-parse-file "path/to/file")_ in the API

    e.g (ghost-parse-file "files/files.ghost")  
  
 _note:_  The code is tasted on python 3
 