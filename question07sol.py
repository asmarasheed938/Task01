#Charactercount
class Charactercount:
    __my_Str=None
    def setValue(self,input):
       if type(input)==str:
          self.__my_Str=input
       else:
           print("Invalid String Entered!")

    def countChar(self):
        if self.__my_Str!=None:
            return len(self.__my_Str)

cc=Charactercount()
cc.setValue("1")
if(cc.countChar()!=None):
    print("count of characters in string: ",cc.countChar())