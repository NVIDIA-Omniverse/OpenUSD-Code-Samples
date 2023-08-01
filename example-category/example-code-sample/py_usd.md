Here you can add any info specific to the code sample flavor and introduce the code sample.

You should include your code sample as a separate source code file like this:
``` {literalinclude} py_usd.py
:language: py
```

You should use these includes instead of putting code in markdown code blocks. The first source code file should be named the same as the markdown file. If you want to show any variations of the code sample of expand it, you should then include source code files with the suffix `_var#`.

``` {literalinclude} py_usd_var1.py
:language: py
```

Variations are not required and you generally won't need them, but it's available if you find you code sample could benefit from showing variations.