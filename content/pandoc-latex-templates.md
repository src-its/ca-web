# Using LaTeX Templates with Pandoc Conversions: Introduction #
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Why would one want to style as sheet with a LaTeX template, yet write it in Markdown? There are quite a few, but perhaps the most important motivator is that Markdown is just straight up easier to learn and use (though LaTeX itself is actually a rather simple language to learn). 
## Install Pandoc ##
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If you have yet to do so, make sure that you have Pandoc installed somewhere and verify that it is indeed installed. To do this, run the command prompt or terminal (depending on if you run Windows or Linux/Mac). Now type into the terminal `pandoc --version`. It should display the version of Pandoc that you have installed. If you get an error, see [the Pandoc installation guide](http://pandoc.org/installing.html). 
## Converting To LaTeX ##
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Now that we have all that cleared up, we can get into converting out .md files into .tex files with a fancy new LaTeX template. Under the assumption that your template file is in the same directory as the file you want to convert, open the terminal and navigate to that directory. From here, all you have to do is type `pandoc -s --template="your-template.latex" -o you_output.pdf` and that should do it.
<br />
<br /> 
Sources:<br />
http://los-pajaros-de-hogano.blogspot.com/2015/01/pandoc-customized-latex-templates-for.html
<br />
<br />
<br />
-Connor Lehman, Simon's Rock ITS 2016