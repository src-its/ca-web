## How to Fork a Repo on GitHub?


- [x] explain what forking is and where it is useful
- [ ] detail how to fork


When you click on "Fork" on GitHub for a specific repository, you create a copy of that repository. Your fork copy is independent of the original repository. That is, as opposed to [cloning](/content/git_cloning.md), a forks acts as a sort of bridge between the original repository and your personal copy.[^git-guides_forking]

One might wish to fork a repository if one wishes to make independent, customized changes to someone elses work or when you are not a permitted developer for a given repository.


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

