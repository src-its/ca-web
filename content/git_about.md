## What is Git?

Git is a piece of software that helps to manage revisions to a repository of files.

## What is Version Control?

Let's say you have some new project, and you are planning to store all the files for that project in some new directory. You know that as time goes on, the files in this project will change - a lot. Things could get messy, and who knows when you might need to revert back to a previous working version of what you had?[^mcwilliams]

So, you install Git, then use it tp create the new project directory. You also tell Git that you would like to keep a history of the changes you make within that directory. Then, you add some files to kick off your project. The files you just added represent the first incremental step on the journey of your project. So you tell Git to take a snapshot. Then you make a small change - your next incremental step. So you take another snapshot. And that's about it: version control is a system for recording incremental changes.  The Git version control system (VCS) allows you to  step back and forth whenever necessary through each snapshot (aka version) of your project directory.[^mcwilliams]

Git is just one among many version control systems out there.  It is a so-called distributed version control system, meaning that Git has commands that allow you to push and pull your changes to other people's machines. Neither copy of the project directory is any better or 'greater' than any other - you are both collaborating on identical copies. This is a good thing, and Git gives you the power to work on your own copy as-is until you are ready to pull in your collaborator's changes, and push back your own changes.[^mcwilliams]


## References

```
[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""
```

[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""
