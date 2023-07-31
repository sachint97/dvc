with open("artifact.txt","r") as f:
    text = f.read()
    print(text)

with open("artifact.txt","w") as f:
    f.write("added one line")

print("stage 3 ended")