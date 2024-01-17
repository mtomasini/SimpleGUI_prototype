# Making scientific codes user friendly

> Author: Matteo Tomasini
>
> Date: 17.01.2024

We have all been there. You write a complex script that takes a large number of input parameters and outputs a large number of plots, tables and results, through a script that simulates a physical system, solves a system of differential equations or loops through a series of complex O/I processes. After publishing your results, you stop taking care of the code, and nobody else is able to run it on their machine or to understand how the code is done. Sometimes, you want to make your work available to other researchers without the know-how to run such a complex code. In particular, since they aren't you, they cannot wrap their head around where is it that you need to enter parameters, what parameters should not be touched, and what results are being produced.

There is a plethora of ways to avoid the problems that I described, here I focus on the simplest one: writing a GUI that wraps up the big chunk of the code that does all the operations, and presents the user with two things: a window where he can input some parameters (the parameters that your user is allowed to modify) and a window where he can select what plot to see after the simulation has ran.

I illustrate this through a simple script with a few functions that take two or three parameters, and outputs different plots.

The result looks ancient, but is perfectly functional, allowing to change parameters, run an underlying script and fetch figures directly from a folder:

![A beautiful, simple GUI!](/mockup_script_GUI_wrapper.png)