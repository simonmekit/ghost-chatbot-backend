# ghost-chatbot-backend

This is a python API for ghost-chatbot


Requirements

you need to install the following before running this Api

1 OPENCOG (cogutil, atomspace and opencog)

2 Relex Server

3 Guile

and check that all these are working prefectly

the code is tasted on python 2.75 and python 3.6


How to Run this

1 download or clone this projects in the directory you want

2 in StartServer.py add your /path/to/relex location

    e.g self.relex_location = "/home/aman/relex"

3 then run the apighost.py by any of your python IDE
   or in the command line as 

   python apighost.py
   
  in the beginning there is only one data that is parsed which is 

  (ghost-parse "u: (hi robot) hello human")
  
  so you can check it by typing hi robot only
  
  then if you want to parse your own data you can type 
  
  (ghost-parse-file "path/to/file") in the api
  
  e.g (ghost-parse-file "files/files.ghost")  
  
  then you can ask any question that is parsed in your file
   