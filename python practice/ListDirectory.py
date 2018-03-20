def listDirectory(directory,fileExtList):
    "get list of file info objects for files of particular extensions"
    fileList=[os.path.normcase(f) for f in os.listdir(directory)]
    fileList=[os.path.join(directory,f) for f in fileList if os.path.splitext(f)[1] in fileExtList]
    def getFileInfoClass(filename,module=sys.module[FileInfo.__module__]):
        "get file info class from filename extension"
        subclass="%sFileInfo"%os.path.splitext(filename[1].upper()[1:])
        return hasattr(module,subclass) and getattr(module,subclass) or FileInfo
    return [getFileInfoClass(f)(f) for f in fileList]

if "__name__"=="__main__":
    listDirectory("c:\\data\\db",".lock")
