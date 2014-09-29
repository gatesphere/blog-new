--- 
tags: [processing, mobile processing, blackberry, development, rim]
date: 2012-09-12
title: Using Mobile Processing on the BlackBerry

Hello all,

I recently was able to get [Mobile Processing](http://mobile.processing.org/)
working for Java development on the BlackBerry plug-in for Eclipse, and it
works wonderfully.  I thought I'd share my process for anyone who is interested.
It even works intermingled with the BlackBerry API, aside from the UI classes.

What you need
-------------
To do this, you will need the following:

  - A copy of Eclipse with the [Java BlackBerry Plug-in](https://developer.blackberry.com/java/download/eclipse) installed
  - A copy of [Mobile Processing](http://mobile.processing.org/download/index.php)
  
That's it.  No need to download the WTK/CLDC, or JavaME, etc.

Using the following steps, you can create a project that uses Mobile Processing
targeting the BlackBerry.

Preliminaries
-------------
First, extract the Mobile Processing archive you downloaded.  Find the lib/ 
directory with all the .jars, and save it somewhere you know you'll be able
to find it later.  This is where the core of Mobile Processing lives.

Make a new project
------------------
From within Eclipse, do: File -> New -> New Project.  Select BlackBerry Project
and click Next >.  On the next screen, give it a name, and choose the JRE
for the OS level you are targeting, and click Next >.  On this next screen,
click on the Libraries tab up top, then click Add External JARs, navigate
to the lib/ directory you saved earlier, and select mobile.jar.  Now click
on the Order and Export tab up top, and make sure the checkbox next to mobile.jar
is checked (it most likely is not by default).  Click Next > again, then
select Empty Application, and click Next >.  Give it a package name and
a class name, and click Finish.

Configuration of the project
----------------------------
Open up the BlackBerry_App_Descriptor.xml file for your newly created
project.  Give it a proper title, version, vendor, and description.  Under
Application type, select MIDlet.  Then type the fully-qualified name of
your app's main class (i.e. suschord.processingtest.HelloWorld).  Save.

Code!
-----
To use the Mobile Processing API in your project, your main app class has
to `import processing.core.PMIDlet;`, and also be declared that it
`extends PMIDlet`.  You should get rid of any `main()` function... it cannot
be used here, `PMIDlet` includes a `main()` that does all the right things.
You should create at least two functions, `public void setup()` and `public
void draw()`.

At this point, you have a working Mobile Processing sketch.  Any code you 
place inside your main app class will work exactly as if you were coding
a Mobile Processing sketch.

Here's an example of an application that draws lines from the center of the
screen to random points across the screen, in random colors.

    package suschord.processingtest;

    import processing.core.PMIDlet;

    public class HelloWorld extends PMIDlet {
      int white;
      int x, y, center_x, center_y;
      int linecolor;
      
      public void setup() {
        white = color(255);
        background(white);
        center_x = width / 2;
        center_y = height / 2;
        framerate(15);
      }
      
      public void draw() {
        linecolor = randcolor();
        x = randx();
        y = randy();
        stroke(linecolor);
        line(center_x, center_y, x, y);
      }
      
      int randcolor() {
        return color(random(255), random(255), random(255));
      }
      
      int randx() {
        return random(width);
      }
      
      int randy() {
        return random(height);
      }
    }

The method definitions `randcolor()`, `randx()`, and `randy()` are unnecessary,
but I thought I'd throw them in to demonstrate that methods work the same
way here as they do in Mobile Processing.

Making it Exciting
------------------
Now that you have a Mobile Processing sketch running on your BlackBerry, it's
time to start working the RIM API to talk with the BlackBerry device.

Here's an example which uses accelerometer data to determine the colors of the lines
from the previous example:

    package suschord.processingtest;

    import net.rim.device.api.system.AccelerometerSensor;
    import net.rim.device.api.system.Application;
    import processing.core.PMIDlet;

    public class HelloWorld extends PMIDlet {
      int white;
      int x, y, center_x, center_y;
      int linecolor;
      AccelerometerSensor.Channel accl;
      short[] xyz = new short[3];
      
      public void setup() {
        accl = AccelerometerSensor.openRawDataChannel(Application.getApplication());
        white = color(255);
        background(white);
        center_x = width / 2;
        center_y = height / 2;
        framerate(15);
      }
      
      public void draw() {
        linecolor = accelcolor();
        x = randx();
        y = randy();
        stroke(linecolor);
        line(center_x, center_y, x, y);
      }
      
      public void destroy() {
        accl.close();
      }
      
      int accelcolor() {
        accl.getLastAccelerationData(xyz);
        return color(xyz[0], xyz[1], xyz[2]);
      }
      
      int randx() {
        return random(width);
      }
      
      int randy() {
        return random(height);
      }
    }

From my tests, this works with most of the RIM API, aside from the UI classes.
Even code that needs to be signed works.  There are some caveats with using
Mobile Processing, though.  One major issue is that MIDlets cannot automatically
start when the device does.  I'm looking for a workaround for this, or a way
to compile and deploy as a native app.  Time will tell if I can make this work,
however.  Future posts will explain how to listen for keyboard/trackball events, 
touchscreen events, etc.

Thanks for reading!