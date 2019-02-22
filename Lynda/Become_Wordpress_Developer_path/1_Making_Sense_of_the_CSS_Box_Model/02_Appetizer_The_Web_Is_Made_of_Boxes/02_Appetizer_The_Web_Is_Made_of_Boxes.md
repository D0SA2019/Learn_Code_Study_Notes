# 1. Making Sense of the CSS Box Model
## 1.2. Appetizer The Web Is Made of Boxes
### 1.2.1 - Displaying information through the web
When we look at a website, we should be able to see more than photos, videos, and content. What we see is actually interpreting media elements by all browsers, such as HTML, CSS, JavaScript, images, and videos, and visualized for us. A document is a data of pixels that look like a written text to us. A visual image appears as a photo for us, but in the software world is a combination of bright and dark and hue. The task of a web developer is to write a series of interpretation information to show the page visitors the most accessible way. This can mean a lot of things. Writing a proper markup, making responsive designs accessible on all screens, etc.

![](http://i63.tinypic.com/avt1cj.png)

For example, in the above simple webpage, the developer passes the following information to the browser:

1. Write the given text in the upper left corner with the default font.
2. View the information.
3. View the image.
4. View the text using the available space.

We'll tell you how the browser will interpret these stages. In the Internet world, content and content presentation are two different things. The content is HTML, and the presentation is CSS. There is an unlimited way to visualize a content, and its basis is through the boxes.

-------
-------
### 1.2.2 - The web is made of boxes
![](http://i67.tinypic.com/ab362s.png)

Let's start with how a browser interprets the document. The above example code ignores parts marked with `<head>`, only the `<body>` tag looks at. Some sections of the document may be composed of articles, links, paragraphs, etc., such as `The Web is Made of Boxes` line. Some contents, such as images or videos, are not actually included in the document, but instead, display them from another source we refer to as a reference.


![](http://i66.tinypic.com/30hpxqt.png)

A page that appears as above is actually the following document. The browser receives this document and sets up the visual structure of the page by the information provided.

![](http://i66.tinypic.com/315mpfb.png)

When we take a closer look at this document, which looks like plain text, we see that it consists of a group of labels and boxes of different components. Thus, the browser takes the rules, the parts that are written, and presents them to the visitor in a meaningful way.

![](http://i66.tinypic.com/143j7mo.png)

The box model for the browser starts with a markup such as `<div>`, `<p>`, `<img>` or `<a>` and ends when the same markup is closed. So,  every label is a box.

![](http://i66.tinypic.com/nvtn2g.png)

To understand the logic of the boxes, just look at a plain HTML page with the browser's developer tools.

![](http://i68.tinypic.com/2d1pdle.png)

-------
-------
### 1.2.3 - Designing with boxes
It is essential to understand the structure of these boxes correctly to make a box-based design. For example, a page with a layout like the following is a view of a visitor:

![](http://i64.tinypic.com/14o3nz4.png)

A web developer should be able to interpret the boxes behind this image as follows.

![](http://i66.tinypic.com/ngup2.png)

When starting the page design, determining general structure by paper and pencil is the basics of what to do in the coding phase.

![](http://i63.tinypic.com/2r7979y.png)

Instead of creating a single design structure, it is more efficient to work with alternatives for different screens and scenarios. Because in today's world we cannot talk about a design that applies to every device.

![](http://i67.tinypic.com/ifr19j.png)

It is important to determine what the final design will look like with the CSS Box Model from the beginning, even if the single line of code is not written yet. As shown in the following example, once the general box structure is decided, it is easier to edit and change the possibilities in the content such as positioning, padding, color, and font. The box model acts as a map on your design.

![](http://i63.tinypic.com/2qthg6c.png)

![](http://i63.tinypic.com/zu2sk9.png)

![](http://i67.tinypic.com/289l8pe.png)
