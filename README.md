<HTML>
<head>
<title>Gimp Colour Shift plugin</title>
</head>
<body>
<h1>Gimp Colour Shift plugin</h1>
This plug in will take between 2 and 5 input colours and their corresponding outputs. Only the first <b>ColourSwaps</b> pairs of <b>from</b> and <b>to</b> values are used. The rest are ignored. It will transform the colours in such a way that each input is replaced by its output. Intermediate colours are smoothly interpolated. See examples. Colour swap transforms colours only. It does not rely on the spacial location of pixels or attempt to find objects. The filter takes about 5 seconds on a 3 Mb image. Twice as long as a scaling.

<h2>Plug in</h2>
<img src="PlugIn.jpg" >
<h2>Image before filter</h2>
<img src="BeforeFlower.jpg" >
<h2>Image after multiquadric filter</h2>
<img src="multiquadricFlower.jpg" />
<h2>Image after cubic filter</h2>
<img src="cubicFlower.jpg" />
<h2>Image after gaussian filter</h2>
<img src="gaussianFlower.jpg" />
<h2>Image after linear filter</h2>
<img src="linearFlower.jpg" />
<h2>Image after inverse filter</h2>
<img src="inverseFlower.jpg" />
<h2>Image after thin_plate filter</h2>
<img src="thin_plateFlower.jpg" />
<h2>Image after quintic filter</h2>
<img src="quinticFlower.jpg" />
<h2>Todo</h2>
Change UI from gimpfu standard to put <b>from</b> and <b>to</b> colours side by side. Add a plus button to add new colour pairs instead of a slider. Allow the interpolation to be done over the HSV colour space. Allow interpolation between gradients or pallets.
</body>
</html>
