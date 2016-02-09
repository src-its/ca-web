## What is Git?

Git is a piece of software that helps to manage revisions to a repository of files.

## What is Version Control?

At its core, version control systems are tools for making file management easier.  When you start working on a project, alone or in a group, you will be updating your files at one time or another, and this is when 'version control' comes into play. All the changes you or your collaborators do to the project files is recorded. That is, the new changes are added to the project files, but 'version control' makes sure to also keep a history and/or copies of all the files in their previous state. Now, if one of people in the project makes a mistake in any of the files, or if you decide that a previous idea you worked in was better, you look back into the history 'version control' created and manages for you, and you can access all the files in their previous state. To put it simply "version control is a system for recording incremental changes." There are many other 'version controls' out there other than Git.[^mcwilliams][ref2]

##How is Git different from other Version Controls?

Usually most 'version control' systems keep track and store their information as a list of file changes. When changes are made to any of the files, the new versions of the files are saved on top of the previous versions. Git is more efficient in that it uses a 'snapshot' system. Git is constantly keeping snapshots of all changes, instead of complete new file versions. So if a small change is made to a file, Git implements the change and leaves the rest of the content unchanged. It references the unchanged content from the previous version, instead of saving the new version as a separate new file. This makes Git lightweight and efficient in that it does not use a lot of space when changing the files. [ref2][ref3]

##How to use Git?

In addition to installing Git locally in your machine, you also need a server to run Git in, which keeps all the stored files and their snapshots from every project collaborator. A great hosting server for Git is GitHub. For more information on Git vs GitHub, check out this article https://github.com/fkast/ca-web/blob/master/content/git-vs-github.md

## References

```
[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""
```


[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""

ref 2: Git. ["About Version Control"] (https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

ref 3: Git. ["Git Basics"] (https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
