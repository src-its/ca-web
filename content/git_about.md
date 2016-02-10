## What is Git?

Git is a piece of software that helps to manage revisions to a repository of files.

## What is Version Control?

Version control systems (VCS) are tools for making file management easier.  If you are working on any project over a period of time&mdash;be it alone or in a group&mdash;you are likely to make multiple changes to the same file.  Without VCS, the onus of trackign changes is yours alone.  VCS record the changes that you or your collaborators make to a project files for you. That is, as you change project files, your VCS keeps a record of these changes so that you can track the history of edits and can even revert a  file (or files) to a previous state. This way, if anyone on the project makes a mistake or a change that anyone else doesn't agree with, it is possible to revert that file to previous state. In other words, version control is a mean of recording incremental changes so that each iteration of a file can be accessed and restored, as neccessary.[^mcwilliams][^git_about-vcs]

## How is Git different from other Version Controls?

There are many 'version control systems' available; Git is just one. 

Git is a so-called distributed version control system, meaning that it allows a user to push and pull changes to another user's machines. No copy of a file or project directory is any better or 'greater' than any other;  all contributers are working on identical copies.[^mcwilliams]

Git is constantly keeping snapshots of all changes, instead of complete new file versions. So if a small change is made to a file, Git implements the change and leaves the rest of the content unchanged. It references the unchanged content from the previous version, instead of saving the new version as a separate new file. This makes Git lightweight and efficient in that it does not use a lot of space when changing the files.[^git_about-vcs][^git_basics]

<!--

##How to use Git?

In addition to installing Git locally in your machine, you also need a server to run Git in, which keeps all the stored files and their snapshots from every project collaborator. A great hosting server for Git is GitHub. For more information on Git vs GitHub, check out this article https://github.com/fkast/ca-web/blob/master/content/git-vs-github.md

[I am not sure that the content in this commented section helps to further the overall discussion of this article.]
-->

## References

```
[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""
[^git_about-vcs]: Git. ["About Version Control"] (https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
[^git_basics]: Git. ["Git Basics"] (https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

```


[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. "Is Git the Same Thing as Github!?""
[^git_about-vcs]: https://git-scm.com/book/en/v2/Getting-Started-About-Version-ControlGit. ["About Version Control"] (https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
[^git_basics]: https://git-scm.com/book/en/v2/Getting-Started-Git-BasicsGit. ["Git Basics"] (https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
