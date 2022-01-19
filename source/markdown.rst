Brief introduction to Markdown
------------------------------

`Markdown <https://en.wikipedia.org/wiki/Markdown>`__ is a markup
language to create rich text and designed to make it easy to read and
write using just plain text editors. It serves similar purpose as html
language (another markup language) to format text on web pages. It is
becoming quite common and becoming a sort of standard language people
use to format text in places like Github or in other code repositories.
Other similar markup languages are
`Textile <https://en.wikipedia.org/wiki/Textile_(markup_language)>`__
and
`reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`__.

In this course, I will be teaching you to learn to use this markup
language to format text and documents that may need to be submitted as
reports or research projects. We will go into those in a little later.
Even in Jupyter lab, you will see that it uses Markdown to format text
so that it is easy to write/read and to quickly publish.

Basic Markdown syntax can be found here:
https://www.markdownguide.org/basic-syntax/

Basic syntax
~~~~~~~~~~~~

A few basic things about Markdown syntax here. If you want to write a
header line, you provide “#” sign in front of the text. You can put 1,
2, or 3 “#” signs in front of some text and it will format different
levels of headers for you. For example, if you type like this in a
Markdown file:

::

   # Text
   ## Text
   ### Text

When rendered properly, your web browser will display the headers like
these:

Text
====

.. _text-1:

Text
----

.. _text-2:

Text
~~~~

So this means, the more # you have in front of some text, the smaller
the font size becomes. You can go down to 6 levels of heading. One thing
to make sure though is that you leave a space between the “#” sign and
the text.

Another thing you want to learn to use is to make some text either
**bold** or *italicized*. You do this by typing like this:

::

   **bold text**

   *E. coli*

And they will be rendered like this:

**bold text**

*E. coli*

So, if you quote text inside 2 \* signs, you get a bold text. If you put
text inside single \* signs, then you get an italicized text.

Lists
~~~~~

If you want to create a numbered list, you can type like this:

::

   1. A
   1. B
   1. C

And it will automatically number them for you like this:

1. A
2. B
3. C

To create bullet lists, you can type like this:

::

   - text
   - text
     - A
     - B
     - C
   - text
   - text

And it will render it like this:

-  text
-  text

   -  A
   -  B
   -  C

-  text
-  text

Instead of using a “-”, you can also use \* and + symbols for lists.

Code
~~~~

To denote a word or phrase as code, enclose it in backticks (`). For
example, if you want to indicate a Unix command, such as “ls”, you can
type \`ls\` to highlight the Unix command. And it will render like this:

``ls``

If you have a code snippet that you want to render using rich text and
syntax highlighting, you can type like this:

\```bash

for i in 1 2 3 4;do

::

   echo ${i}

done

\``\`

And it will render like this:

.. code:: bash

   for i in 1 2 3 4;do
       echo ${i}
   done

Note that I type “bash” after the first 3 backticks to tell the program
that I want to highlight the syntax for ``bash`` programming language.
And the rendering engine in Jupyter formatted it with color to highlight
special key words and variables in ``bash``. Many Markdown processors
will recognize various programming languages and will automatically
highlight them for you if you specify which language it is supposed to
be in.

Tables
~~~~~~

You can also create nice-looking tables in Markdown. For example, if you
want to create a simple 2-columns, 3-rows table, you can type like this:

::

   | Syntax      | Description |
   | ----------- | ----------- |
   | Header      | Title       |
   | Paragraph   | Text        |

In Jupyter, it will render it like this:

========= ===========
Syntax    Description
========= ===========
Header    Title
Paragraph Text
========= ===========

You can align text within the cells to be left, right, or centered. You
do this by putting “:” signs betweek the dashes for each column. For
example, if you type like this:

::

   | Syntax      | Description |
   | ----------- | ----------: |
   | Header      | Title       |
   | Paragraph   | Text        |

========= ===========
Syntax    Description
========= ===========
Header    Title
Paragraph Text
========= ===========

You will notice that the 2nd column becomes right-aligned. It may not
display correctly in this page due to a different Markdown processor
being used by the ``sphinx`` command I used to generate this page but it
will show up correctly in Jupyter.

These are just a few examples of how you can use Markdown either inside
Jupyter or as a standalone Markdown file that you can convert to PDF or
other formats. Play around with Markdown using ``jupyter-lab`` on your
computer and see if you understand the basic syntax I have shown here.
