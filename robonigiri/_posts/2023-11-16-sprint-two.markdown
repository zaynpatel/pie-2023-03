---
layout: post
title:  "Sprint 2"
date:   2023-11-16 00:43:39
categories: Sprint Updates
description: "Refining our design and adding rigidity"
image: 'https://i.imgur.com/O7LpEOQ.jpg'
published: true
canonical_url: https://olincollege.github.io/development/2023/11/16/sprint-two.html
---

### Goal of Sprint 2
The goal of our second sprint was to integrate a mechanism which allowed us to add a
strip of seaweed to the device, and incorporate the required food safety considerations
after receiving feedback on this in our last sprint review.

### Kaizen
During this second sprint, we set a group kaizen of comfortably finishing our project
before the deadline. This collective goal centered on continuous improvement was achieved
by sticking to standard group organization practices (whiteboard and sticky notes), and
maintaining good communication.

### Previous designs

After our progress on Sprint 1, we had plenty of things to work on in terms of the
Mechanical, Software, and Electrical integration.

We noted some key things that needed to be addressed from our previous prototypes,
and worked to fix them in this second sprint.


{% include youtube.html video="bmqTy7l4CPA" %}

The first thing that we noticed was that when the servo was turning the arm on our rotary wheel,
it was causing the actual mold to shake around on its way up and down, which resulted in 
inconsistent pressing of the rice below. This would cause the mold to end up slicing the rice
on some runs, and other times it would cause the rice to be moved around. This would mess up
the calibration of our design, and ruin the autonomy of the process, so we needed to find a
solution to this.

{% include youtube.html video="ronWqALxMQY" %}

The second thing that we noticed which needed to be addressed was the fact that our current servo
and arm combination wasnt strong enough to fully compress the rice into the mold that we had designed.
This mean't that the rice was not actually being formed into a triangle, as it was not being pressed
with enough force to reach each of the corners in the mold. We suspected that our servo was not strong
enough, either way we needed to resolve this so that our onigiri could be in the right shape for the
next steps.

{% include youtube.html video="2On2l7vcduQ" %}

The last main issue that we needed to address in this sprint based on our previous designs was the overall
structural flex that took place whenever we started the servo to begin the molding process. This issue was
mainly due to the lack of strength in our structure, mainly caused by the low infill %. We were easily able
to account for this by redesigning our pieces with thicker edges and printing them with a much higher infill.

### Sprint 2 Progress

Based on the above concerns we found in our previous designs, as well our preexisting goals for sprint 2, we
were able to make substantial progress towards our goal for demo day.

#### Mechanical Updates

On the mechanical side of things, we worked to design and fabricate a more rigid design which took into account
all of the issues regarding flex and wobbling. We used a hiher infill percentage when printing the designs, and
increased the thickness of most of the parts in order to make the overall design much more structurally sound.

#### Software Updates

On a software side of things, we completely redesigned the website to have this format, and it was setup in a way
that allowed us to add scripts for the arduino library. We also did some research on microcontrollers that would
best interface with the existing arduino setup and at the end of our sprint, we decided that it would be easiest
to upgrade to the Arduino to the UNO R4 with WiFi, and setup a local port that would listen for a button press on
a website. We also looked at setting up a control loop that would incrementally turn the servo to press the rice
rather than a fully continuous motion.