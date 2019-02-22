# Making Sense of the CSS Box Model
## 1.3. Entre The Origin of the Box in Typography
### 1.3.1 - Understanding the basics of type
When working with the CSS box model, it is ideal to start from the core and expand outward. In a web page, the core is `type`. The vast majority of content in the Internet world is text, so the vast majority of CSS features are about shaping the text. So we're going to start by understanding the techniques that go back to the traditional typography.

The paper will form the frame of a web page.

![](http://i67.tinypic.com/2jb3be0.png)

The place where the letters in a row end is called the **base line**.

![](http://i65.tinypic.com/2iiu5pe.png)

Below the base line, there is space for the lower case letters as shown in the example above. This area, which is included from the top of the line to the lowest point, is called **point size**. This is also known as the **pixel size** in the digital world. 1em is the height and width of capital letters, regardless of the font and size that is being worked on.  

![](http://i63.tinypic.com/ix5p4k.png)

Traditionally, these letters are shed as square boxes. The default box that we draw around is what the browser creates as a CSS box when a part or sentence of a post is completed, as in the example.

![](http://i65.tinypic.com/2jd0591.png)

In the example above, the size of the box is equal to the size of the sentence, but we can change it by adding new words.

![](http://i64.tinypic.com/fcm14.png)

Separating the text with `padding` and `margin` produces block level elements for us. Placing the contents in different blocks is also a way to tag them in the HTML and CSS world with another markup, such as `p`, `heading`, `quote`. Each of these is a block. So we can work independently on each block without affecting the others.


![](http://i68.tinypic.com/fbfbsy.png)

In this way, placing a box pattern on the base of a group of letters gives us a chance to create a highly sophisticated layout.

---------------
---------------
### 1.3.2 - Change the type and change the box
All fonts and all types have standard point size, line height, leading, tracking and kerning. They determine the relationship between letters, words, sentences and lines. Therefore, the size of our CSS boxes is also linked to them.

![](http://what-when-how.com/wp-content/uploads/2012/07/tmpe13152.png)

The ideal way to change a box is to change the type. Changing the font type and size also changes the size of the box. Larger fonts create larger boxes.

![](http://i68.tinypic.com/oggyo2.png)

Leading in typography is the term used for space between lines.

![](http://www.indesignskills.com/wp-content/uploads/2017/11/Leading.jpg)

Leading in CSS is `line-height`. Below you can see the changes made on `line-height` in detail.

#### `line-height` = 10px

![](http://i68.tinypic.com/2ilhm4l.png)

#### `line-height` = 1px

![](http://i66.tinypic.com/30wms6t.png)

#### `line-height` = 16px

![](http://i65.tinypic.com/1zxr68h.png)



![](http://usabilitypost.com/images/0810/letter_spacing.png)

We can also change the tracking and spacing of the text. We do this with `letter-spacing` in CSS. Below you can see examples of different spacing values.

#### `letter-spacing` = 3px

![](http://i64.tinypic.com/mikrxe.png)


#### `letter-spacing` = -1px

![](http://i66.tinypic.com/n4ir2d.png)


![](http://www.indesignskills.com/wp-content/uploads/2017/11/track2-696x410.jpg)
Tracking is often used in traditional typography to align text within a box. However, in the web world, the text alignment is organized in another particular, called `text-align`. For this reason, `letter-spacing` is also used for tracking in the digital world. Alignment is used for `text-align`. See examples below.

#### `text-align` = right
![](http://i64.tinypic.com/29gndqf.png)


#### `text-align` = right
![](http://i65.tinypic.com/xmieky.png)

#### `text-align` = justify
![](http://i67.tinypic.com/sbpy6o.png)

---------------
---------------
### 1.3.3 - Text flow in the box
In traditional print typography, the size of the paper is fixed, and values such as the resolution pixel of the print machine do not change. When it changes, old designs are invalid and replaced with new ones. However, when viewing content in the digital world, we are faced with different resolutions and viewing options on multiple devices. Since there is no clear boundary for viewing dimensions, there is no limit to how content is arranged according to screens. Generally, such display arrangements are made through the Y-axis. We can fix the area to be used for each box and give the minimum and maximum values for height and width. When we provide a `width` value, specify the height of the box itself, but when determining a constant` height` value of the box can be out of the box, we may need to take additional measures for this.

Below you can see some examples.

#### `width` without anything
![](http://i66.tinypic.com/vpjadu.png)

#### `width` = 60%
![](http://i63.tinypic.com/69penb.png)

#### `width` = 70%
![](http://i67.tinypic.com/1zbxs88.png)


#### `height` = 100px
![](http://i67.tinypic.com/54hcw8.png)


#### `height` = 100px and `overflow` = scroll
![](http://i64.tinypic.com/27wzxw1.png)
