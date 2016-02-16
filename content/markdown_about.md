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

```
	# Topical header here.

	*Italicize this sentence.
```

Rendering:

----

# Topical header here.

*Italicize this sentence.*

----

Markdown's simplicity makes it readable and accessible, including for those who don’t know about coding. Even for those who are familiar with HTML, Markdown makes it easier to spot encoding errors.

## What are some of the shortcomings of Markdown (and how to overcome them)?

- [ ] citations

- [x] CommonMark

> John Gruber’s canonical description of Markdown’s syntax does not specify the syntax unambiguously.

> In the absence of a spec, early implementers consulted the original Markdown.pl code to resolve these ambiguities. But Markdown.pl was quite buggy, and gave manifestly bad results in many cases, so it was not a satisfactory replacement for a spec. Markdown.pl was last updated December 17th, 2004.

> Because there is no unambiguous spec, implementations have diverged considerably over the last 10 years. As a result, users are often surprised to find that a document that renders one way on one system (say, a GitHub wiki) renders differently on another (say, converting to docbook using Pandoc). To make matters worse, because nothing in Markdown counts as a “syntax error,” the divergence often isn’t discovered right away.

> There’s no standard test suite for Markdown; MDTest is the closest thing we have. The only way to resolve Markdown ambiguities and inconsistencies is Babelmark, which compares the output of 20+ implementations of Markdown against each other to see if a consensus emerges. 


[CommonMark](http://commonmark.org/) proposes to be a standard, unambiguous syntax [specification](http://spec.commonmark.org/) for Markdown, along with a suite of comprehensive tests to validate Markdown implementations against this specification. We believe this is necessary, even essential, for the future of Markdown.  CommonMark proposes a finalized 1.0 spec and test suite in early 2016.



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
