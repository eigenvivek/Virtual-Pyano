# Virtual-Pyano
I attempt to build a virtual piano using Python and a Leap Motion Controller! Watch me fail miserably!

Current capabilities:
As of January 18, 2017, the program tracks the 1-dimensional motion of the index finger (on either hand) and maps the x-position to a note in the C major pentatonic scale.

To do:
1. Add functionality for all fingers across both hands.
2. Make a better way of programming in the piano.
3. Add a y-component so that if y>threshold, a note is not being pressed.
4. Factor in the velocity of the finger such that velocity is proportional to volume (also means I have to program a volume variable rip)
5. Integrate the tech with a Raspberry-Pi to create a handheld, virtual midi controller.

Note: All files in the `lib` folder are only designed to work on Macs. To get the libraries that work with Windows or Linux, download the [Leap Motion SDK](https://developer.leapmotion.com/get-started) and replace the appropriate files in the `lib` folder.
