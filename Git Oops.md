autoscale: true  
slidenumbers: true  
theme: Next, 3
slide-transition: fade(0.3)

# [fit] Git Oops
# [fit] How I stopped worrying and love the Git[^*]


<br/>

```swift
let author = "Konstantin Portnov"
let github = "github.com/x0000ff"
```

![inline](./img/wallapop.png)

![right](https://octodex.github.com/images/privateinvestocat.jpg)

[^*]: the Private Investocat (c) https://octodex.github.com/privateinvestocat/

---

# ☝️ First things first
## Probably I won't see chat

![inline](./img/rules.jpg)

---

# 😕 Have you ever felt confused using Git?
![inline](./img/wtf.png)

---

# 😐 Have you ever said "it's not my code" inspecting your Pull Request?
![inline](./img/monkey-puppet.jpg)

---

# 😖 Have you ever lost your code?
![inline](./img/confused-travolta.gif)

---

# 🤫 Have created commits "Missed files" ,"Oops" etc?
![inline](./img/missed-files.jpg)

---

# 🥸 Why are we here?

1. Stop to worry
2. Take total control
3. Zero surprises

![right](./img/frog.jpg)

---

# What is Git? 
# <br/> 
# 🎤

![right](./img/wtf-is-this-john.gif)


---

# 🤔 What is Git?

[.build-lists: true]

1. Database
2. Time machine
3. Something else?

[.build-lists: false]

---

# 🕵️‍♂️ Let's have a closer look

[.build-lists: true]

[.column]

**Commit has**

- Author
- Message
- Hash (SHA-256)
- Parent Hash (optional)

[.column]

![inline](./img/3-commits.png)

[.build-lists: false]

---


[.build-lists: true]

# Looks similar, no?

![inline](https://img.money.com/2022/06/What-Is-Blockchain-Infographic.jpg)

---

# 🧙‍♂️ Reset 

---

# Commit creation


![fit inline](./img/commit.png)

---

# How does the `reset` work?


![fit inline](./img/reset.png)

---

# 🛝 Demo time 

---


# 😰 Missed commits

[.column]

You you don't see something in the **git log** or your **GUI client**, that **doesn't mean**, that the changes is **lost**.

If you did commit - you're saved :) 

[.column]

![inline](./img/git-out.png)  

---

# 🏎💨 Fast travel

```shell
$ git reset --hard <commit-ish>
```

===

> Do not forget do `git push --force`
> It's safe if you work alone in the branch

---

# 🗺 Use **tags** as breadcrumbs

Do not push them to remote 🙏

![inline](./img/mole.gif)

---

# 🛝 Bonus Demo time 

---

# 📝 Cheatsheet

| Command | What does? |
| --- | --- |
| `git reset --hard head~N` | Force change current branch head N commits back [^⚠️]
| `git reset --mixed head~N` | Cancel N commits. All changes are **unstaged** [^⚠️]
| `git reset --soft head~N` | Cancel N commits. All changes are **staged** [^⚠️]
| |
| `git tag <NAME>` | Create a tag
| `git tag -d <NAME>` | Remove a tag
| |
| `git cherry-pick <REVISION>` | Duplicates a commit to current branch
| `git reflog` | See histroy of changes of the current branch head
| `git commit --amend --no-edit` | Add all the staged changes to the last commit [^⚠️]

[^⚠️]: `push --force` needed


---

# 🥸 Why are we here?

1. Stop to worry
2. Take total control
3. Zero surprises

![right](./img/frog.jpg)

---

# 🎉 Fin

---

# ☺️ Thanks a lot!

![30% right fit](./img/common/thanks.jpg)

---

# 🤔 Q & A

![inline](./img/qr.png)

## `github.com/x0000ff/git-oops`
