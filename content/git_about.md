## What is Git?

Git is a piece of software that helps manage revisions to a repository of files.

## What is Version Control?

Version control systems (VCS) are tools used to make file management easier.  If you are working on any project over a period of time&mdash;be it alone or in a group&mdash;you are likely to make multiple changes to the same file.  Without VCS you would be responsible for tracking all of your changes.  A VCS records the changes so that you can track the history of edits and can even revert a  file (or files) to a previous state if needed. This way, mistakes or a changes can be reverted to a previous state.

In other words, version control is a mean of recording incremental changes so that each iteration of a file can be accessed and restored, as neccessary.[^mcwilliams] [^git_about-vcs]

## How is Git different from other Version Control Systems?

There are many version control systems available; Git is just one. 

Git is a so-called distributed version control system, meaning that it allows a user to push and pull changes to another user's machine. No copy of a file or project directory is any better or 'greater' than any other;  all contributers are working on identical copies.[^mcwilliams]

Git is constantly keeping snapshots of all changes, instead of complete new file versions. So if a small change is made to a file, Git implements the change and leaves the rest of the content unchanged. It references the unchanged content from the previous version, instead of saving the new version as a separate new file. This makes Git lightweight and efficient because it does not use a lot of space when changing the files.[^git_about-vcs] [^git_basics]

<!--

##How to use Git?

In addition to installing Git locally in your machine, you also need a server to run Git in, which keeps all the stored files and their snapshots from every project collaborator. A great hosting server for Git is GitHub. For more information on Git vs GitHub, check out this article https://github.com/fkast/ca-web/blob/master/content/git-vs-github.md

[I am not sure that the content in this commented section helps to further the overall discussion of this article.]
-->

## References

* Andrew McWilliams. ["Is Git the Same Thing as Github!?"](https://jahya.net/blog/git-vs-github/)
* Git. ["About Version Control"](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
* Git. ["Git Basics"](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

[^mcwilliams]: https://jahya.net/blog/git-vs-github/ "Andrew McWilliams. 'Is Git the Same Thing as Github!?'"
[^git_about-vcs]: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control "Git. 'About Version Control'"
[^git_basics]: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics "Git. 'Git Basics'."
