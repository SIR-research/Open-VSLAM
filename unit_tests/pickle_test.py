# -*- coding: utf-8 -*-
#!/usr/bin/env python
import pickle
import os
#os.chdir("/home/paulo/openvslam/openvslam/build")
#print(os.getcwd())
with open ('database.pkl','rb') as f:
    mylist = pickle.load(f)

#print(mylist[1])
## Tá funcionando bonitinho

#filename = '/home/user/somefile.txt'   #FUNCIONA
#filename=filename.rsplit( ".", 1 )[ 0 ] 
#print(filename)

#uma observação... os nomes devem ser diferentes a cada pickling...
#alguma solução pra associar ao nome do mapa?