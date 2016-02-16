## What is Markdown and Why Do We Use it?

Markdown was developed in 2004 by John Gruber, who wrote the first markdown-to-html converter in Perl that has become widely used in web applications. [^commonmark] It is a simple language and software tool used by web writers to convert plain text into HTML. According to its creator, John Gruber, the design goal of Markdown “is to make it as readable as possible”.

<!-- Citation needed for comment above -->

Markdown can be considered both a lazy and an efficient way to write HTML. It allows one to simply define elements such as headers, links, but reduces the jargon and extranious coding required by HTML.

Consider writing this:

```
	<p> <!--Creating a new page. -->
	<h1>Topical header here.</h1>
	<p><i>Create this paragraph line. Italicize this sentence.</i></p>
	</p> <!-- End page. -->
```

To get the same output in Markdown:

	`*Italicize this sentence.*`

Rendering:

*Italicize this sentence.*

Markdown's simplicity makes it readable and accessible, including for those who don’t know about coding. Even for those who are familiar with HTML, Markdown makes it easier to spot encoding errors.

<!-- 

NOTE: At some point we should introduce a discussion about how Markdown is currently without a 'standard'.

Flavours  of Markdown include:

* John Gruber’s original Markdown
* Github-flavored Markdown
* PHP Markdown Extra
* Pandoc
* MultiMarkdown

-->

[^commonmark]:http://commonmark.org/ CommonMark. 2016 "What is Markdown?" 
