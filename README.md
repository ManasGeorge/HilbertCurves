Hilbert Curve
=============

[Hilbert Curves](http://en.wikipedia.org/wiki/Hilbert_curve) are space filling
curves with the provable best locality characteristics - for example, given
a two-dimensional Hilbert curve, points that are close by on the plane will be
close by on the curve as well.

This is an attempt to map the RGB color space onto a 2D plane using Hilbert curves
so that the transitions between colors are as smooth as possible - that is, colors
that are nearby in RGB space will be nearby picture.

[Hamilton's paper on the subject](https://www.cs.dal.ca/sites/default/files/technical_reports/CS-2006-07.pdf) is extremely illuminating, and was my primary source for an understanding of the
ideas involved in higher-dimensional Hilbert curves, although there is a subtle
bug that trips up implementation.

[The Wikipedia page](http://en.wikipedia.org/wiki/Hilbert_curve) is also a good
resource, and has a relatively easy-to-understand implementation of the
coordinate transforms for the 2D curve.

This project was an attempt to traverse the entire RGB space through a Hilbert
curve in 3 dimensions and then draw the result as a Hilbert Curve in 2 dimensions.

![hilbertrgb](https://cloud.githubusercontent.com/assets/1315728/4989633/4b87920c-6949-11e4-9684-6ab5d75757a4.png)

Last of all, a shout out to [Aldo Cortesi](http://corte.si/), whose implementation
I found after writing my own. Aldo also produces visualizations for alternative
traverals of RGB space, wrapping them up in a nice helper program.

Further development will focus on documenting the code, trying to explain some
of the math more intuitively, cleaning up the code, and comparing alternative
traversals of RGB space. I also intend to implement a "sort" feature that
takes a picture, maps its pixels to a Hilbert Curve in 3D, sorts the pixels by
distance along the curve, and draws the result as a 2D Hilbert curve.

This picture was created by simply mapping every single color in RGB space to
a point in the picture plane, no fancy traversals involved.

![vanillargb](https://cloud.githubusercontent.com/assets/1315728/4998116/52ac4820-69a3-11e4-9874-77f3bb00d603.png)


This picture was created by mapping a straight traversal of RGB space to a hilbert
curve traversal of the picture plane.

![vanillargbhilbert](https://cloud.githubusercontent.com/assets/1315728/4998126/655aa566-69a3-11e4-9344-55e03d0ad694.png)
