#Jayden Williams
#9/19
#Mad Libs
word1 = input("enter a difficulty")
word2= input("enter a verb")
word3=input("enter a website www.example.com")
word4=input("enter a noun")
word5=input("enter a noun")
word6=input("enter an adjective")
word7=input("enter a noun ending with er")
word8=input("enter a noun ending with s")
word9=input("enter a language type")
word10=input("enter an adjective")
story = str.format(""" Python is a {} to learn, {} programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with
its interpreted
nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the {} Web site, https://{}/, and may be freely distributed.
The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
The Python interpreter is easily extended with new {} and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for {} applications.
This tutorial introduces the {} informally to the basic concepts and features of the Python language and system.
It helps to have a Python interpreter handy for {}-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.
For a description of standard objects and modules, see The Python Standard Library.
The Python Language Reference gives a more formal definition of the language {}.
To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature.
Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s {} and style.
After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library. """,word1,word2,word4,word3,word5,word6,word7,word8,word9,word10)
print(story)
input()
