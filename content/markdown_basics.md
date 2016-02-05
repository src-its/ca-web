# A Bit About Markdown


Markdown refers to both:

1. a [markup syntax](http://en.wikipedia.org/wiki/Markup_language) that was designed as an "easy-to-read, easy-to-write plain text format"
1. a text-to-XHTML/HTML conversion tool, written in Perl 

The overriding design goal in initial formulation of Markdown’s formatting syntax was to make it as "readable" as possible. The idea is that any Markdown-formatted document can be publishable "as-is"--i.e., as plain text file that can be logically interpreted by an unfamiliar reader without having to process it's formatting syntax through some form of 'printing' application [unlike text formatted in other a markup languages, such as Rich Text Format (RTF) or HTML, which--in their raw form--are cluttered with tags and formatting instructions to an extent that makes them difficult for human consumption].

It is important to note that there is no clearly-defined Markdown standard.  The original writeup and implementation by John Gruber is referred to by some as 'vanilla' Markdown, with other "flavours" of the syntax being created as different vendors write their own variants of the language to correct flaws or add missing features.

Markdown can be [converted easily](Working-with-Pandoc) to other formatting and printing languages.  It is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

Markdown is free software, available under a [BSD-style open source license](http://daringfireball.net/projects/markdown/license).


# Markdown Cheatsheet


| **Type** | **Or** | **… to Get** |
|----------|--------|--------------|
||||
||||
||||
||||
||||
||||



----

> This cheatsheet is taken from [a Gist](https://gist.github.com/jonschlinkert/5854601) by Jon Schlinkert.  Rendering can be enabled using the [{{gist}} helper](https://github.com/assemble/handlebars-helpers#gist) [without it, code syntax colorization is not visible].


# Typography 

## Headings

Headings from `h1` through `h6` are constructed with a `#` for each level:

``` markdown
# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading
```

Renders to:

# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading

HTML:

``` html
<h1>h1 Heading</h1>
<h2>h2 Heading</h2>
<h3>h3 Heading</h3>
<h4>h4 Heading</h4>
<h5>h5 Heading</h5>
<h6>h6 Heading</h6>
```

<br>
<br>
<br>


## Horizontal Rules

The HTML `<hr>` element is for creating a "thematic break" between paragraph-level elements. In markdown, you can create a `<hr>` with any of the following:

* `___`: three consecutive underscores
* `---`: three consecutive dashes
* `***`: three consecutive asterisks

renders to:

___

---

***


<br>
<br>
<br>


## Body Copy 

Body copy written as normal, plain text will be wrapped with `<p></p>` tags in the rendered HTML.

So this body copy:

``` markdown
Lorem ipsum dolor sit amet, graecis denique ei vel, at duo primis mandamus. Et legere ocurreret pri, animal tacimates complectitur ad cum. Cu eum inermis inimicus efficiendi. Labore officiis his ex, soluta officiis concludaturque ei qui, vide sensibus vim ad.
```
renders to this HTML:

``` html
<p>Lorem ipsum dolor sit amet, graecis denique ei vel, at duo primis mandamus. Et legere ocurreret pri, animal tacimates complectitur ad cum. Cu eum inermis inimicus efficiendi. Labore officiis his ex, soluta officiis concludaturque ei qui, vide sensibus vim ad.</p>
```


<br>
<br>
<br>


## Emphasis

### Bold
For emphasizing a snippet of text with a heavier font-weight.

The following snippet of text is **rendered as bold text**.

``` markdown
**rendered as bold text**
```
renders to:

**rendered as bold text**

and this HTML

``` html
<strong>rendered as bold text</strong>
```

### Italics
For emphasizing a snippet of text with italics.

The following snippet of text is _rendered as italicized text_.

``` markdown
_rendered as italicized text_
```

renders to:

_rendered as italicized text_

and this HTML:

``` html
<em>rendered as italicized text</em>
```


### strikethrough
In GFM you can do strickthroughs. 

``` markdown
~~Strike through this text.~~
```
Which renders to:

~~Strike through this text.~~


<br>
<br>
<br>


## Blockquotes
For quoting blocks of content from another source within your document.

Add `>` before any text you want to quote. 

``` markdown
Add `>` before any text you want to quote. 
```

Renders to:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.

and this HTML:

``` html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
</blockquote>
```

Blockquotes can also be nested:

``` markdown
> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue. 
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi. 
>> Sed adipiscing elit vitae augue consectetur a gravida nunc vehicula. Donec auctor 
odio non est accumsan facilisis. Aliquam id turpis in dolor tincidunt mollis ac eu diam.
>>> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue. 
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi. 
```

Renders to:

> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue. 
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi. 
>> Sed adipiscing elit vitae augue consectetur a gravida nunc vehicula. Donec auctor 
odio non est accumsan facilisis. Aliquam id turpis in dolor tincidunt mollis ac eu diam.
>>> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue. 
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi. 


<br>
<br>
<br>


## Lists

### Unordered
A list of items in which the order of the items does not explicitly matter.

You may use any of the following symbols to denote bullets for each list item:

```markdown
* valid bullet
- valid bullet
+ valid bullet
```

For example

``` markdown
+ Lorem ipsum dolor sit amet
+ Consectetur adipiscing elit
+ Integer molestie lorem at massa
+ Facilisis in pretium nisl aliquet
+ Nulla volutpat aliquam velit
  - Phasellus iaculis neque
  - Purus sodales ultricies
  - Vestibulum laoreet porttitor sem
  - Ac tristique libero volutpat at
+ Faucibus porta lacus fringilla vel
+ Aenean sit amet erat nunc
+ Eget porttitor lorem
```
Renders to:

+ Lorem ipsum dolor sit amet
+ Consectetur adipiscing elit
+ Integer molestie lorem at massa
+ Facilisis in pretium nisl aliquet
+ Nulla volutpat aliquam velit
  - Phasellus iaculis neque
  - Purus sodales ultricies
  - Vestibulum laoreet porttitor sem
  - Ac tristique libero volutpat at
+ Faucibus porta lacus fringilla vel
+ Aenean sit amet erat nunc
+ Eget porttitor lorem

And this HTML

``` html
<ul>
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
  <li>Integer molestie lorem at massa</li>
  <li>Facilisis in pretium nisl aliquet</li>
  <li>Nulla volutpat aliquam velit
    <ul>
      <li>Phasellus iaculis neque</li>
      <li>Purus sodales ultricies</li>
      <li>Vestibulum laoreet porttitor sem</li>
      <li>Ac tristique libero volutpat at</li>
    </ul>
  </li>
  <li>Faucibus porta lacus fringilla vel</li>
  <li>Aenean sit amet erat nunc</li>
  <li>Eget porttitor lorem</li>
</ul>
```

### Ordered

A list of items in which the order of items does explicitly matter.

``` markdown
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem
```
Renders to:

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem

And this HTML:

``` html
<ol>
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
  <li>Integer molestie lorem at massa</li>
  <li>Facilisis in pretium nisl aliquet</li>
  <li>Nulla volutpat aliquam velit</li>
  <li>Faucibus porta lacus fringilla vel</li>
  <li>Aenean sit amet erat nunc</li>
  <li>Eget porttitor lorem</li>
</ol>
```

**TIP**: If you just use `1.` for each number, GitHub will automatically number each item. For example:

``` markdown
1. Lorem ipsum dolor sit amet
1. Consectetur adipiscing elit
1. Integer molestie lorem at massa
1. Facilisis in pretium nisl aliquet
1. Nulla volutpat aliquam velit
1. Faucibus porta lacus fringilla vel
1. Aenean sit amet erat nunc
1. Eget porttitor lorem
```

Renders to:

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem


<br>
<br>
<br>


## Code

### Inline code
Wrap inline snippets of code with `` ` ``.

For example, `<section></section>` should be wrapped as "inline".

``` html
For example, `<section></section>` should be wrapped as "inline".
```


### Indented code

Or indent several lines of code by at least four spaces, as in:

``` js
    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code
```

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


### Block code "fences"

Use "fences"  ```` ``` ```` to block in multiple lines of code. 

<pre>
``` html
Sample text here...
```
</pre>


```
Sample text here...
```

HTML:

``` html
<pre>
  <p>Sample text here...</p>
</pre>
```

### Syntax highlighting

GFM, or "GitHub Flavored Markdown" also supports syntax highlighting. To activate it, simply add the file extension of the language you want to use directly after the first code "fence", ` ``` js `, and syntax highlighting will automatically be applied in the rendered HTML. For example, to apply syntax highlighting to JavaScript code:

<pre>
``` javascript
grunt.initConfig({
  assemble: {
    options: {
      assets: 'docs/assets',
      data: 'src/data/*.{json,yml}',
      helpers: 'src/custom-helpers.js',
      partials: ['src/partials/**/*.{hbs,md}']
    },
    pages: {
      options: {
        layout: 'default.hbs'
      },
      files: {
        './': ['src/templates/pages/index.hbs']
      }
    }
  }
};
```
</pre>

Renders to:

``` javascript
grunt.initConfig({
  assemble: {
    options: {
      assets: 'docs/assets',
      data: 'src/data/*.{json,yml}',
      helpers: 'src/custom-helpers.js',
      partials: ['src/partials/**/*.{hbs,md}']
    },
    pages: {
      options: {
        layout: 'default.hbs'
      },
      files: {
        './': ['src/templates/pages/index.hbs']
      }
    }
  }
};
```

And this complicated HTML:

``` xml
<div class="highlight"><pre><span class="nx">grunt</span><span class="p">.</span><span class="nx">initConfig</span><span class="p">({</span>
  <span class="nx">assemble</span><span class="o">:</span> <span class="p">{</span>
    <span class="nx">options</span><span class="o">:</span> <span class="p">{</span>
      <span class="nx">assets</span><span class="o">:</span> <span class="s1">'docs/assets'</span><span class="p">,</span>
      <span class="nx">data</span><span class="o">:</span> <span class="s1">'src/data/*.{json,yml}'</span><span class="p">,</span>
      <span class="nx">helpers</span><span class="o">:</span> <span class="s1">'src/custom-helpers.js'</span><span class="p">,</span>
      <span class="nx">partials</span><span class="o">:</span> <span class="p">[</span><span class="s1">'src/partials/**/*.{hbs,md}'</span><span class="p">]</span>
    <span class="p">},</span>
    <span class="nx">pages</span><span class="o">:</span> <span class="p">{</span>
      <span class="nx">options</span><span class="o">:</span> <span class="p">{</span>
        <span class="nx">layout</span><span class="o">:</span> <span class="s1">'default.hbs'</span>
      <span class="p">},</span>
      <span class="nx">files</span><span class="o">:</span> <span class="p">{</span>
        <span class="s1">'./'</span><span class="o">:</span> <span class="p">[</span><span class="s1">'src/templates/pages/index.hbs'</span><span class="p">]</span>
      <span class="p">}</span>
    <span class="p">}</span>
  <span class="p">}</span>
<span class="p">};</span>
</pre></div>
```


<br>
<br>
<br>



## Tables
Tables are created by adding pipes as dividers between each cell, and by adding a line of dashes (also separated by bars) beneath the header. Note that the pipes do not need to be vertically aligned.


``` markdown
| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```

Renders to:

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

And this HTML:

``` html
<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>data</td>
    <td>path to data files to supply the data that will be passed into templates.</td>
  </tr>
  <tr>
    <td>engine</td>
    <td>engine to be used for processing templates. Handlebars is the default.</td>
  </tr>
  <tr>
    <td>ext</td>
    <td>extension to be used for dest files.</td>
  </tr>
</table>
```

### Right aligned text

Adding a colon on the right side of the dashes below any heading will right align text for that column.

``` markdown
| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


<br>
<br>
<br>


## Links

### Basic link

``` markdown
[Assemble](http://assemble.io)
```

Renders to (hover over the link, there is no tooltip):

[Assemble](http://assemble.io)

HTML:

``` html
<a href="http://assemble.io">Assemble</a>
```


### Add a title

``` markdown
[Upstage](https://github.com/upstage/ "Visit Upstage!")
```

Renders to (hover over the link, there should be a tooltip):

[Upstage](https://github.com/upstage/ "Visit Upstage!")

HTML:

``` html
<a href="https://github.com/upstage/" title="Visit Upstage!">Upstage</a>
```

### Named Anchors

Named anchors enable you to jump to the specified anchor point on the same page. For example, each of these chapters:

```markdown
# Table of Contents
  * [Chapter 1](#chapter-1)
  * [Chapter 2](#chapter-2)
  * [Chapter 3](#chapter-3)
```
will jump to these sections:

```markdown
## Chapter 1 <a id="chapter-1"></a>
Content for chapter one.

## Chapter 2 <a id="chapter-2"></a>
Content for chapter one.

## Chapter 3 <a id="chapter-3"></a>
Content for chapter one.
```
**NOTE** that specific placement of the anchor tag seems to be arbitrary. They are placed inline here since it seems to be unobtrusive, and it works.


<br>
<br>
<br>


## Images
Images have a similar syntax to links but include a preceding exclamation point.

``` markdown
![Minion](http://octodex.github.com/images/minion.png)
```
![Minion](http://octodex.github.com/images/minion.png)

or
``` markdown
![Alt text](http://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")
```
![Alt text](http://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

``` markdown
![Alt text][id]
```
![Alt text][id]

With a reference later in the document defining the URL location:

[id]: http://octodex.github.com/images/dojocat.jpg  "The Dojocat"


    [id]: http://octodex.github.com/images/dojocat.jpg  "The Dojocat"



## Citations and References



Citations in HTML are generally achieved as such:

```
Quote here.

-- <cite>Benjamin Franklin</cite>

```

Quote here.

-- <cite>Benjamin Franklin</cite>



Citations and References are treated differently by different flavours of Markdown:



GitHub Flavored Markdown doesn't support footnotes, but you can manually fake it¹ with Unicode characters or superscript tags, e.g. `<sup>1</sup>`.

<sup>1</sup>Of course this isn't ideal, as you are now responsible for maintaining the numbering of your footnotes. It works reasonably well if you only have one or two, though.

Expanding a little bit on the previous answer, you can make the footnote links clickable here as well. First define the footnote at the bottom like this

`<a name="myfootnote1">1</a>: Footnote content goes here`
Then reference it at some other place in the document like this

`<sup>[1](#myfootnote1)</sup>`




[Fletcher Penny’s MultiMarkdown](http://fletcherpenney.net/multimarkdown/) adds additional features to Markdown especially useful for academics.

MultiMarkdown gives writers a greater range of tools for writing more complex material. Footnotes, for example, are represented by [^1] and correspond to the note such as:

```
This sentence needs a citation.[^1]

[^1]: This is the citation.
```

If you are using Pandoc for transforming text, you can use its flavor of Markdown to do inline footnoting.^[Which looks something like this.]

If things start getting a little messy, Dr. Drang has a [Python script that will clean up Markdown reference links](http://www.leancrew.com/all-this/2012/09/tidying-markdown-reference-links/).

Because we typically want to list the citations as references at the end of the document, reference-style links should be preferred over inline links. From the markdown syntax documentation:

```
This is [an example][id] reference-style link.

[id]: http://example.com/  "Optional Title Here"
```

Results in:

This is [an example][id] reference-style link.

[id]: http://example.com/  "Optional Title Here"


It might be tempting to use sequential numbers as id for the reference-style links, but the order of links can of course change during writing. It may make sense to think of the id in reference-style links as a citekey, and people should be free use that functionality of their reference manager. The citekey is used to link to the reference list at the bottom of the document, different from linking to the citekey in a separate bibtex file.

All of the above can be done in any text editor. This also includes the text editor that scholars spend most of their time with - their email program. Reference-style citations in an email are very readable, and also actionable since they are links and not text with bibliographic information.

One problem with this approach is of course that all links are inline in the resulting HTML, without a references section at the end of the document. This may be fine, as we can provide citation information in the title attribute, available upon hovering over the link (try hovering over [this link](http://dx.doi.org/10.1371/journal.pmed.0020124 "Ioannidis JPA. Why Most Published Research Findings Are False. PLoS Medicine. Public Library of Science; 2005;2(8):e124. Available from: http://dx.doi.org/10.1371/journal.pmed.0020124"), the journal eLife is doing [something similar](http://dx.doi.org/10.7554/eLife.00633)). The markdown could look like this (using the Vancouver citation style):

```
[@Ioannidis2005]: http://dx.doi.org/10.1371/journal.pmed.0020124 "Ioannidis JPA. Why Most Published Research Findings Are False. PLoS Medicine. Public Library of Science; 2005;2(8):e124. Available from: http://dx.doi.org/10.1371/journal.pmed.0020124"
```

The title attribute now of course uses a citation style, but this is optional information and can easily be reformatted as we have the DOI.

Or we break away from standard markdown and display reference-style links at the end of the document - similar to [footnotes](http://rephrase.net/box/word/footnotes/syntax/), which are also not part of standard markdown. But this is just a display issue that can be solved, and the solution might look different depending on whether the output is HTML, PDF or XML. This document for example contains 14 reference-style citations.

There is obviously a need for tools that make adding citations to scholarly markdown easier. This could be accomplished by relatively small changes to existing reference managers (enabling copy/paste of citations in reference-style markdown format), or by tools similar to the [knitcitations](http://carlboettiger.info/2012/05/30/knitcitations.html) and [kcite](http://wordpress.org/plugins/kcite/).


### References:

* [Daring Fireball: Markdown](http://daringfireball.net/projects/markdown/)
* [Wikipedia: Markdown](http://en.wikipedia.org/wiki/Markdown)
* [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)
* [Markdown Basics](https://help.github.com/articles/markdown-basics/)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

* [GitHubGist: jonschlinkert/markdown.md](https://gist.github.com/jonschlinkert/5854601)
* [Jason Heppler. 2012. "Using Markdown Like an Academic". *Gradhacker.org*](http://www.gradhacker.org/2012/11/20/using-markdown-like-an-academic/)
* [Martin Fenner. 2013. "Citations in Scholarly Markdown"](http://blog.martinfenner.org/2013/06/19/citations-in-scholarly-markdown/)
* [Martin Fenner. 2010. "Citations are links, so where is the problem?"](http://blog.martinfenner.org/2013/06/19/citations-in-scholarly-markdown/)
* [CommonMark: A strongly defined, highly compatible specification of Markdown](http://commonmark.org/)
* [MultiMarkdown Syntax Guide](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide)

* ["Bibliographies and Citations". *R Markdown*](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
