
class JustCounter:
   __secretCount = 0			# Double underscore to make it hidden
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

print counter._JustCounter__secretCount   #object._className__attrName


print counter.__secretCount  #This is hidden attr...cant be accessed

