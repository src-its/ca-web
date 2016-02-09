## What is Git?

<<<<<<< HEAD
Git is a piece of software that you install locally on your computer which handles 'version control' for you.[ref1] 

## What is Version Control?

In the modern era, using computers to do different projects in different fields is crucial or just makes your life easier. When you start working on a project, alone or in a group, you will be updating your files at one time or another, and this is when 'version control' comes into play. All the changes you or your collaborators do to the project files is recorded. That is, the new changes are added to the project files, but 'version control' makes sure to also keep a history and/or copies of all the files in their previous state. Now, if one of people in the project makes a mistake in any of the files, or if you decide that a previous idea you worked in was better, you look back into the history 'version control' created and manages for you, and you can access all the files in their previous state. To put it simply "version control is a system for recording incremental changes." There are many other 'version controls' out there other than Git[ref1][ref2]

##How is Git different from other Version Controls?

Usually most 'version control' systems keep track and store their information as a list of file changes. When changes are made to any of the files, the new versions of the files are saved on top of the previous versions. Git is more efficient in that it uses a 'snapshot' system. Git is constantly keeping snapshots of all changes, instead of complete new file versions. So if a small change is made to a file, Git implements the change and leaves the rest of the content unchanged. It references the unchanged content from the previous version, instead of saving the new version as a separate new file. This makes Git lightweight and efficient in that it does not use a lot of space when changing the files. [ref2][ref3]

##How to use Git?

In addition to installing Git locally in your machine, you also need a server to run Git in, which keeps all the stored files and their snapshots from every project collaborator. A great hosting server for Git is GitHub. For more information on Git vs GitHub, check out this article https://github.com/fkast/ca-web/blob/master/content/git-vs-github.md
=======
Git is a piece of software that helps to manage revisions to a repository of files.

## What is Version Control?

Let's say you have some new project, and you are planning to store all the files for that project in some new directory. You know that as time goes on, the files in this project will change - a lot. Things could get messy, and who knows when you might need to revert back to a previous working version of what you had?[^mcwilliams]

So, you install Git, then use it tp create the new project directory. You also tell Git that you would like to keep a history of the changes you make within that directory. Then, you add some files to kick off your project. The files you just added represent the first incremental step on the journey of your project. So you tell Git to take a snapshot. Then you make a small change - your next incremental step. So you take another snapshot. And that's about it: version control is a system for recording incremental changes.  The Git version control system (VCS) allows you to  step back and forth whenever necessary through each snapshot (aka version) of your project directory.[^mcwilliams]

Git is just one among many version control systems out there.  It is a so-called distributed version control system, meaning that Git has commands that allow you to push and pull your changes to other people's machines. Neither copy of the project directory is any better or 'greater' than any other - you are both collaborating on identical copies. This is a good thing, and Git gives you the power to work on your own copy as-is until you are ready to pull in your collaborator's changes, and push back your own changes.[^mcwilliams]


## References
>>>>>>> upstream/master

```
[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""
```

<<<<<<< HEAD
ref 2: Git. ["About Version Control"] (https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

ref 3: Git. ["Git Basics"] (https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
=======
[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""

Test
>>>>>>> upstream/master
