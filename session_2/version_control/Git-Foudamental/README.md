# Inittilize Empty Reopsitry
```python
git init
```
- For seeing the  empty repo run this command b/c by default file is hidden
```python
ls -la
```

- For see the status
```python
git status
```

- After seeing status add the files or single file
```pthon
git add .
```
- **OR**
```python
git add <file name>
```

- After adding commit the files
```python
git commit -m "Your commit."
```

-- See the log 
```python
git log
```
# Check the difference b/w previous and change file
```python
git diff file_name
```

# Checkout any previous version
```python
git checkout your_commit_code -- filename
```

# Working with `git restore`
- **Case1**
    - To Undo Changes, get the last successfull change
    ```python
        git restore file_name
    ```
- **Case2**
    - If we can add the chages using git add.
    ```python
    git restore --staged filename
    ```
- **Case3**
    - Add changes to staging area(did't commit) after this add more files.
    ```python
    git restore --worktree filename
    ``` 
# Useful tips for `git log`
- **Last2 commit**
    ```python
        git log -p -2
    ```
- **Summary of changes**
    ```python
    git log --stat
    ```
- **Check commit in oneline**
    ```python
    git log --pretty=oneline
    ```
**or**
    ```python
    git log --pretty=format:"%h - %an, %ar:%s"
    ```
**OR**
```python
git log -S name_of_fun
```
**Searching any thing**
```python
git log --grep "any string"
```

**See the specific user commit**
```python
git log --author="sami"
```

# Working with remote `repe`
**Check the origin**
```python
git remote
```
**or**
```pthon
git remote -v
```

# Git `pull`
- If we can changes on github it is necessary to `pull` the change.
```python
git pull origin main
```

# Understanding `Git clone`
- we can clone any repo
```python
git clone url_of_the_repo
```

# Branching and merging
- **Creating new branch**
```python
git branch new_branch_name
```
- **Switch the branch as needed**
```python
git checkout branch_name
```

# Merging
- **After the successfull changes in new branch merge them.**
- **First go to main branch and then merge.**
```python
git merge new_branch_name
```
# Git Forking and Pull Request
- Fork is nothing it is some thing that any user can fork our repo and add some changes and then create a pull reaques for merging.
- Also some body can add more feature if feature are good owner can add them