### 1.2. Basic CSS

* All in one study notes : [notes](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS.md)
---------
Cascading Style Sheets (CSS) tell the browser how to display the text and other content that you write in HTML.

Note that CSS is case-sensitive so be careful with your capitalization. CSS has been adopted by all major browsers and allows you to control:

* color
* fonts
* positioning
* spacing
* sizing
* decorations
* transitions

There are three main ways to apply CSS styling. You can apply inline styles directly to HTML elements with the style attribute. Alternatively, you can place CSS rules within style tags in an HTML document. Finally, you can write CSS rules in an external style sheet, then reference that file in the HTML document. Even though the first two options have their use cases, most developers prefer external style sheets because they keep the styles separate from the HTML elements. This improves the readability and reusability of your code. The idea behind CSS is that you can use a selector to target an HTML element in the DOM (Document Object Model) and then apply a variety of attributes to that element to change the way it is displayed on the page.

In this section, you'll see how adding CSS styles to the elements of your CatPhotoApp can change it from simple text to something more.


**Lessons**
1. [Change the Color of Text](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/1.%20Change%20the%20Color%20of%20Text.md)
2. [Use CSS Selectors to Style Elements](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/2.%20Use%20CSS%20Selectors%20to%20Style%20Elements.md)
3. [Use a CSS Class to Style an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/3.%20Use%20a%20CSS%20Class%20to%20Style%20an%20Element.md)
4. [Style Multiple Elements with a CSS Class](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/4.%20Style%20Multiple%20Elements%20with%20a%20CSS%20Class.md)
5. [Change the Font Size of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/5.%20Change%20the%20Font%20Size%20of%20an%20Element.md)
6. [Set the Font Family of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/6.%20Set%20the%20Font%20Family%20of%20an%20Element.md)
7. [Import a Google Font](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/7.%20Import%20a%20Google%20Font.md)
8. [Specify How Fonts Should Degrade](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/8.%20Specify%20How%20Fonts%20Should%20Degrade.md)
9. [Size Your Images](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/9.%20Size%20Your%20Images.md)
10. [Add Borders Around Your Elements](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/10.%20Add%20Borders%20Around%20Your%20Elements.md)
11. [Add Rounded Corners with border-radius](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/11.%20Add%20Rounded%20Corners%20with%20border-radius.md)
12. [Make Circular Images with a border-radius](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/12.%20Make%20Circular%20Images%20with%20a%20border-radius.md)
13. [Give a Background Color to a div Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/13.%20Give%20a%20Background%20Color%20to%20a%20div%20Element.md)
14. [Set the id of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/14.%20Set%20the%20id%20of%20an%20Element.md)
15. [Use an id Attribute to Style an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/15.%20Use%20an%20id%20Attribute%20to%20Style%20an%20Element.md)
16. [Adjust the Padding of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/16.%20Adjust%20the%20Padding%20of%20an%20Element.md)
17. [Adjust the Margin of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/17.%20Adjust%20the%20Margin%20of%20an%20Element.md)
18. [Add a Negative Margin to an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/18.%20Add%20a%20Negative%20Margin%20to%20an%20Element.md)
19. [Add Different Padding to Each Side of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/19.%20Add%20Different%20Padding%20to%20Each%20Side%20of%20an%20Element.md)
20. [Add Different Margins to Each Side of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/20.%20Add%20Different%20Margins%20to%20Each%20Side%20of%20an%20Element.md)
21. [Use Clockwise Notation to Specify the Padding of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/21.%20Use%20Clockwise%20Notation%20to%20Specify%20the%20Padding%20of%20an%20Element.md)
22. [Use Clockwise Notation to Specify the Margin of an Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/22.%20Use%20Clockwise%20Notation%20to%20Specify%20the%20Margin%20of%20an%20Element.md)
23. [Use Attribute Selectors to Style Elements](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/23.%20Use%20Attribute%20Selectors%20to%20Style%20Elements.md)
24. [Understand Absolute versus Relative Units](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/24.%20Understand%20Absolute%20versus%20Relative%20Units.md)
25. [Style the HTML Body Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/25.%20Style%20the%20HTML%20Body%20Element.md)
26. [Inherit Styles from the Body Element](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/26.%20Inherit%20Styles%20from%20the%20Body%20Element.md)
27. [Prioritize One Style Over Another](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/27.%20Prioritize%20One%20Style%20Over%20Another.md)
28. [Override Styles in Subsequent CSS](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/28.%20Override%20Styles%20in%20Subsequent%20CSS.md)
29. [Override Class Declarations by Styling ID Attributes](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/29.%20Override%20Class%20Declarations%20by%20Styling%20ID%20Attributes.md)
30. [Override Class Declarations with Inline Styles](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/30.%20Override%20Class%20Declarations%20with%20Inline%20Styles.md)
31. [Override All Other Styles by using Important](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/31.%20Override%20All%20Other%20Styles%20by%20using%20Important.md)
32. [Use Hex Code for Specific Colors](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/32.%20Use%20Hex%20Code%20for%20Specific%20Colors.md)
33. [Use Hex Code to Mix Colors](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/33.%20Use%20Hex%20Code%20to%20Mix%20Colors.md)
34. [Use Abbreviated Hex Code](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/34.%20Use%20Abbreviated%20Hex%20Code.md)
35. [Use RGB values to Color Elements](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/35.%20Use%20RGB%20values%20to%20Color%20Elements.md)
36. [Use RGB to Mix Colors](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/36.%20Use%20RGB%20to%20Mix%20Colors.md)
37. [Use CSS Variables to change several elements at once](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/37.%20Use%20CSS%20Variables%20to%20change%20several%20elements%20at%20once.md)
38. [Create a custom CSS Variable](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/38.%20Create%20a%20custom%20CSS%20Variable.md)
39. [Use a custom CSS Variable](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/39.%20Use%20a%20custom%20CSS%20Variable.md)
40. [Attach a Fallback value to a CSS Variable](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/40.%20Attach%20a%20Fallback%20value%20to%20a%20CSS%20Variable.md)
41. [Improve Compatibility with Browser Fallbacks](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/41.%20Improve%20Compatibility%20with%20Browser%20Fallbacks.md)
42. [Cascading CSS variables](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/42.%20Cascading%20CSS%20variables.md)
43. [Change a variable for a specific area](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/43.%20Change%20a%20variable%20for%20a%20specific%20area.md)
44. [Use a media query to change a variable](https://github.com/hevalhazalkurt/Learn_Code_Study_Notes/blob/master/freeCodeCamp/Responsive_Web_Design_Certification_(300_hours)/02_Basic_CSS/44.%20Use%20a%20media%20query%20to%20change%20a%20variable.md)
