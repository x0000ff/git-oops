# Git: Oops

![](./cover.png)

- [Source](./Git%20Oops.md)
- [Generated PDF](./Git%20Oops.pdf)

> PDF is outdated. Deckset crashes on export 😔  
> Presentation was made with [Deckset](https://www.decksetapp.com) and [MacDown](https://macdown.uranusjr.com/)

## Cases

### Amend Last Commit

1. Typo in last commit -> `commit --amend`
2. Forgot to add a file -> `commit --amend --no-edit`

### Recreate Last Commit

1. Typo in last commit -> `reset --soft`
2. Forgot to add a file -> `reset --soft`

### Recreate Last N Commit

1. Typo in last commit -> `reset --soft head~3`

### Join last 3 commits

0. Mark with tag `before-join`
1. `reset --soft head~3` + `commit -m "2 + 3 + 4`

### Remove commits / Fast Travel

1. I gon't need last 2 commits -> `reset --hard head~2`
2. Oops... Identify dissappeared commit -> `reflog`
3. Use `show`
4. Use `cat-file -p`
4. Take only commit `head~2` -> `cherry-pick`

### Why commits have different hashes?

1. Add tag
2. `reset --soft head~1`
3. Create a tag with the same message
4. Why do they have different hashes?