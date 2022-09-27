---
title: "Embed html5 videos in blog posts"
author: Philipp
date: 2022-09-25T15:39:23+02:00
draft: false
socialShare: false
toc: false
tags: [hugo, video, html5, programming, shortcode]
thumbnail: /images/blogs/generic-thumbs/hugo.webp
---

## Shortcode to embed videos in blog posts

I've written a little video shortcode to embed local videos in my blog posts.

I use the bootstrap class *embed-responsive* on the container and *embed-responsive-item* on the element.
The *w-100* class ensures, that the video has the same width as the text.

```html
{{% include "layouts/shortcodes/video.html" %}}
```

You use it like this:

- string1: path to the video file in the static folder. e.g. "/exampleVideo.mp4"
- string2: video format. e.g. "video/mp4"
- string3: additional attibute. e.g. autoplay or controls

```md
{{</* video "string1" "string2" "string3" */>}}
```