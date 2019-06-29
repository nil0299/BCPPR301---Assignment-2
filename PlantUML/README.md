# BCPR301 Assignment 2
# Smell Detection
## Bad Smell 1
Name: Large Class
Location: PlantUML/module_builder/class_builder.py/ClassBuilder/ (between lines 6-77)
Reasons why it is bad:
1.	It is quite a large class (77 lines of code)
2.	It has long methods, where some methods are repeated. This makes it harder to extend for further functionality as it is performing more than one task, which makes it difficult to understand e.g. the print_class method (lines 60-76) is performing more than one task and repeating some
3.	There are lots of methods doing too many things, therefore, it is harder to debug and extend e.g. the print_class method (lines 60-76)
4.	It is hard to read as the class is so long you don’t know what method relates to what section
