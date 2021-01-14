#movefile.py
#by Matthew Bendyna
#this module contains a single function that takes two parameters,
#One being the file path, a .txt file name
#This allows you to easily write a file into any given directory.

#Remember to use the raw string r symbol before the path string if you have single slashes

def returnFile(r, file, ordir): #a special function called under a special circumstance in the move() method
    import os                 #returnFile() returns the file to the directory
    os.chdir(ordir)           #that move() attempted to move from
    f=open(file, 'x')
    f.write(r)
    f.close()
    return
    

def move(path, file, returntobasedir=True): #Moves a chosen file in your current directory to another directory of your choice
    import os
    os.path.join('usr', 'bin', 'spam')
    
    ordir=os.getcwd()
    
    if os.path.exists(file):
        f=open(file, 'r')
        r=f.read()
        f.close()
        os.remove(file)
    else:
        print('Error: This file does not exist.')
        return
    
    if os.path.exists(path):
        os.chdir(path)
    else:
        print('Desired path does not exist')

    if os.path.exists(file):
        y=input('This file already exists in the target directory. Are you sure you wish to overwrite it? (y/n)')
        if y=='y':
            f=open(file, 'w')
            f.write(r)
            f.close()
            print(file+' has been overwritten.')
        elif y=='n':
            returnFile(r, file, ordir)
            print('Overwrite has been aborted and your file returned.')
            return
        else:
            returnFile(r, file, ordir)
            print('Your response was not understood. Process aborted and file returned')
            return
    else:
        f=open(file, 'w')
        f.write(r)
        f.close()
        print(file+' has been successfully moved from '+ordir+' to '+path+'.')

    if returntobasedir==True:
        os.chdir(ordir)
    else:
        return(ordir)
    return

def copy(path, file, returntobasedir=True): #Copies a file to another directory
    import os
    os.path.join('usr', 'bin', 'spam')

    ordir=os.getcwd()

    if os.path.exists(file):
        f=open(file, 'r')
        r=f.read()
        f.close()
    else:
        print('Error: This file does not exist.')
        return
    
    if os.path.exists(path):
        os.chdir(path)
    else:
        print('Desired path does not exist')
        return
    
    if os.path.exists(file):
        y=input('This file already exists in the target directory. Are you sure you wish to overwrite it? (y/n)')
        if y=='y':
            f=open(file, 'w')
            f.write(r)
            f.close()
            print(file+' has been overwritten.')
        elif y=='n':
            print('Overwrite has been aborted.')
        else:
            print('Your response was not understood. Overwrite has been aborted')
            return
    else:
        f=open(file, 'x')
        f.write(r)
        f.close()
        print(file+' has been copied into '+path+'.')
        
    if returntobasedir==True:
        os.chdir(ordir)
    else:
        return(ordir)
    return
            

def remove(path, file, returntobasedir=True): #Deletes a file in any directory
    import os
    os.path.join('usr', 'bin', 'spam')
    
    ordir=os.getcwd()

    if os.path.exists(path):
        os.chdir(path)
    else:
        print('Desired path does not exist')
        return
    if os.path.exists(file):
        os.remove(file)
    else:
        print('The file you wish to delete does not exist.')
        
    if returntobasedir==True:
        os.chdir(ordir)
    else:
        return(ordir) 
    return
