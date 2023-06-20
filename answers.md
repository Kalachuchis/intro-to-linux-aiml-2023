1. List all the directories
```ls```

2. Copy folder_0 and all its contents into folder_1
```cp -r folder_0 folder_1```

3. Delete all the contents in folder_0 and create 3 new text files
```rm folder_0/* && touch folder_0/new_file{1..3}.txt```

5. Move the contents of folder_3 to folder_4
```mv folder_3/* folder_4```

6. List all the contents of all the directories with a single command
```ls folder_*```

OPTIONAL:
7. Move all the contents of folder_2, folder_3, folder_4 to its parent folder
```mv folder_[2-4]/* ./```

8. Delete all the content in current directory
```rm -rf *```
