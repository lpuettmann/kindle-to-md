Kindle to Markdown
======

Notes on a Kindle are saved in a file called "My Clippings.txt". This script transforms these notes for one book into a post written in Markdown that can be displayed on a [Jekyll](https://jekyllrb.com/) website.

Find the line of text in "My Clippings.txt" that specifies the book and change `bookStr`:

```python
bookStr = 'Moby Dick: or, the White Whale (Melville, Herman)'
```
