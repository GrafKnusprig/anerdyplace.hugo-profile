---
title: "Hugo Full Text Search"
author: Philipp
date: 2022-09-14T22:15:01+02:00
draft: false
socialShare: false
tags: [hugo, search, javascript, programming]
thumbnail: /images/blog/generic-thumbs/hugo.webp
---

## Showcase
You can embed the search everywhere you like 😉

{{< search >}}
<hr>

## Overview

To implement a full text search in my hugo site, I used a method I found in a post from [weitblick.org](https://weitblick.org/post/simple-static-site-search-hugo-jamstack/) and modified it to my needs.

It's really simple:


1. create **index.json** template
2. modify **config.toml**
3. add **search.js** to website
4. create **search.html** and modify it if needed
5. create **search.md** page

## 1. index.json
add index.json to ./layouts/_default

```json
{{% include "layouts/_default/index.json" %}}
```

## 2. config.toml
add to config.toml

```toml
[outputs]
   home = [ "HTML", "JSON" ]
```

In my case, I use yaml:

```yaml
outputs:
  home:
    - HTML
    - JSON
```

## 3. search.js
add [*search.js*](search.js) to ./static/js/

```javascript
{{% include "search.js" %}}
```

## 4. search.html
add search.html to ./layouts/shortcodes/ 

```html
{{% include "layouts/shortcodes/search.html" %}}
```

## 5. search.md
add search.md page

```md
---
title: "Search"
summary: "Search blog for keywords"
toc: false
socialShare: false
date: false
---

{{</* search */>}}

```