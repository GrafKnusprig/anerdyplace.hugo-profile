---
title: "Embed files in blog posts"
author: Philipp
date: 2022-09-25T18:52:23+02:00
draft: false
socialShare: false
toc: false
tags: [hugo, files, shortcode, preview, programming]
thumbnail: /images/blog/generic-thumbs/hugo.webp
---

## Shortcode to embed files in blog posts

In my posts, I write about the things I'm programming in my free time and often I want to show the code.
Therefore I need an easy way to include the files as code preview in my blog posts.

I use a shortcode which makes use of HUGOs [readFile](https://gohugo.io/functions/readfile/) and [saveHtml](https://gohugo.io/functions/safehtml/) function.

include.html

```html
{{% include "/layouts/shortcodes/include.html"%}}
```

and you use it like this:

```markdown
    ```html
    {{% include "/layouts/shortcodes/include.html"%}}
    ```
```

Furthermore I'd like to have some kind of raw-data view, that allows an easy download of the files, without copy and paste.
For this to work, the file has to be in the static folder of your hugo project.
Then you can provide the file like this:

```markdown
[include.html](include.txt)
```

which results in:

[include.html](include.txt)
