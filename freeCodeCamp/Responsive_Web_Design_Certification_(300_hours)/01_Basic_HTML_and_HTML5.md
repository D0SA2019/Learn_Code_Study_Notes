# Introduction to Basic HTML & HTML5
HTML, or HyperText Markup Language, is a markup language used to describe the structure of a web page. It uses a special syntax or notation to organize and give information about the page to the browser. Elements usually have opening and closing tags that surround and give meaning to content. For example, there are different tag options to place around text to show whether it is a heading, a paragraph, or a list.

```HTML
<h1>Top level heading: Maybe a page title</h1>

<p>A paragraph of text. Some information we would like to communicate to the viewer. This can be as long or short as we would like.</p>

<ol>
  <li>Number one on the list</li>
  <li>Number two</li>
  <li>A third item</li>
</ol>
```
--------------
--------------
## 1. Say Hello to HTML Elements

The code in your code editor that says `<h1>Hello</h1>`? That's an HTML element.
Most HTML elements have an opening tag and a closing tag.

Opening tags look like this: `<h1>`

Closing tags look like this: `</h1>`

The only difference between opening and closing tags is the forward slash after the opening bracket of a closing tag.

```html
<!-- GIVEN -->
<h1>Hello</h1>

<!-- SOLUTION -->
<h1>Hello World</h1>
```
--------------
#### `Before - After`

![](http://i66.tinypic.com/x66pv.png)

--------------
--------------
## 2. Headline with the h2 Element
The h2 element you will be adding in this step will add a level two heading to the web page.

This element tells the browser about the structure of your website. h1 elements are often used for main headings, while h2 elements are generally used for subheadings. There are also h3, h4, h5 and h6 elements to indicate different levels of subheadings.


**Test** : Add an h2 tag that says "CatPhotoApp" to create a second HTML element below your "Hello World" h1 element.

```html
<h1>Hello World</h1>
<h2>CatPhotoApp</h2>
```
--------------
#### `Before - After`
![](http://i67.tinypic.com/s0y6pe.png)


--------------
--------------
## 3. Inform with the Paragraph Element

`p` elements are the preferred element for paragraph text on websites. `p` is short for "paragraph".

You can create a paragraph element like this: `<p>I'm a p tag!</p>`

**Test** : Create a p element below your h2 element, and give it the text "Hello Paragraph".

```html
<h1>Hello World</h1>
<h2>CatPhotoApp</h2>
<p>Hello Paragraph</p>
```
--------------
#### `Before - After`
![](http://i63.tinypic.com/dvn4bc.png)

--------------
--------------
## 4. Fill in the Blank with Placeholder Text
Web developers traditionally use `lorem ipsum text` as placeholder text. The 'lorem ipsum' text is randomly scraped from a famous passage by Cicero of Ancient Rome.

Lorem ipsum text has been used as placeholder text by typesetters since the 16th century, and this tradition continues on the web.

Well, 5 centuries is long enough. Since we're building a CatPhotoApp, let's use something called `kitty ipsum text`.


**Test** : Replace the text inside your `p` element with the first few words of this kitty ipsum text: `Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.`

```html
<h1>Hello World</h1>

<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
```
--------------
#### `Before - After`

![](http://i66.tinypic.com/2lnjzmw.png)

--------------
--------------
## 5. Uncomment HTML
Commenting is a way that you can leave comments for other developers within your code without affecting the resulting output that is displayed to the end user.

Commenting is also a convenient way to make code inactive without having to delete it entirely.

Comments in HTML starts with `<!--, and ends with a -->`

```html
<!-- GIVEN -->
<!--
<h1>Hello World</h1>

<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
-->

<!-- SOLUTION -->
<h1>Hello World</h1>

<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
```

--------------
--------------
## 6. Comment out HTML

Remember that in order to start a comment, you need to use `<!-- and to end a comment, you need to use -->`

Here you'll need to end the comment before your h2 element begins.

**Test** : Comment out your h1 element and your p element, but not your h2 element.

```html
<!--
<h1>Hello World</h1>

<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
-->

<!-- SOLUTION -->
<!--
<h1>Hello World</h1>
-->
<h2>CatPhotoApp</h2>
<!--
<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
-->
```

--------------
--------------
## 7. Delete HTML Elements
Our phone doesn't have much vertical space.

Let's remove the unnecessary elements so we can start building our CatPhotoApp.

**Test** : Delete your `h1` element so we can simplify our view.

```html
<!-- GIVEN -->
<h1>Hello World</h1>

<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>

<!-- SOLUTION -->
<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
```
--------------
#### `Before - After`

![](http://i65.tinypic.com/4r2rsh.png)

--------------
--------------
## 8. Introduction to HTML5 Elements
HTML5 introduces more descriptive HTML tags. These include `header`, `footer`, `nav`, `video`, `article`, `section` and others.

These tags make your HTML easier to read, and also help with Search Engine Optimization (SEO) and accessibility.

The `main` HTML5 tag helps search engines and other developers find the main content of your page.

**Note** : Many of the new HTML5 tags and their benefits are covered in the Applied Accessibility section.

**Test** : Create a second p element after the existing p element with the following kitty ipsum text: `Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.`
Wrap the paragraphs with an opening and closing `main` tag.

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>

<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>


<!-- SOLUTION -->
<h2>CatPhotoApp</h2>

<main>
<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>

<p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>
```
--------------
#### `Before - After`
![](http://i63.tinypic.com/20udh8m.png)


--------------
--------------
## 9. Add Images to Your Website
You can add images to your website by using the `img` element, and point to a specific image's URL using the `src` attribute.

An example of this would be: `<img src="https://www.your-image-source.com/your-image.jpg">`

Note that `img` elements are self-closing.

All `img` elements must have an `alt` attribute. The text inside an `alt` attribute is used for screen readers to improve accessibility and is displayed if the image fails to load.

Note: If the image is purely decorative, using an empty alt attribute is a best practice.

Ideally the `alt` attribute should not contain special characters unless needed.

Let's add an `alt` attribute to our `img` example above:

`<img src="https://www.your-image-source.com/your-image.jpg" alt="Author standing on a beach with two thumbs up.">`


**Test**
Insert an `img` tag, before the `h2` element.

Now set the `src` attribute so that it points to this url:

`https://bit.ly/fcc-relaxing-cat`

Finally don't forget to give your image an `alt` text.


```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>



<!-- SOLUTION -->
<img src="https://bit.ly/fcc-relaxing-cat" alt="Kitty upside down">
<h2>CatPhotoApp</h2>
<main>

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>
```
--------------
#### `Before - After`
![](http://i68.tinypic.com/24zgopj.png)

--------------
--------------
## 10. Link to External Pages with Anchor Elements
You can use `anchor` elements to link to content outside of your web page.

`anchor` elements need a destination web address called an href attribute. They also need anchor text. Here's an example:

`<a href="https://freecodecamp.org">this links to freecodecamp.org</a>`

Then your browser will display the text "this links to freecodecamp.org" as a link you can click. And that link will take you to the web address https://www.freecodecamp.org.

**Test**  : Create an a element that links to http://freecatphotoapp.com and has "cat photos" as its anchor text


```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>

<a href="http://freecatphotoapp.com">cat photos</a>
</main>
```
--------------
#### `Before - After`
![](http://i66.tinypic.com/sqju50.png)

--------------
--------------
## 11. Link to Internal Sections of a Page with Anchor Elements
Anchor elements can also be used to create internal links to jump to different sections within a webpage.

To create an internal link, you assign a link's `href` attribute to a hash symbol `#` plus the value of the id attribute for the element that you want to internally link to, usually further down the page. You then need to add the same id attribute to the element you are linking to. An id is an attribute that uniquely describes an element.

Below is an example of an internal anchor link and its target element:

```html
<a href="#contacts-header">Contacts</a>
...
<h2 id="contacts-header">Contacts</h2>
```
When users click the Contacts link, they'll be taken to the section of the webpage with the Contacts header element.

**Test** : Change your external link to an internal link by changing the `href` attribute to "#footer" and the text from "cat photos" to "Jump to Bottom".

Remove the `target="_blank"` attribute from the anchor tag since this causes the linked document to open in a new window tab.

Then add an `id` attribute with a value of "footer" to the `<footer>` element at the bottom of the page.
```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>

  <a href="http://freecatphotoapp.com" target="_blank">cat photos</a>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
  <p>Meowwww loved it, hated it, loved it, hated it yet spill litter box, scratch at owner, destroy all furniture, especially couch or lay on arms while you're using the keyboard. Missing until dinner time toy mouse squeak roll over. With tail in the air lounge in doorway. Man running from cops stops to pet cats, goes to jail.</p>
  <p>Intently stare at the same spot poop in the plant pot but kitten is playing with dead mouse. Get video posted to internet for chasing red dot leave fur on owners clothes meow to be let out and mesmerizing birds leave fur on owners clothes or favor packaging over toy so purr for no reason. Meow to be let out play time intently sniff hand run outside as soon as door open yet destroy couch.</p>

</main>

<footer>Copyright Cat Photo App</footer>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>

  <a href="#footer">Jump to Bottom</a> <!-- Changes here -->

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
  <p>Meowwww loved it, hated it, loved it, hated it yet spill litter box, scratch at owner, destroy all furniture, especially couch or lay on arms while you're using the keyboard. Missing until dinner time toy mouse squeak roll over. With tail in the air lounge in doorway. Man running from cops stops to pet cats, goes to jail.</p>
  <p>Intently stare at the same spot poop in the plant pot but kitten is playing with dead mouse. Get video posted to internet for chasing red dot leave fur on owners clothes meow to be let out and mesmerizing birds leave fur on owners clothes or favor packaging over toy so purr for no reason. Meow to be let out play time intently sniff hand run outside as soon as door open yet destroy couch.</p>

</main>

<footer id="footer">Copyright Cat Photo App</footer> <!-- Changes here -->
```
--------------
#### `Before - After`
![](http://i64.tinypic.com/34dsokm.png)

--------------
--------------
## 12. Nest an Anchor Element within a Paragraph
You can nest links within other text elements.


```html
<p>
Here's a <a target="_blank" href="http://freecodecamp.org"> link to freecodecamp.org</a> for you to follow.
</p>
```
Let's break down the example:

Normal text is wrapped in the p element:
`<p> Here's a ... for you to follow. </p>`

Next is the anchor element <a> (which requires a closing tag </a>):
`<a> ... </a>`

`target` is an anchor tag attribute that specifies where to open the link and the value `"_blank"` specifies to open the link in a new tab

href is an anchor tag attribute that contains the URL address of the link:
`<a href="http://freecodecamp.org"> ... </a>`

The text, "link to freecodecamp.org", within the anchor element called anchor text, will display a link to click:,
`<a href=" ... ">link to freecodecamp.org</a>`

The final output of the example will look like this:
Here's a link to freecodecamp.org for you to follow.

**Test** : Nest your existing `a` element within a new `p` element (just after the existing main element). The new paragraph should have text that says "View more cat photos", where "cat photos" is a link, and the rest of the text is plain text.
```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>

  <a href="http://freecatphotoapp.com" target="_blank">cat photos</a>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>

  <a href="http://freecatphotoapp.com" target="_blank">cat photos</a>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
  <p>View more <a href="http://freecatphotoapp.com" target="_blank">cat photos </a></p> <!-- Changed line -->
</main>
```
--------------
#### `Before - After`
![](http://i68.tinypic.com/rh31pg.png)

--------------
--------------
## 13. Make Dead Links Using the Hash Symbol
Sometimes you want to add `a` elements to your website before you know where they will link.

This is also handy when you're changing the behavior of a link using JavaScript, which we'll learn about later.

**Test** : The current value of the `href` attribute is a link that points to "http://freecatphotoapp.com". Replace the `href` attribute value with a `#`, also known as a hash symbol, to create a dead link.

For example: `href="#"`

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="http://freecatphotoapp.com" target="_blank">cat photos</a>.</p>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#" target="_blank">cat photos</a>.</p> <!-- Changes here -->

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>
```
--------------
#### `Before - After`
![](http://i64.tinypic.com/2yoz5vk.png)

--------------
--------------
## 14. Turn an Image into a Link
You can make elements into links by nesting them within an a element.

Nest your image within an `a` element. Here's an example:

`<a href="#"><img src="https://bit.ly/fcc-running-cats" alt="Three kittens running towards the camera."></a>`

Remember to use `#` as your `a` element's `href` property in order to turn it into a dead link.

**Test** : Place the existing image element within an anchor element.

Once you've done this, hover over your image with your cursor. Your cursor's normal pointer should become the link clicking pointer. The photo is now a link.
```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back.">

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a> <!-- Changes here -->

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>
```

--------------
--------------
## 15. Create a Bulleted Unordered List
HTML has a special element for creating **unordered lists**, or bullet point style lists.

Unordered lists start with an opening `<ul>` element, followed by any number of `<li>` elements. Finally, unordered lists close with a `</ul>`

For example:

```html
<ul>
  <li>milk</li>
  <li>cheese</li>
</ul>
```
would create a bullet point style list of "milk" and "cheese".

**Test** : Remove the last two `p` elements and create an unordered list of three things that cats love at the bottom of the page.

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>
  <!-- Changer below -->
  <ul>
    <li> Drinking milk </li>
    <li> Sleeping well </li>
    <li> Playing more </li>
  </ul>
</main>
```
--------------
#### `Before - After`
![](http://i64.tinypic.com/23ro21g.png)

--------------
--------------
## 16. Create an Ordered List
HTML has another special element for creating ordered lists, or numbered lists.

Ordered lists start with an opening `<ol>` element, followed by any number of `<li>` elements. Finally, ordered lists close with a `</ol>`

For example:

```html
<ol>
  <li>Garfield</li>
  <li>Sylvester</li>
</ol>
```
would create a numbered list of "Garfield" and "Sylvester".

**Test** : Create an ordered list of the top 3 things cats hate the most.


```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>

</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>mice</li>
    <li>dogs </li>
    <li>being wet </li>
    </ol>

</main>
```
--------------
#### `Before - After`
![](http://i63.tinypic.com/2zhdt10.png)


--------------
--------------
## 17. Create a Text Field
Now let's create a web form.
Input elements are a convenient way to get input from your user.
You can create a text input like this:

`<input type="text">`

Note that input elements are self-closing.


**Test** : Create an input element of type text below your lists.

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>

</main>



<!-- SOLUTION -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <input type="text">    <!-- Added this line -->
</main>
```
--------------
#### `Before - After`
![](http://i66.tinypic.com/30sye5y.png)

--------------
--------------
## 18. Add Placeholder Text to a Text Field

Placeholder text is what is displayed in your input element before your user has inputted anything.

You can create placeholder text like so:

`<input type="text" placeholder="this is placeholder text">`
and looks like :
<input type="text" placeholder="this is placeholder text">


**Test** : Set the placeholder value of your text input to "cat photo URL".

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <input type="text">   <!-- will change as below-->
</main>



<!-- SOLUTION -->
<input type="text" placeholder="cat photo URL">
```
--------------
#### `Before - After`
![](http://i67.tinypic.com/o0tf1w.png)

--------------
--------------
## 19. Create a Form Element

You can build web forms that actually submit data to a server using nothing more than pure HTML. You can do this by specifying an action on your `form` element.

For example:

`<form action="/url-where-you-want-to-submit-form-data"></form>`



**Test** : Nest your text field inside a `form` element, and add the `action="/submit-cat-photo"` attribute to the form element.

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <input type="text" placeholder="cat photo URL">   <!-- Change will be here -->
</main>



<!-- SOLUTION -->
<form action="/submit-cat-photo"><input type="text" placeholder="cat photo URL"></form>
```

--------------
--------------
## 20. Add a Submit Button to a Form

Let's add a `submit` button to your form. Clicking this button will send the data from your form to the URL you specified with your form's `action` attribute.

Here's an example submit button:

`<button type="submit">this button submits the form</button>`

Looks like :

<button type="submit">this button submits the form</button>

**Test** : Add a button as the last element of your `form` element with a type of `submit`, and "Submit" as its text.

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="/submit-cat-photo">   <!-- Changes will be here-->
    <input type="text" placeholder="cat photo URL">
  </form>
</main>



<!-- SOLUTION -->
<form action="/submit-cat-photo">
  <input type="text" placeholder="cat photo URL">
  <button type="submit">Submit</button>
</form>
```
--------------
#### Before - After

![](http://i66.tinypic.com/1johzq.png)

--------------
--------------
## 21. Use HTML5 to Require a Field

You can require specific form fields so that your user will not be able to submit your form until he or she has filled them out.

For example, if you wanted to make a text input field required, you can just add the attribute `required` within your `input` element, like this:

`<input type="text" required>`


**Test** : Make your text `input` a `required` field, so that your user can't submit the form without completing this field.

Then try to submit the form without inputting any text. See how your HTML5 form notifies you that the field is required?


```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="/submit-cat-photo">
    <input type="text" placeholder="cat photo URL">   <!-- Change will be here-->
    <button type="submit">Submit</button>
  </form>
</main>



<!-- SOLUTION -->
<input type="text" required placeholder="cat photo URL">
```
--------------
#### `Before - After`

![](http://i65.tinypic.com/so8u1u.png)


--------------
--------------
## 22. Create a Set of Radio Buttons

You can use `radio buttons` for questions where you want the user to only give you one answer out of multiple options.

Radio buttons are a type of `input`.

Each of your radio buttons can be nested within its own `label` element. By wrapping an `input` element inside of a `label` element it will automatically associate the radio button input with the label element surrounding it.

All related radio buttons should have the same `name` attribute to create a radio button group. By creating a radio group, selecting any single radio button will automatically deselect the other buttons within the same group ensuring only one answer is provided by the user.

Here's an example of a radio button:

`<label>
  <input type="radio" name="indoor-outdoor">Indoor
</label>`


Looks like :
<label>
  <input type="radio" name="indoor-outdoor">Indoor
</label>

It is considered best practice to set a `for` attribute on the `label` element, with a value that matches the value of the `id` attribute of the `input` element. This allows assistive technologies to create a linked relationship between the label and the `child` input element. For example:

`<label for="indoor">
  <input id="indoor" type="radio" name="indoor-outdoor">Indoor
</label>`

Looks like :
<label for="indoor">
  <input id="indoor" type="radio" name="indoor-outdoor">Indoor
</label>

**Test** : Add a pair of radio buttons to your form, each nested in its own label element. One should have the option of `indoor` and the other should have the option of `outdoor`. Both should share the name attribute of `indoor-outdoor` to create a radio group.

```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="/submit-cat-photo">   <!--Changes will be here-->
    <input type="text" placeholder="cat photo URL" required>
    <button type="submit">Submit</button>
  </form>



<!-- SOLUTION -->
<form action="/submit-cat-photo">
  <input type="text" placeholder="cat photo URL" required>
  <button type="submit">Submit</button>
  <label>
   <input type="radio" name="indoor-outdoor">Indoor</input>
    </label>
  <label>
    <input type="radio" name="indoor-outdoor">Outdoor</input>
      </label>
</form>
```
--------------
#### `Before - After`

![](http://i67.tinypic.com/vnjtz4.png)

--------------
--------------
## 23. Create a Set of Checkboxes

Forms commonly use `checkboxes` for questions that may have more than one answer.

Checkboxes are a type of `input`

Each of your checkboxes can be nested within its own `label` element. By wrapping an `input` element inside of a `label` element it will automatically associate the checkbox input with the label element surrounding it.

All related checkbox inputs should have the same `name` attribute.

It is considered best practice to explicitly define the relationship between a checkbox `input` and its corresponding `label` by setting the `for` attribute on the `label` element to match the `id` attribute of the associated `input` element.

Here's an example of a checkbox:

`<label for="loving"><input id="loving" type="checkbox" name="personality"> Loving</label>`

Looks like :
<label for="loving"><input id="loving" type="checkbox" name="personality"> Loving</label>

**Test** : Add to your form a set of three checkboxes. Each checkbox should be nested within its own `label` element. All three should share the `name` attribute of `personality`.



```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="/submit-cat-photo"> <!-- Changes will come here-->
    <label for="indoor"><input id="indoor" type="radio" name="indoor-outdoor"> Indoor</label>
    <label for="outdoor"><input id="outdoor" type="radio" name="indoor-outdoor"> Outdoor</label><br>
    <input type="text" placeholder="cat photo URL" required>
    <button type="submit">Submit</button>
  </form>
</main>



<!-- SOLUTION -->
<form action="/submit-cat-photo">
  <label for="indoor"><input id="indoor" type="radio" name="indoor-outdoor"> Indoor</label>
  <label for="outdoor"><input id="outdoor" type="radio" name="indoor-outdoor"> Outdoor</label><br>
  <label for="grumpy"><input id="grumpy" type="checkbox" name="personality"> Grumpy</label>
  <label for="cute"><input id="cute" type="checkbox" name="personality"> Cute</label>
  <label for="lazy"><input id="lazy" type="checkbox" name="personality"> Lazy</label>
  <input type="text" placeholder="cat photo URL" required>
  <button type="submit">Submit</button>
</form>
```

--------------
#### `Before - After`

![](http://i64.tinypic.com/esjk39.png)

--------------
--------------
## 24. Check Radio Buttons and Checkboxes by Default

You can set a checkbox or radio button to be checked by default using the `checked` attribute.
To do this, just add the word "checked" to the inside of an input element. For example:

`<input type="radio" name="test-name" checked>`
<input type="radio" name="test-name" checked>

**Test** : Set the first of your `radio buttons` and the first of your `checkboxes` to both be checked by default.


```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="/submit-cat-photo"> <!-- Changes will come here-->
    <label><input type="radio" name="indoor-outdoor"> Indoor</label>
    <label><input type="radio" name="indoor-outdoor"> Outdoor</label><br>
    <label><input type="checkbox" name="personality"> Loving</label>
    <label><input type="checkbox" name="personality"> Lazy</label>
    <label><input type="checkbox" name="personality"> Energetic</label><br>
    <input type="text" placeholder="cat photo URL" required>
    <button type="submit">Submit</button>
  </form>
</main>



<!-- SOLUTION -->
<form action="/submit-cat-photo">
  <label><input type="radio" name="indoor-outdoor"checked> Indoor</label>
  <label><input type="radio" name="indoor-outdoor"> Outdoor</label><br>
  <label><input type="checkbox" name="personality" checked> Loving</label>
  <label><input type="checkbox" name="personality" checked> Lazy</label>
  <label><input type="checkbox" name="personality"> Energetic</label><br>
  <input type="text" placeholder="cat photo URL" required>
  <button type="submit">Submit</button>
</form>
```

--------------

#### `Before - After`

![](http://i68.tinypic.com/kbvk09.png)


--------------
--------------
## 25. Nest Many Elements within a Single div Element
The `div` element, also known as a division element, is a general purpose container for other elements.

The `div` element is probably the most commonly used HTML element of all.

Just like any other non-self-closing element, you can open a div element with `<div>` and close it on another line with `</div>`.


**Test** : Nest your "Things cats love" and "Things cats hate" lists all within a single `div` element.

Hint: Try putting your opening `div` tag above your "Things cats love" `p` element and your closing `div` tag after your closing `ol` tag so that both of your lists are within one `div`.


```html
<!-- GIVEN -->
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>
  <!-- Changes will come here-->
  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>

  <form action="/submit-cat-photo">
    <label><input type="radio" name="indoor-outdoor" checked> Indoor</label>
    <label><input type="radio" name="indoor-outdoor"> Outdoor</label><br>
    <label><input type="checkbox" name="personality" checked> Loving</label>
    <label><input type="checkbox" name="personality"> Lazy</label>
    <label><input type="checkbox" name="personality"> Energetic</label><br>
    <input type="text" placeholder="cat photo URL" required>
    <button type="submit">Submit</button>
  </form>
</main>



<!-- SOLUTION -->
<div>
<p>Things cats love:</p>
<ul>
  <li>cat nip</li>
  <li>laser pointers</li>
  <li>lasagna</li>
</ul>
<p>Top 3 things cats hate:</p>
<ol>
  <li>flea treatment</li>
  <li>thunder</li>
  <li>other cats</li>
</ol>
</div>
```

--------------
#### `Before - After`

![](http://i68.tinypic.com/70l7pz.png)


--------------
--------------
## 26. Declare the Doctype of an HTML Document
The challenges so far have covered specific HTML elements and their uses. However, there are a few elements that give overall structure to your page, and should be included in every HTML document.

At the top of your document, you need to tell the browser which version of HTML your page is using. HTML is an evolving language, and is updated regularly. Most major browsers support the latest specification, which is HTML5. However, older web pages may use previous versions of the language.

You tell the browser this information by adding the `<!DOCTYPE ...>` tag on the first line, where the "..." part is the version of HTML. For HTML5, you use `<!DOCTYPE html>`.

The `!` and uppercase `DOCTYPE` is important, especially for older browsers. The `html` is not case sensitive.

Next, the rest of your HTML code needs to be wrapped in `html` tags. The opening `<html>` goes directly below the `<!DOCTYPE html>` line, and the closing `</html>` goes at the end of the page.

Here's an example of the page structure:

```HTML
<!DOCTYPE html>
<html>
  <!-- Your HTML code goes here -->
</html>
```

**Test** : Add a `DOCTYPE` tag for HTML5 to the top of the blank HTML document in the code editor. Under it, add opening and closing `html` tags, which wrap around an `h1` element. The heading can include any text.


```html
<!-- SOLUTION -->
<!DOCTYPE HTML>
<html>
    <h1> Here is the HTML5</h1>
    </html>
```
--------------
#### `Before - After`

![](http://i65.tinypic.com/2di4o7o.png)

--------------
--------------
## 27. Define the Head and Body of an HTML Document
You can add another level of organization in your HTML document within the `html` tags with the `head` and `body` elements. Any markup with information about your page would go into the `head` tag. Then any markup with the content of the page (what displays for a user) would go into the `body` tag.

Metadata elements, such as `link`, `meta`, `title`, and `style`, typically go inside the `head` element.

Here's an example of a page's layout:

```HTML
<!DOCTYPE html>
<html>
  <head>
    <!-- metadata elements -->
  </head>
  <body>
    <!-- page contents -->
  </body>
</html>
```

**Test** : Edit the markup so there's a `head` and a `body`. The `head` element should only include the `title`, and the `body` element should only include the `h1` and `p`.

```html
<!-- GIVEN -->
<!DOCTYPE html>
<html>
  <title>The best page ever</title>

  <h1>The best page ever</h1>
  <p>Cat ipsum dolor sit amet, jump launch to pounce upon little yarn mouse, bare fangs at toy run hide in litter box until treats are fed. Go into a room to decide you didn't want to be in there anyway. I like big cats and i can not lie kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Meow i could pee on this if i had the energy for slap owner's face at 5am until human fills food dish yet scamper. Knock dish off table head butt cant eat out of my own dish scratch the furniture. Make meme, make cute face. Sleep in the bathroom sink chase laser but pee in the shoe. Paw at your fat belly licks your face and eat grass, throw it back up kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>

</html>  


<!-- SOLUTION -->
<!DOCTYPE html>
<html>
    <head>
  <title>The best page ever</title>
    </head>

    <body>
  <h1>The best page ever</h1>
  <p>Cat ipsum dolor sit amet, jump launch to pounce upon little yarn mouse, bare fangs at toy run hide in litter box until treats are fed. Go into a room to decide you didn't want to be in there anyway. I like big cats and i can not lie kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Meow i could pee on this if i had the energy for slap owner's face at 5am until human fills food dish yet scamper. Knock dish off table head butt cant eat out of my own dish scratch the furniture. Make meme, make cute face. Sleep in the bathroom sink chase laser but pee in the shoe. Paw at your fat belly licks your face and eat grass, throw it back up kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  </body>
</html>
```
--------------

#### `Before - After`

![](http://i64.tinypic.com/309psmx.png)


--------------
--------------
# Worksheet codes and preview
----------------
----------------

```HTML
<!-- Basic HTML and HTML5 -->
<!DOCTYPE HTML>
<html>
  <head>
    <title>The best about CatPhotoApp</title>
  </head>

  <body>
    <h2>CatPhotoApp</h2>
    <main>

<a href="#footer">Jump to Bottom</a>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
  <p>Meowwww loved it, hated it, loved it, hated it yet spill litter box, scratch at owner, destroy all furniture, especially couch or lay on arms while you're using the keyboard. Missing until dinner time toy mouse squeak roll over. With tail in the air lounge in doorway. Man running from cops stops to pet cats, goes to jail.</p>
  <p>Intently stare at the same spot poop in the plant pot but kitten is playing with dead mouse. Get video posted to internet for chasing red dot leave fur on owners clothes meow to be let out and mesmerizing birds leave fur on owners clothes or favor packaging over toy so purr for no reason. Meow to be let out play time intently sniff hand run outside as soon as door open yet destroy couch.</p>

  <p> Some things to do that cat love : </p>

  <ul>
    <li> Drinking milk </li>
    <li> Sleeping well </li>
    <li> Playing more </li>
  </ul>

  <div>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>mice</li>
    <li>dogs </li>
    <li>being wet </li>
    </ol>
    </div>

  <form action="/submit-cat-photo">
    <input type="text" placeholder="cat photo URL" required>
      <button type="submit">Submit</button>
      <label>
       <input type="radio" name="indoor-outdoor" checked>Indoor</input>
        </label>
      <label>
        <input type="radio" name="indoor-outdoor">Outdoor</input>
          </label>
    </form>

  <p>View more <a href="http://freecatphotoapp.com" target="_blank">cat photos </a></p>
  <p>Some link will come <a href="#" target="_blank">here</a>.</p>

</main>

<footer id="footer">Copyright Cat Photo App</footer>
  </body>
</html>
```

<html>
  <head>
    <title>The best about CatPhotoApp</title>
  </head>

  <body>
    <h2>CatPhotoApp</h2>
    <main>

<a href="#footer">Jump to Bottom</a>

  <a href="#"><img src="https://bit.ly/fcc-relaxing-cat" alt="A cute orange cat lying on its back."></a>

  <p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>
  <p>Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff. Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched.</p>
  <p>Meowwww loved it, hated it, loved it, hated it yet spill litter box, scratch at owner, destroy all furniture, especially couch or lay on arms while you're using the keyboard. Missing until dinner time toy mouse squeak roll over. With tail in the air lounge in doorway. Man running from cops stops to pet cats, goes to jail.</p>
  <p>Intently stare at the same spot poop in the plant pot but kitten is playing with dead mouse. Get video posted to internet for chasing red dot leave fur on owners clothes meow to be let out and mesmerizing birds leave fur on owners clothes or favor packaging over toy so purr for no reason. Meow to be let out play time intently sniff hand run outside as soon as door open yet destroy couch.</p>

  <p> Some things to do that cat love : </p>

  <ul>
    <li> Drinking milk </li>
    <li> Sleeping well </li>
    <li> Playing more </li>
  </ul>

  <div>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>mice</li>
    <li>dogs </li>
    <li>being wet </li>
    </ol>
    </div>

  <form action="/submit-cat-photo">
    <input type="text" placeholder="cat photo URL" required>
      <button type="submit">Submit</button>
      <label>
       <input type="radio" name="indoor-outdoor" checked>Indoor</input>
        </label>
      <label>
        <input type="radio" name="indoor-outdoor">Outdoor</input>
          </label>
    </form>

  <p>View more <a href="http://freecatphotoapp.com" target="_blank">cat photos </a></p>
  <p>Some link will come <a href="#" target="_blank">here</a>.</p>

</main>

<footer id="footer">Copyright Cat Photo App</footer>
  </body>
</html>
