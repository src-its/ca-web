## How to Fork a Repo on GitHub?


- [x] explain what forking is and where it is useful
- [ ] detail how to fork

A fork is a copy of another repository this means it leaves the original repository unchanged.

---

A fork is an independent copy of a repository. As opposed to [cloning](/content/git_cloning.md), a forks acts as a sort of bridge between the original repository and your personal copy.[^git-guides_forking]


---


The main reason to fork a repository is to propose changes to someone elses project especially if you are not be part of the main team.

Otherwise, use forking to take someone else's source code and help build on it, using your own code and ideas.

---


One might wish to fork a repository if one wishes to make independent, customized changes to someone elses work or when you are not a permitted developer for a given repository.


---

When you click on "Fork" for a specific repository, you instantly create a copy of that repository.  Thus, if you have forked a repository and it is later changed, those changes are not updated on your forked repository.

If you want to keep updating you fork along with the main repository, you will have to use the "fetch" command.

If you are using terminal and you are pushing to your fork, only your fork will be updated.

--

When you fork a repository, any subsequent changes to the original repository will not be reflected in your fork until issuing a "fetch" command. If you want the changes you made to your fork, to also be included in the main repository, then after you fork, you must go into the main repository in GitHub, and create a pull request.


<!-- There are several concepts in the above paragraph that could be elaborated in greater detail. -->

--


If you want the changes you made to your fork to also be included in the main repository, then after you fork, you must go into the main repository in GitHub and create a pull request.

The owner of that repository will then take a look at your pull request and decide whether to keep it or not.

Author: Feston

----


## References:

* [GitHub Help: Fork A Repo](https://help.github.com/articles/fork-a-repo/)
* GitHub Guides. 2014. [Forking Projects](https://guides.github.com/activities/forking/) *GitHub Guides*

<!-- Add in-line citations to the main content body. -->

[^git-guides_forking]: https://guides.github.com/activities/forking/ "GitHub Guides. 2014. Forking Projects."

