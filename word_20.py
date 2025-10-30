sentence=input("enter anything you want to print:")
word=""
for char in sentence:
    if char!=" ":
     word=word+char
    else:
       if word!="":
          print(word)
          word=""
if word!="":
       print(word)    
