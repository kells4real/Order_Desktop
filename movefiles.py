
import os, shutil, glob
import time
import datetime
user_path = os.path.expanduser('~')

def main():
    def moveAllFilesinDir(srcDir, dstDir):
        def text():
            dstDir2 = f'{dstDir}\Text' # Text folder path spcified
            lists = [] # Empty list to count files
                
            if os.path.isdir(dstDir2) == False: # If the Text directory doesn't already exist in the head folder
                os.makedirs(dstDir2) # Create the afformentioned folder
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2): # If source directory and destination directory is a go, then proceed
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.txt' in filePath or '.rtf' in filePath: # if file path has '.txt' or 'rtf' which are text extentions
                        lists.append(filePath) # append the file paths to the LIST lists
                        shutil.move(filePath, dstDir2) # Moves the files from the initial path to the destination path specified
                aall = len(lists) # Assigns the lenght of the LIST list to aall
                    
                if aall > 1: # If the variable aall which is the lenght of all items iterated through is more than one
                    print (f'{aall} files moved to {dstDir2}') # This is pluralize. I am open to a better way this can be done like in django though.
                    print()
                elif aall == 1: # else if the variable aall is exactly 1, then singularize
                    print (f'{aall} file moved to {dstDir2}') # Print affirmation singularized
                    print()
                else:
                    print (f'program did not find any file') # else, prints nothing found
                    print()
                    
        # All other functions follows the logic as the above function 
                    
        def pictures():
            dstDir2 = f'{dstDir}\Pictures'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2):
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.jpg' in filePath or '.png' in filePath or '.gif' in filePath or '.jpeg' in filePath or '.JPG' in filePath or '.JPEG' in filePath or '.svg' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()
        
        def audio():
            dstDir2 = f'{dstDir}\Media\Audio'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2):
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.mp3' in filePath or '.ogg' in filePath or '.wav' in filePath or '.wma' in filePath or '.midi' in filePath or '.m3u' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()

        def compressed():
            dstDir2 = f'{dstDir}\Compressed'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.zip' in filePath or '.rar' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()

        def video():
            dstDir2 = f'{dstDir}\Videos'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.mkv' in filePath or '.mp4' in filePath or '.avi' in filePath or '.mpeg' in filePath or '.flv' in filePath or '.3gp' in filePath or '.wmv' in filePath or '.mpg' in filePath or '.m4v' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()

        def shortcut():
            dstDir2 = f'{dstDir}\Shortcuts'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.lnk' in filePath or '.tmp' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()

        def disc():
            dstDir2 = f'{dstDir}\Discs'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.img' in filePath or '.iso' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()
                    
        def py():
            dstDir2 = f'{dstDir}\Py'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.py' in filePath or '.pyw' in filePath or '.pyd' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()

        def programs():
            dstDir2 = f'{dstDir}\Programs'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.exe' in filePath or '.msi' in filePath or '.bat' in filePath or '.apk' in filePath or '.jar' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file ')
                    print()

        def webdocs():
            dstDir2 = f'{dstDir}\WebDocs'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.html' in filePath or '.php' in filePath or '.css' in filePath or '.js' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file ')
                    print()

        def pdf():
            dstDir2 = f'{dstDir}\Pdf'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.pdf' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()
                    
        def cs():
            dstDir2 = f'{dstDir}\Csharp'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.cs' in filePath or '.xml' in filePath or '.axml' in filePath in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()         

        def microsoftdocs():
            dstDir2 = f'{dstDir}\microsoft'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.doc' in filePath or '.docx' in filePath or '.csv' in filePath or '.ppt' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file')
                    print()
                    
        def fonts():
            dstDir2 = f'{dstDir}\Fonts'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.fon' in filePath or '.fnt' in filePath or '.ttf' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file with the give extention (.txt)')
                    print()
                    
        def other():
            dstDir2 = f'{dstDir}\other'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.' in filePath:
                        lists.append(filePath)
                        shutil.move(filePath, dstDir2)
                aall = len(lists)
                    
                if aall > 1: 
                    print (f'{aall} files moved to {dstDir2}')
                    print()
                elif aall == 1:
                    print (f'{aall} file moved to {dstDir2}')
                    print()
                else:
                    print (f'program did not find any file with the give extention (.txt)')
                    print()             
                    
        text() # calls the function for indentifying text files
        pictures() # calls the function for indentifying picture files
        audio() # calls the function for indentifying audio files
        compressed() # calls the function for indentifying compressed files like .rar and .zip
        video() # calls the function for indentifying video files
        shortcut() # calls the function for indentifying shortcuts
        programs() # calls the function for indentifying executional files like .exe
        disc() # calls the function for indentifying disc files like ISO
        py() # calls the function for indentifying python files
        webdocs() # calls the function for indentifying web document files like .html, .php
        pdf() # calls the function for indentifying pdf files
        cs() # calls the function for indentifying C# files
        microsoftdocs() # calls the function for indentifying microsoft docs like word and excel
        other() # calls the function for indentifying other files that may not have been specified
        
        print("Thanks For Kells Using Desktop Cleaner")
        time.sleep(30) # waits for ten seconds, then exits if the user forgets to close the program after use
        print("Program will now exit in..")
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        exit()
        
    get_srcDir = input('Enter Source Dir.. e.g downloads/files: ') # source directory
    get_dstDir = input('Enter Destination Dir.. e.g downloads/files: ') # Directory where you'd like to store the moved files
    date = datetime.date.today() # Date of the current day to get unique folders where files are moved to for easy identification
    srcDir = f'{user_path}/{get_srcDir}' # Joins the pc user path to the inputed source directory to get the directory specified according to each computer
    dstDir = f'{user_path}/{get_dstDir}/{date}' # Joins the pc user path to the inputed destination directory to get the directory specified according to each computer
    
    if os.path.isdir(dstDir) == False: 
        os.makedirs(dstDir) # if the destination path doesn't exist, this creates the given directory

    moveAllFilesinDir(srcDir, dstDir) # calls the main function for this programm
    
if __name__ == "__main__":
    main() # Runs the program initially by calling the main function

