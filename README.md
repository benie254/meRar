# meRar

An image gallery app, generated with [Python](https://www.python.org/) version 3.8.13 for [Django](https://www.djangoproject.com/) version 4.4.0 

# meRar
#### This repo creates an image gallery website, which consumes an api and utilizes a database for data storage, retrieval, and manipulation.
## Author
[Benson Langat](https://github.com/benie254)

## Description

meRar is a simple website gallery, displaying photos from different categories, posted at different times, and from different locations. Users can click on images to expand their details view; users can also follow a link to get more details about a selected photo. On top of these, is a functionality to copy an image's link and share in across social platforms. 
The app enables content creators/admins `CRUD` functionalities to Create, Read, Update, and Delete images and their content/details. 


## Screenshot--Home Page

<img src="https://user-images.githubusercontent.com/99865051/170883835-6983266d-4eba-4f25-a19d-e13c8b594741.png" >

## Screenshot--Modal--Home Page

<img src="https://user-images.githubusercontent.com/99865051/170883871-f57b62a9-3c54-4ab3-8a86-9219de242fca.png">

## Screenshot--Image Details Page

<img src="https://user-images.githubusercontent.com/99865051/170883932-2b4f09bf-3eb3-4e67-9f64-1d2e7491acce.png">


## Behavior Driven Development--BDD

**1. Home Page**
   - OUTPUT: 'Navbar', 'Home page content'
   
**2. User Action:** 
   - INPUT:  Click : Navbar : 'meRar', 'HOME'
   - OUTPUT: Home page
   - OUTPUT: All Images

**3. User Action:**
   - INPUT:  Click : Image object
   - OUTPUT: Modal, Image details
   - INPUT:  Click : Close
   - OUTPUT: Home Page
   - INPUT: Click : 'Read more'
   - OUTPUT: Single image page
   - OUTPUT: The selected image's details
   - OUTPUT: Image title, Image, Image category
   - OUTPUT: Image details
   - OUTPUT: Image location, Image tags, Image editor, Image publish date/time, Get image link button
   - INPUT:  Click: Get Link
   - OUTPUT: Image link, Copy image link Button
   - INPUT:  Click : Copy Link

**4. User Action:**
   - INPUT:  Input : Navbar : 'Search by tag',
   - OUTPUT: Image results--image results page 
   - INPUT:  Input : Navbar : 'Search by category',
   - OUTPUT: Image results--image results page
   - INPUT:  Input : Navbar : 'Search by location',
   - OUTPUT: Image results--image results page

**5. User Action:**
   - INPUT:  Click : Navbar : 'meRar','Home'
   - OUTPUT: All images

**6. User Action:**
   - INPUT:  Click : Browser Page : Close
   - Exits


## Setup/Installation Requirements

* To use this open-source repo, clone it; to contribute, fork it. 
* Open your Terminal (CTRL + ALT + T on Ubuntu/Linux). 
* Make a destination directory in your preferred path (where you would like to clone the repo into.)
* Run the command ``` cd yourDestinationDirectory ```
* Run the command ``` git clone https://github.com/benie254/meRar.git ``` to clone the repo into your destination directory. 
* Run the command ``` cd meRar ``` to move you into this repo's directory.
* Run the command ``` atom . ``` for Atom or ``` code . ``` for VSCode --opens the directory in your preferred code editor. (it is okay if you use something different.)
* Happy coding!

## Known Bugs

No known bugs. Please report any issues or encountered bugs! 

## Technologies Used

* [Python](https://www.python.org/) 
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)

## Other Resources 

* [Bootstrap](https://getbootstrap.com/) -- page designs
* [Adobe Color Wheel](https://color.adobe.com/) -- color palette 
* [Coolors](https://coolors.co/) -- color palette
* [Google Fonts](https://fonts.google.com) -- stylized fonts


## Support and contact details

Reach out with any issues, concerns, or contributions to [Benie-throughMail](davinci.monalissa@gmail.com)

### License

*Copyright (c) 2022* ***Benson Langat***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

###
Copyright (c) 2022 **Benson Langat**

[Python](https://www.python.org/) version 3.8.13
