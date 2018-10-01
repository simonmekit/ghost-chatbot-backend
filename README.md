# ghost-chatbot-Api

This is a python API for ghost-chatbot

**Requirements**

you need to install the following before running this Api and check that all these are working prefectly
    
    1 OPENCOG (cogutil, atomspace and opencog)
    
    2 Relex Server
    
    3 Guile


**How to Run this**

1 Download or clone this projects in the directory you want

2 In StartServer.py add your relex location in place of /path/to/relex

    e.g self.relex_location = "/home/aman/relex"

3 Then run apighost.py in any of your python IDE or in the Terminal as _python apighost.py_ in the beginning there is only one data that is parsed which is _(ghost-parse "u: (hi robot) hello human")_ so you can check it by typing _hi robot_ only then if you want to parse your own data you can type **(ghost-parse-file "path/to/file")** in the API

    e.g (ghost-parse-file "files/files.ghost")  
  
 _note:_  The code is tasted on python 2.75 and python 3.6
 