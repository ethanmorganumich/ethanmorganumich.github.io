import sys
import os

# pandoc -f markdown -t html5 -o "ouptut-1.html" "input-1.md" 
# pandoc -f markdown -t html5 -o "ouptut-2.html" "input-2.md" -c "style.css"
mdFiles = os.listdir("./build/blog")

command = """pandoc -f markdown -t html5 -o "./source/blog/?.html" "build/blog/?.md" --template "./build/template.html" """
gitcommand= """ git add ./source/blog/?.html """

for file in mdFiles:
    print(command.replace("?", file[:-3]))
    print(gitcommand.replace("?", file[:-3]))
    os.popen(command.replace("?", file[:-3]))
    os.popen(gitcommand.replace("?", file[:-3]))


# making main
 
mainCommand = """pandoc -f markdown -t html5 -o "./source/blog.html" build/blog/*.md --template "./build/template.html" """
os.popen(mainCommand)
os.popen("git add ./source/blog.html")