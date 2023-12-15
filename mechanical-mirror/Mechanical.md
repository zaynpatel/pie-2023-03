# Mechanical 
Walk through the Sprints and explain the ideation process and build methods, what worked, what didn’t, pivots made and why
(Add CAD and Product Images with Descriptions)


# Basic Design used for all sprints.
<div style="text-align: center;">
  
![A simple diagram demonstrating the basic design working principles](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/MMMechanismPrinciples.png "Mechanism Principles Diagram")

</div>


Our basic design consists of a grid of drum-shaped pixels with integrated gears that rotate to change what color is currently exposed to a viewer. The axis of rotation is parallel to the X axis (if X is left-right, Y is up down and Z is pointing out of the plane of the mirror). On the back of the mirror, a gantry mechanism flips pixels column by column to display an image, by rotating each to display a desired state.

The gantry system consists of a vertical arm the height of the mirror (which we call the vertical servo arm, or VSA) that moves horizontally across the back of the display. A single servo motor is mounted for every pixel row of the mirror to the vertical servo arm. The horizontal movement is controlled by two lead screws powered by two stepper motors. 

Each servo has a gear on it. As the VSA moves across the mirror, the gear aligns with each pixel in a row and can rotate it to a desired state. Each gear has a section of missing teeth to allow the gear to align with a pixel gear without physical conflict. After the arm aligns the gears with the first column of pixels it stops at that position. Then the servos rotate the gears until the teethed sections on them mesh with and rotate their respective pixels in the column. After completing a column, the vertical servo arm moves to the next column with the toothless section of the gear facing the board. The process repeats until all columns have been addressed by the arm and the array is displaying the desired image. 

We used this design to prevent the need for a servo for every single pixel, as that would not be scalable in terms of overall cost.


![A rendering of the pixel design used for sprint 1 and 2](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/PixelSp12.png "Sprint 1 and 2 pixel")
![A rendering of the pixel design used for sprint 3](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/PixelSp3.png "Sprint 3 pixel")

The pixel design for sprint 1 sprint 2 (left), and sprint 3 (right) this pixel design worked well and was actuated by a similarly sized gear connected to the VSA. For sprints 1 and 2 each pixel had its mounting frame that it would spin freely inside of while in sprint 3 the pixel was directly mounted (while still able to free spin) to the mirror. Colored black and white these will form the image drawn upon the mirror.




![A rendering of the Vertical Servo Arm design used for sprint 1](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/VSASp1.png "Sprint 1 Vertical Servo Arm")
![A rendering of the Vertical Servo Arm design used for sprint 2](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/VSASp2.png "Sprint 2 Vertical Servo Arm")
![A rendering of the Vertical Servo Arm design used for sprint 3](https://github.com/mcuevas-olin/pie-2023-03/blob/gh-pages/mechanical-mirror/Images/VSASp1.png "Sprint 3 Vertical Servo Arm")

The Vertical Servo Arm (VSA) design for sprint 1 (left), sprint 2 (center), and sprint 3 (right). Each consists of a large arm moved by the linear screw actuators back and forth containing servos with the gears to mesh with each pixel. This is what moves collum by collum meshing with and then rotating pixels to change what color they display thus drawing an image on the mirror.




## Sprint 1:
For our first design, we wanted to make a simple proof of concept. We made a 2x2 mirror with one threaded rod acting as a lead screw and one stepper motor. The pixels were drum-shaped with gear teeth on one end. It was mostly 3D printed and constructed out of PLA. Overall, it was a very rough, but working, prototype.

Each pixel was attached with paper straws to a rectangular PLA frame where it was free to rotate. These frames with the pixels within were glued together and attached to a larger base.

The pixel structure was then glued to the square structure with the stepper-motor-powered vertical servo arm. The moving servo arm was further locked in place by 2 dowels that helped guide its movement. This square structure was then glued to the piece containing the pixels. The threaded rod was a simple one designed for construction and thus was held in place by multiple nuts and bolts and the VSA was attached to it with a nut as well. 2 servos, each with a gear attached to it, are mounted to the VSA. 

We used a scrap threaded rod as a lead screw, instead of a proper lead screw with a larger pitch. Due to our unfamiliarity with lead screws, we wanted to test whether the idea would work before ordering one. The threaded rod we used has a much lower pitch than the lead screws used in Sprints 2 and 3, so traversal along it was very slow. However, it provided proof of concept that the design would work.


(A view of our sprint 1 design as it was in the CAD.)



(A view of our completed sprint 1 design of the front mechanisms not in view)

## Sprint 2: 
For the second version, we ambitiously scaled the mirror up to a 5 by 5-pixel design again using the same basic principles. We used the pixel design mounted with paper straw to a PLA frame design, but we added a laser-cut MDF board with 25 square holes in the 5 x 5 pattern where each pixel-frame couple could be glued to a hole in the board. The pixels were colored white on one side with gaffer tape. 

We made a frame out of aluminum 80-20, to which the board could be mounted. The 80-20 frame acts as a structural support for all physical components of the design, and acts as a stand for the mechanical mirror.

We ordered two actual lead screws to use in our Sprint 2 gantry. These were mounted to the top and bottom of the back of the frame, and powered by two stepper motors. They powered the VSA used to actuate the pixels. 

Our Sprint 2 VSA was a flat plate of laser-cut MDF with holes in it for mounting servos and that was done. Attached to the servos was a new gear design that increased the size and teeth count to better optimize how the pixels were turned. A 3D-printed PLA adapter with a nested brass nut connected the top and bottom of the VSA to each lead screw.

Cad screenshot placeholder

(A view of our sprint 2 design in CAD)


(A rear view Photo of our sprint 2 design ) 


## Sprint 3:
For Sprint 3, we decided to pursue a slightly more ambitious design. We chose to do a 15 x 15 array of pixels, in which each individual pixel is much smaller. We also decided to test a more complicated gantry design to attempt to improve the overall reaction speed of the mirror.

Instead of 3D printing pixels out of PLA, we laser cut them out of ¼” medium-density fiberboard and then painted them black and white. Each pixel is free spinning in 2 PLA mounts glued to an MDF board with holes for each pixel. Attached also to the free spinning pixel is a gear. The pixel board uses the same basic principle as our first two designs, but in a column, the orientation of the gear teeth on the pixel is staggered a bit to allow for more spacing. 

We made no significant differences in how we mounted the stepper motors and lead screws to the 80-20 frame. However, we re-sized the VSA to allow for 15 servo motors to be mounted on one arm, one for each row. In addition, we added a second VSA, so that each row had two servos allocated to it.

To improve the overall speed of the mirror, we decided to test a more complicated design for turning pixels. Instead of a single gear, each servo powered a wooden dowel acting as an axle. Attached to the dowel are 3 spaced gears for turning pixels. The gears are spaced such that only one gear ever aligns with a pixel at once. This reduces the distance a servo has to travel by roughly ⅓ and makes it so that the VSA only has to move a short distance to address large portions of the grid. 

As a fallback plan for if we ran out of time, we made it possible for the design to be scaled back to the original VSA design we used in sprint 2, where each servo has only one gear attached to it. After some initial testing of the more ambitious VSA design, we had to scale back down to the original design. Because of impending deadlines, the fabrication was done quickly and haphazardly, and as a result, the product wasn’t precise enough and the fallback plan was successfully implemented resulting in our sprint 3 design. 

(A view of our sprint 3 / final design in CAD)

(a front view of the sprint 3 design mechanisms not in view)
