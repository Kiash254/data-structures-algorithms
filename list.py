print("****** WELCOME TO DATA STRUCTURES AND ALGORITHMS *********")
print(" ---- DONE BY KIASH -----")
print("DATA STRUCTURES - this shows how data are stored in a program")
print("ALGORITHM - these  are set steps by steps  instructions used to  solve a problem of a given bussiness logic")
print("** LIST CONCEPT **")
print("LIST- is used to store data in an ordered which is used to store diffrent data types unlike arrays below is an example")
list=[1,2,3,4,6,"one","Two"]
print("this is a list",list)
print("oparations on list")
postive=list[3]
print("indexing in a postive method",postive)
print("negative indexing")
negative=list[-3]
print("this is a method on negative indexing",negative)
print("slicing")
slicing=list[1:4]
print("this is a method on slicing",slicing)
print("adding elements to a list")
list.append("kiash")
print("this is a method on adding elements to a list",list)
print("removing elements from a list")
list.remove("kiash")
print("Removing kiash from a list",list)
print("removing elements from a list using pop")
list.pop(1)
print("removing elements from a list using pop",list)
print("removing elements from a list using del")
del list[1]
print("removing elements from a list using del",list)
print("removing elements from a list using clear")
list.clear()
print("removing elements from a list using clear",list)
#nesting list inside a list
print("nesting list inside a list")
list1=[1,2,3,["kiash","loves","what","he","does"],4,5,['dedicated','programmer','from','karatina']]
print("this is a nested list within a list",list1)


