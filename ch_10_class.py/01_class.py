class Empolyee:
    language ="python" #this is a class attribute
    salary = 120000
    
samrat = Empolyee()
samrat.name ="samrat kumar sahu" 
#this is a instance attribute

print(samrat.name,samrat.language,samrat.salary)

rohan = Empolyee()
rohan.name ="rohan roro robinson"
print(rohan.name,rohan.language,rohan.salary)
#here name is instance attribute and salary and language are class attributes as they directly belong to the class
         