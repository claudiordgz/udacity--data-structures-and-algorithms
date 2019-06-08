#  Finding Files

## Approved functions

```
os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)
```

## Forbidden functions

```
os.walk()
```

Our primary requirement is to find all paths recursively, and there is no mention or complexity or using Stacks or Queues to solve this. So we will answer it recursively. 

This method will check any directory recursively, which will run out of stack quickly if we have a very nested directory tree. Another way to do it is to keep a queue of the directories we need to check, and exhaust that queue as we go. Both solutions will have to check each file descriptor, whether it is a directory or a file. 

Time Complexity is `O(n)` because we will be checking every file.
