# Movie Site README

Movie is a project that **creates** a web page to display an _interactive_ list of movies.

It includes _three_ pieces of code:

- [media.py](#p1)
- [entertainment_centre.py](#p2)
- [fresh_tomatoes.py](#p3)

## (how to) Make it yours

To create _your very own_ movie site (see [license](#p4))

You can find this code on my [github](https://github.com/bran-don/RottenPotatoes)

Unless we have the same set of favorite movies, you will want to create your own list. Edit [entertainment_centre.py](#p2) to replace my movies with your own.
I have six movies, you can make more or less; but you must change the movies list to represent your movie objects. Note* class movie (in [media.py](#p1)) has six attributes, only 5 are being used currently (see [CONTRIBUTE](#p5))

Once you have created your movie objects and a list `movies[]` with your movie objects, run [entertainment_centre.py](#p2) to render an html webpage in current working directory.

This webpage should open in your default browser.

## code
#### <a name="p1"></a>media.py
###### Defines class movie with following attributes:
1. Title
2. Storyline
3. Poster Image
4. Trailer link (youtube)
5. Length
6. Rating
#### <a name="p2"></a>entertainment_centre.py
1. Create instances of class movie
2. Create list of those movie instances
3. Call [fresh_tomatoes.py](#p3) to create HTML/CSS webpage with list
#### <a name="p3"></a>fresh_tomatoes.py
- Function `open_movies_page()`  uses `create_movie_tiles_content()` with HTML&CSS to render web page populated by `movies[]` in [media.py](#p1)


- Web page will be created in directory containing above files.
### <a name="p5"></a>CONTRIBUTE

I encourage your contribution to extending this project.

Movie class objects contain a storyline attribute that I have yet to implement on website. I would like to see this on a hover tooltip, project for later!

Send me an update with any interesting developments brandon.actual@gmail.com

### <a name="p4"></a>LICENSE

This content is licensed under a GNU General Public License v3.0. See [license](./LICENSE.txt)