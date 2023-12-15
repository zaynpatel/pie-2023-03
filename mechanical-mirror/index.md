# Mechanical Mirror
You are the art
# Table of Contents

> We have consolidated our other pages here for ease of access.
> - [Software](/mechanical-mirror/Software)
  >   - The algorithms and methods used to get our final output from our input data
> - [Firmware](/mechanical-mirror/Firmware)
  >   - The code that controls the servos
> - [Electrical](/mechanical-mirror/Electrical)
 >    - Wiring and Servos Galore!
> - [Mechanical](/mechanical-mirror/Mechanical)
 >    - The Visible (and hidden) mechanics behind the magic!

> - [About the Team](/mechanical-mirror/About)
 >    - More information about the team behind the project (Ale, Dominic, Lauren, Pauleen, and Rohan)

> - [Bill of Materials](/mechanical-mirror/BillofMaterials)
 >    - A list of components, materials, and their associated costs.


# About the Project
We made a mechanical mirror, which is a mechanical display that displays anyone who stands in front of it.

# Examples
## Example before and after photos:

## Example Video:

# How it all ties together

![A System diagram showing how all the different parts interconnect.](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/SystemDiagramFinal.jpg "System Diagram")

Our system has 4 subsystems. The gantry, the VSA, the screen, and the user interaction system. The Raspberry Pi and the Arudino monitor the user interaction, perform all of the necessary computation, and send commands to the VSA and gantry. The stepper motors in the gantry move the VSA across the columns of the screen of pixels. The servos on the VSA are each able to turn the pixels in one row of the screen. By having the Raspberry Pi and and Arduino move the VSA across the screen of pixels and turn specific servos at specific times, we can display an image on the screen.


# Design Rationale

During each sprint, all the subteams met to decide what route to take based on the learnings from the previous sprint product. For the initial sprint, our team looked ahead to what we wanted to create in each sprint and decided to slowly scale up the size of our matrix display. To make a large display, we noticed buying over 100 servos to make just a 10x10 matrix would be out of our budget. This led us to design a vertical servo arm that moves across and changes a column of servos at a time. The trade-off to this was we would not be able to capture a moving image of a person in real-time, but instead, take snapshots every few seconds and have a delay before showing the full image. We only would have needed 4 servos for the first sprint, but we decided to test the vertical servo arm and used only 2 servos for a 2x2 matrix. This sprint design performed well but was very slow to display the image as we used a regular threaded rod instead of a lead screw with a larger pitch. This working model demonstrated proof of concept so we continued with the design and made some adjustments to scale and speed up the design. We also focused on modularity as we thought if a pixel were to break it would be hard with a larger pixel count to replace all of them. We scaled up the design to a 5x5 matrix and kept the PLA 3D-printed tiles and gears. To increase the reliability, we implemented a second stepper motor, and to increase speed, we bought proper lead screws meant for linear actuation. This design worked well. The individual pixels were redesigned to be modular and easily put in and taken out. As expected, with a 5x5 it was hard to display the shape of a person standing in front. When creating this design, there was a significant amount of PLA material used and a lot of time to print the pixels, so for the final design we switched to using MDF and laser cutting the parts. For the final sprint, we decided to create a 15x15 matrix that would involve 225 individual pixels and more clearly display a person's figure. Laser cutting made the process of cutting out the pixels and gears faster, but integrating 200 more pixels than the previous sprint took many hours of work as each pixel took about five minutes to fully assemble. This backlogged a lot of our team’s time so we were not able to fully test and integrate our design until later than expected. For the final sprint, our team also incorporated a second vertical servo arm to speed up the pixel display further and added offset gears so the stepper motors would not have to move as far to show the full display. When testing, the gears on the servo arm were not aligning with all the pixels. Following time constraints, we decided to switch back to one vertical servo arm and a single set of gears. This system works and it allows the Mechanical Mirror to accurately illustrate a figure of a person in front.


# Project Objectives 

> Designing a modular pixel display
  >  - The point of this goal was to be able to fix broken pixels easily. We achieved modularity by designing the parts to be easily put in and taken out with a snap-fit. 
> Scaling the display during each iteration 
  >  - To demonstrate proof of concept, the team started small and worked their way up. Each sprint involved a larger display than the previous as the matrix went from a 2x2, 5x5, to a 13x15.

> Creating an interactable piece of art
  >  - For the demo day, we wanted our project to be something those checking out the project could get involved in. By making a moving piece of art, users were able to capture a photo of themselves and then see the mirror display their figure. 

> Sticking to a timeline
  >  - Team check-ins were a priority to stay on top of deadlines. The team practiced the scrum management style by working through three sprints and logging tasks. 


# Link to Github
