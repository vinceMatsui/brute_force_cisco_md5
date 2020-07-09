import os
import sys
import shlex

search= sys.argv[1]
salt  = sys.argv[2]
counter = 0
with open("crackstation-human-only.txt", 'r', errors='ignore') as infile:
    for line in infile:
        line = line.replace("\n", "")
        line = line.strip()
        secret = line
        secret = shlex.quote(secret)
        try :
          if not secret :
              print("nullable")
              continue
          else:
              print(secret)
              cmd = "openssl passwd -1 -salt "+salt+" "+secret
              hash= os.popen(cmd).read()
              print(hash)
              if(hash.strip() == search) :
                  print("\n\nFIND PASSWORD : "+str(secret))
                  break
              else:
                  print("NOT FOUND \n\n")
                  continue
        except Exception  as error:
            print('ERROR '+str(error))
        counter += 1
