
import os, shutil, glob
import time
import datetime
user_path = os.path.expanduser('~')

def main():
    def moveAllFilesinDir(srcDir, dstDir):
        def text():
            dstDir2 = f'{dstDir}\Text'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.txt' in filePath or '.rtf' in filePath:
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
                    
        def pictures():
            dstDir2 = f'{dstDir}\Pictures'
            lists = []
                
            if os.path.isdir(dstDir2) == False: 
                os.makedirs(dstDir2)
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
                        # Iterate over all the files in source   
                for filePath in glob.glob(srcDir + '/*'):
                            # Move each file to destination Directory
                    if '.jpg' in filePath or '.png' in filePath or '.gif' in filePath or '.jpeg' in filePath or '.JPG' in filePath or '.JPEG' in filePath:
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
                
            if os.path.isdir(srcDir) and os.path.isdir(dstDir2) :
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
                    
        text()
        pictures()
        audio()
        compressed()
        video()
        shortcut()
        programs()
        disc()
        py()
        webdocs()
        pdf()
        cs()
        microsoftdocs()
        other()
        
        print("Thanks For Kells Using Desktop Cleaner")
        time.sleep(30)
        print("Program will now exit in..")
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        exit()
        
    get_srcDir = input('Enter Source Dir.. e.g downloads/files: ')
    get_dstDir = input('Enter Destination Dir.. e.g downloads/files: ')
    date = datetime.date.today()
    srcDir = f'{user_path}/{get_srcDir}'
    dstDir = f'{user_path}/{get_dstDir}/{date}'
    
    if os.path.isdir(dstDir) == False: 
        os.makedirs(dstDir)

    moveAllFilesinDir(srcDir, dstDir)
    
if __name__ == "__main__":
    main()

