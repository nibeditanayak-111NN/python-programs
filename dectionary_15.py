student ={
"name":"nibedita nayak",
"age":19,
"adult":True,
"mark":95,
"branch":"cse",
"sgpa":8.5,
"collage":"giet",
}
print(student["mark"])
print(student["name"])
print(student.get("father"))
student["city"]= "delhi"
student["markes"]=88
student.pop("adult")
student.popitem()
print(student.keys())
print(student.values())
print(student.items())
student.update({"grade":"A"})
student_1=student.copy()
print(student_1)
#student.clear()
print(student)
school= {
"studentA":{"name":"nibedita","house":"kalagada"},
"studentB":{"name":"bibek","house":"balsahi"}
}
print(school)