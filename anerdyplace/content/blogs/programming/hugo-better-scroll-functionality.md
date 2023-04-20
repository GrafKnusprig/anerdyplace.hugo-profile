---
title: "Hugo Better Scroll Functionality"
author: Philipp
date: 2023-04-18T16:03:08+02:00
draft: false
socialShare: false
toc: false
tags: [hugo, scroller, button]
thumbnail: /images/blogs/generic-thumbs/hugo.webp
image: /images/blogs/generic-thumbs/hugo.webp
---

# The stock...

...page scroller of the hugo-profile theme is nice, but it can only scroll back to the top and the theme has some major flaws, when it comes to mobile devices.

For example, it has always bothered me that the TOC is displayed at the bottom of the page. Of course, you don't have as much space as on the desktop. But displaying it at the top doesn't look very nice either.

So I thought, I'll make another button that scrolls to the TOC.

I copied the single.html and single.css into my static folder, added a new div an put the buttons in there.

code snippet from the css:

```css
...
/* Bottom scroll */

#single #bottomScroll {
    display: block;
    align-self: flex-end;
    z-index: 99;
    border: none;
    outline: none;
    background-color: var(--secondary-color);
    color: var(--primary-color);
    cursor: pointer;
    border-radius: 10px;
    margin: 2px;
}

#single #bottomScroll:hover {
    background-color: var(--primary-color);
    color: var(--secondary-color);
    transition: .5s;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

/* Div for the buttons */

#single #rightSideButtonStack {
    display: flex;
    flex-direction: column;
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 98;
}
```

code snippet from the html:

```html
...
<div class="p-2 px-3" id="rightSideButtonStack">
    <button class="p-2 px-3" onclick="topFunction()" id="topScroll">
      <i class="fas fa-angle-up"></i>
    </button>
    <button class="p-2 px-3" onclick="tocFunction()" id="tocScroll">
      <i class="fas fa-angle-double-down"></i>
    </button>
    <button class="p-2 px-3" onclick="bottomFunction()" id="bottomScroll">
      <i class="fas fa-angle-down"></i>
    </button>
  </div>
</section>

<script>
  var topScroll = document.getElementById('topScroll');
  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    showTop();
    showToc();
    showBottom();
  }

  function showTop() {
    if(topScroll && topScroll != null && topScroll != 'undefined') {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        topScroll.style.display = 'block';
      } else {
        topScroll.style.display = 'none';
      }
    }
  }

  function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

  // scroll to bottom functions
  var pageContent = document.getElementById('page-content');
  var bottomScroll = document.getElementById('bottomScroll');

  function showBottom() {
    if(bottomScroll && bottomScroll != null && bottomScroll != 'undefined' &&
       pageContent && pageContent != null && pageContent != 'undefined') {
      if(bottomInViewport(pageContent)) {
        bottomScroll.style.display = 'block';
      } else {
        bottomScroll.style.display = 'none';
      }
    }
  }

  function bottomFunction() {
    if(pageContent && pageContent != null && pageContent != 'undefined') {
      pageContent.scrollIntoView(false);
      bottomScroll.style.display = 'none';
    }
  }

  function bottomInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.bottom >= (window.innerHeight + 1|| document.documentElement.clientHeight + 1) //+1 to hide scroll button when at bottm
    );
  }

  // scroll to toc functions
  var tocScroll = document.getElementById('tocScroll');
  var toc = document.getElementById('toc');

  function showToc() {
    if(toc && toc != null && toc != 'undefined' &&
       tocScroll && tocScroll != null && tocScroll != 'undefined') {
      if(isInViewport(toc)) {
        tocScroll.style.display = 'none';
      } else {
        tocScroll.style.display = 'block';
      }
    }
  }

  function tocFunction() {
    if(toc && toc != null && toc != 'undefined') {
      toc.scrollIntoView(true);
    }
  }

  function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }
</script>
```

It works as I imagined and I'm pretty happy with it.

I also added another one that scrolls to the end of the post.
Because why not, while I'm at it.

It's now much more convenient on mobile devices and a much better user experience.

:)