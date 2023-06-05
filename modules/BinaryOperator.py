"""This file will be used for Binary read operations"""
import os

class BinaryOperatorClass: 
    """This class will be used for importing and exporting hex files."""
    def __init__(self,filePath):
        if os.path.exists(filePath):
            self.filepath=filePath
            self.file = open(self.filepath, "rb")
            self.data= self.file.read()
            self.datalines=self.file.readlines()
            self.file.close()
        else:
            raise FileNotFoundError(str(filePath)+" was not found ")

    def Read(self):
        return self.data
    
    def ReadDatalines(self):
        return self.data.splitlines()
        
    def WriteToFile(self,FilePath):
        Write_File = open(FilePath, "w")
        Write_File.write(self.data)
        Write_File.close()
    
    def RefreshData(self):
        if os.path.exists(self.filepath):
            self.file = open(self.filepath, "rb")
            self.data= self.file.raw()
            self.file.close()
        else:
            raise FileNotFoundError

#help(BinaryOperatorClass)
