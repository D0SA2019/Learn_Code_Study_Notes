# Making Sense of the CSS Box Model
## 1.5. Dessert The Brave New World of CSS Boxes
### 1.5.1 - Creating flexible boxes with display Flex
CSS is constantly evolving to make it easier to encode complex designs. As this course is specifically focused on the box model, we focus on two innovations: flexible boxes and CSS shapes.

Below we see browsers that support CSS flexbox usage. You can click the link for the current list.

![](https://i.postimg.cc/1XtkSjrg/Screen-Shot-2019-01-29-at-13-24-43.png)
https://caniuse.com/#feat=flexbox

The first example of what can be done with flexbox is vertical centering.  This is also quite simple code. For this purpose, we want to use the box `display: flex;` and then the contents of `align-items: center;` and `justify-content: center;` is sufficient to align.

![](https://media.giphy.com/media/5aYewR3rwldhm9qlnk/giphy.gif)


Flexbox is also very useful when creating columns of equal height in the use of CSS. We can easily place the columns side by side using only the `display: flex;` code. If we want a more detailed layout, we can place descriptive lines such as `width: calc(33% - 1em);` in addition to the column boxes.

![](https://media.giphy.com/media/1oHmyO5a2o70s5lTS5/giphy.gif)

We can change the order in which the boxes that we want to display side by side can be displayed without changing their markup. For this, we can use the `order` feature.

![](https://media.giphy.com/media/9DnPMhqEzG7vsND4jZ/giphy.gif)

We can also reverse the order of the boxes with a single line of code. For this, it is enough to use `flex-direction: row-reverse;`.

![](https://media.giphy.com/media/35TyXwddzApvfIzYBv/giphy.gif)


---------------
---------------
### 1.5.2 - Changing the shape outside
In CSS, each element is a box, and understanding the CSS box model means that you can do anything you want to do. However, in the box model, everything has four sides, and although we can show it in different ways with the properties like radius, every new feature we apply will have vertical edges. However, with CSS3, this problem can be overcome.  The `-webkit-shape-outside: circle ();` code is used for this.

For example, if we want the content to look like wrapped around the profile picture in our content with the following layout, we use the code as follows.

![](https://media.giphy.com/media/28D8UyCkil9GoGMipg/giphy.gif)

Similarly, polygonal structures can be created. However, the `-webKit-shape-outside` feature is not yet supported by all browsers. That's why it's important to be careful when using it.

![](https://i.postimg.cc/XYyrSNJS/Screen-Shot-2019-01-29-at-17-49-53.png)
