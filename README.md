Hilbert Curve
=============

3D
--

Start with the 3-bit Gray code. In order, these specify the coordinates for
the first subcube.

To get the second subcube, for each coordinate in the first subcube,
prepend the digits of the second Gray number. So, for example: if the coordinates
of the subcube were: 0,1,0 and we wished to find the corresponding coordinate
in the second subcube, given that the second 3-bit Gray number is 100, prepending
these gives: 10,01,00 = (2,1,0)

Similarly for the other subcubes. The idea generalizes to higher volume Hilbert
cubes.
