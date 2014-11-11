Hilbert Curve
=============

[Hilbert Curves](http://en.wikipedia.org/wiki/Hilbert_curve) are space filling
curves with the provable best loccality characteristics - for example, given
a two-dimensional Hilbert curve, points that are close by on the plane will be
close by on the curve as well.

This is an attempt to map the RGB color space onto a 2D plane using Hilbert curves
so that the transitions between colors are as smooth as posisble - that is, colors
that are nearby in RGB space will be nearby picture.

[Hamilton's paper on the subject](https://www.cs.dal.ca/sites/default/files/technical_reports/CS-2006-07.pdf) is extremely illuminating, and was my primary source for an understanding of the
ideas involved in higher-dimensional Hilbert curves.

[The Wikipedia page](http://en.wikipedia.org/wiki/Hilbert_curve) is also a good
resource, and has a relatively easy-to-understand implementation of the
coordinate transforms for the 2D curve.

This project was an attempt to traverse the entire RGB space through a Hilbert
curve in 3 dimensions and then draw the result as a Hilbert Curve in 2 dimension.
The resulting picture will soon be uploaded.
