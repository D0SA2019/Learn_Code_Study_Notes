# 04. Main Course Understanding the Box Model
## 01 - What is the CSS box model
When we add any tags to a document, the browser wraps around it and acts like a box. As shown in the following image, each tag creates a separate box. Using CSS, we can edit both the tag and the box's visual functions. Using the CSS box model, we give the browser information on how to display each box specific to it.

![](https://media.giphy.com/media/lcs5C23URIMsfc3bFv/giphy.gif)

The CSS box is formed by four individual edges moving together. These boxes are sorted from inside to outside **content box**, **padding box**, **border box** and **margin box**.  If any CSS code is not applied to the content, all of these four boxes are the same, so they behave as one box. Although we have not set any CSS template, the browser implements some basic styling methods.


![](https://media.giphy.com/media/1ppnh2BdFJtrBT1GxD/giphy.gif)

The content above is 100px to 155px without any CSS style. As mentioned in the previous lessons, this dimension can be shaped as we wish. As shown in the example below, we can use the `padding` function to specify the distance of the **border** box that wraps its contents. As shown in the example below, we can use the `padding` function to specify the distance of the **border** box that wraps its contents. In the example, the distance is given as `20px` in each direction; it can also be given as individual values for each edge.

![](https://media.giphy.com/media/87enDcxg1ivDBYCKpO/giphy.gif)

Adding 20px in all directions to a box where the content is 100px, as in the example, means that the browser will display that content area as 140px. However, with `box-size: border-box`, we can tell the browser to fit content according to the display area.

![](https://media.giphy.com/media/Ww2lqlVE2DfUq0iXkt/giphy.gif)

The other box is **border**. `Padding` is actually an invisible alignment option when `border box` is visible. The border can be in any desired color and thickness.  In addition, borders can be shaped in different styles, such as **solid**, **dotted**, **double*,* **grooved**, **framed**, **inset**, and **outset**.

![](https://media.giphy.com/media/QmGPSFjrqM0K1gT9oy/giphy.gif)

When we add `border` to the content, the size of our box expands by adding the dimensions our base border size. In our example, the right and left both 2px expands, and the viewing area is 144px in the final.

![](https://media.giphy.com/media/g01fTBGaWXgysNR1fI/giphy.gif)


The last box that wraps all the edges is `margin`. `padding` aligns content from the inside, `margin` pushes them to the distance with content outside the box.  In the web world, there is normally no space between the contents or boxes, but default **whitespace** can be created with `margin`.

![](https://media.giphy.com/media/1xke1Pb77YhflNqqJ4/giphy.gif)

---------------
---------------
## 02 - Changing the contents within the box
When working from the inside out, we first try to display the **content** box. Changing the font, size and color of the article are the first steps in styling the content.

![](https://media.giphy.com/media/7SId8nF8XPZ8BH6lKq/giphy.gif)

![](https://media.giphy.com/media/PhYTuK1iY4AOc5hLAo/giphy.gif)

Previously, we learned that we could use `letter-spacing` for the space between the letters. `word-spacing` is used to determine the gap between words. We can also use `text-indent` functions if we want to have an indentation at the beginning of the paragraph.

![](https://media.giphy.com/media/YkrDhYBpoYxGW4AM46/giphy.gif)

CSS is also used for text transformation. For this, we use the `text-transform` feature and one of the `capitalize`, `lowercase`, `uppercase` options. For text decoration, the `text-decoration` function can be used with` underline`.

![](https://media.giphy.com/media/1YeNkIGOuea0hMAN3x/giphy.gif)

When using the `color` property to change the color of the text, the `text-shadow` can also be used as a shadow.

![](https://media.giphy.com/media/NPFOFR2LdylolqjZWm/giphy.gif)

Apart from the arrangements in the articles, the box itself can also be modified. `background-color` is used to change the background color of the box.

![](https://media.giphy.com/media/4T5yUWdTXsrtRHJm9N/giphy.gif)

The `background: url(");` property can be used to add visual images to the background. It can also be determined how the background image will be aligned and whether it will repeat itself according to the size of the box.

![](https://media.giphy.com/media/2A606BMz9KQGqty6J4/giphy.gif)

You can also use the `background-size` feature to adjust the size of the background image. This allows the `cover` image assigned to this feature to cover the entire box.

![](https://media.giphy.com/media/BCdcTk3wyQWhBbUT63/giphy.gif)

We can also shape the outside of the box with the inside. With `box-shadow`, we can give shadow, determine the color of the shadow,  and we can set the roundness ratios of the box edges by `border-radius`.

![](https://media.giphy.com/media/9rroBR1RmvevsOV9QB/giphy.gif)

---------------
---------------
## 03 - Understanding the display property
Each HTML element has its own default display option. Since we know how to manipulate boxes, we can address their relationship with these elements. According to the default display properties, elements are fully visible in full width using the available area. When `padding`, `border`, and `margin` properties are given to the element, the content pushes the box according to the assigned values.

![](https://media.giphy.com/media/XJpBSEOY6J14mJcTZc/giphy.gif)

Inline elements `padding`,` border` and `margin` properties may affect other contents around it.

![](https://media.giphy.com/media/Mn55IAAF4ZdQqt5QWo/giphy.gif)

For this reason, we can tell the browser to process and display an inline element according to the box model with `display inline-block`. However, when we do this, we should consider that the distances between the lines will change and that you will create visual disproportionately.

![](https://media.giphy.com/media/2bXBGOHx0aCrel7dVl/giphy.gif)

One of the `display` features is `flex`. We will discuss this in detail in the following lessons. However, we can look at the example below to see what it does.

![](https://media.giphy.com/media/AsshLSaDyWXzWhgkX2/giphy.gif)

Another `display` feature is `table`. If you want to have more control over content placement, `table` and `table-cell` are the best options.

![](https://media.giphy.com/media/RdIsgEkecwwVPaMqWI/giphy.gif)

---------------
---------------
## 04 - Sidebar Images are inline elements
Images for HTML are inline elements that can be positioned in different ways in the text. The general perception of visuals is like emojis in a message. Due to this situation, there are some consequences of using images in the box model. However, it is not common for web design to be used as inline elements as shown below.

![](http://i65.tinypic.com/29e2hwy.png)

Due to the difficulty of HTML in visuals, designers are trying to solve this problem by using features like `float` and` background`. However, this does not change the fact that images are still an inline element, not a box. Therefore, it restricts the use of many features such as `padding`, `margin`, and `border` in the box model.

![](https://media.giphy.com/media/elNbLsLI1J4SvXMqDU/giphy.gif)

The best way to solve this situation is to set the `display` property of the image to `display: block`. So many more features that are more functional in the box model can be used easily.

![](https://media.giphy.com/media/BcITSB0Yy75qDDzUo7/giphy.gif)

---------------
---------------
## 05 - Position is everything
When viewing the document and its elements, the browser displays the default state, one after the other.  We can edit how the display of elements in CSS with the `position` property. The default `position` setting of HTML is `static`, which means that elements are sorted according to the flow in the document.

![](http://i68.tinypic.com/29en6lc.png)

To make the `position` property of an element `relative` means to determine its position relative to the normal flow in the document. The position of the element changes but that the position of the other elements in the layout does not change so that the elements can overlap, because of that it is useful to be careful when using it.

![](https://media.giphy.com/media/14uQ8uxpfCbOxZhMTA/giphy.gif)

Setting the `position` to `absolute` means positioning `relative` relative to an upper element that includes it. If no such element is found, the object is positioned according to its normal flow in the document.

![](https://media.giphy.com/media/fimLkfNSGXecCpq3Bh/giphy.gif)

The `absolute` property is usually used when positioning elements that are connected to the position of another element, such as the description of the image.

![](https://media.giphy.com/media/YFFDdvxodMArYLDQQW/giphy.gif)

The `fixed` property fixes the element relative to the area the browser displays regardless of all other variables.

![](https://media.giphy.com/media/Ym6mLEBThkGHjj1smL/giphy.gif)


---------------
---------------
## 06 - Floating and clearing content
Although `position` options give good results with positioning, it is necessary to display an object next to another when creating a layout for a document. In traditional CSS, this is done with the `float` property.  The `left` and `right` options given to the `float` property determine the location of an object relative to another object, such as the text in the current display area.

![](https://media.giphy.com/media/4Nbe7ToTqQAW59yiwb/giphy.gif)

In the case of two block elements, we can use `float` by positioning each one separately. In doing so, a value such as `width: 50%` determines how much of an existing field will be used for that element. This is usually useful when the dimensions are equal to two boxes.

![](https://media.giphy.com/media/U6pfx9mRvyJo2TTNrU/giphy.gif)

On objects of different sizes, the `float` property can cause some errors. To override this, we can use the `clear` feature. This is used to wrap the object that used `clear` under the object positioned with `float`.

![](https://media.giphy.com/media/1hM83OUY0VWU4A3xtb/giphy.gif)

The `float` property can be used to form pages but can cause visual problems due to different sizes and lengths of content. `display: flex` is much more useful, although it does the same. In the example below, you can see the same content positioned with `float` and `flex`.


![](https://media.giphy.com/media/2uI9r22fMcyKR2PSs5/giphy.gif)


---------------
---------------
## 07 - Using the clearfix
The `float` and `display` properties in nested boxes can be confusing for beginners. In the following example, you can see an example of nested boxes.

![](https://media.giphy.com/media/MRGE6C6mkVLkCGlilv/giphy.gif)

When we add the `float` property to the boxes in this example, the browser will not be able to resize the space used as a `description` according to the new layout. Instead, the code in that section crashes and displays incorrectly.

![](https://media.giphy.com/media/1dOd0zsWiz0nY9o4oE/giphy.gif)

One solution is to add something new to the container in the background with the `::after` feature, so that it can recover itself again. This option is usually not preferred.

![](https://media.giphy.com/media/xFlei1e0T4kQ43c2ob/giphy.gif)

The `clearfix` property is more ideal to solve this problem. This solution basically involves adding empty content to the container, displaying it as a table, and then overriding it. The browser displays the layout correctly using this invisible element.

![](https://media.giphy.com/media/yNZQj63hxogvj9ydms/giphy.gif)

Using `display: flex` removes all these problems and additional element requirements like` clearfix`. Because it is not desirable to place empty elements among our code, even if they are empty.

![](https://media.giphy.com/media/1eExVzF50usdJIbuxs/giphy.gif)

---------------
---------------
## 08 - Pseudoelements Making the browser hallucinate
**Pseudo Classes** : Alter the display or behavior of all the contents inside an element box.
```css
Pseudo Classes
:active
:focus
:hover
:nth-child
:first-of-type
</>
```

**Pseudo Elements**: Alter the display or behavior of a certain part of the contents inside an element box.

```css
Pseudo Elements
::before
::after
::first-letter
::first-line
::selection
::backdrop
</>
```

`before` and `after` allow us to determine what we want to do at the beginning and end of an element. In the following example, we define quotation marks at the beginning and end of the quoted sentence. Text added as `content` is displayed here, but not selectable.

![](https://media.giphy.com/media/QPoekYjwWyWxp7YkV5/giphy.gif)

Since the elements that are arranged with `before` and `after ` are set separately from the originals, the changes made here are applied only to the parts that are made without change. This gives us many advantages at the design stage. In the following example, although the size and color of the quotation mark at the beginning of the quotation mark is changed, we see that there is no change in the quotation mark at the end and the quotation itself.

![](https://media.giphy.com/media/fQYbwygDTcsSde9ER0/giphy.gif)

`first-letter`, as its name implies, allows you to make the desired change on the first letter of the selected element.

![](https://media.giphy.com/media/YB8NtcJ8uCIDlHF5Lo/giphy.gif)

`first-line` allows you to make the desired changes on the first line of the selected element.

![](https://media.giphy.com/media/8P7fkgN6wjMmEDojp5/giphy.gif)

`first-of-type` changes all of the first element of the selected class group. In the following example, you can see the style applied on the first part of the content marked with `p`.

![](https://media.giphy.com/media/4KFvoni2v5SCzS2VKD/giphy.gif)

The `selection` property determines how we want a particular element to appear if it is selected by the user. In the following example, when the user selects normal fonts, there will be no changes, but the font and background color will change when the user selects the quoted section.

![](https://media.giphy.com/media/9GJccDzb95eEOT8s46/giphy.gif)
