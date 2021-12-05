from person import * #importing from the library created in 'person' file
#The import statement in Python imports code from one module into another.
#you can import all the code from the module you want to import from the import keyword followed by the module

student1= student('M00850971 ','Sirajuddin ','Sayed ','9th Oct 2002' ,'Male ','Indian ','Student ','Year 1','Computer Engineering and Informatics','40,700')
#created an object 'student1' containing answers with respect to the attributes created

student2= student('M00864218 ','Yash ','Mittal ','3rd April 2002' ,'Male ','Indian ','Student ','Year 2','Computer Engineering and Informatics','55,700')
#created an object 'student2' containing answers with respect to the attributes created

student3= student('M00415896 ','Shruti ','Balani ','21st June 2002' ,'Female ','Indian ','Student ','Year 3','Computer Engineering and Informatics','48,500')
#created an object 'student3' containing answers with respect to the attributes created

print(' Student1:'+ student1.__str__())
print(' Student2:'+ student2.__str__())
print(' Student3:'+ student3.__str__())
#printing the final output of the student details and teacher details

