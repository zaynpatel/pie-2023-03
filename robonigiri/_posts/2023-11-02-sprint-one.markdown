---
layout: post
title:  "Sprint 1"
date:   2023-11-02 11:59:07
categories: Sprint Updates
description: "Creating the initial MVP of our system"
image: 'https://i.imgur.com/KEgyJr2.jpeg'
published: true
canonical_url: https://olincollege.github.io/development/2023/11/02/sprint-one.html
---

### Goal of Sprint 1
For our first sprint, our goal was to create a device that could compact something into a triangle.
We used Play-Doh for testing at this phase. We had defined goals for each of the mechanical, software,
and electrical components, although at this stage our work was mostly on the mechanical side of things.

### Kaizen


### Mechanical Progress
In this first sprint, we made several iterations on the overall structure of our onigiri maker. We designed
a chassis for the servo, and a rotary linking system that allowed for the servo to rotate a pinwheel and push our
test mold up and down. We iterated on our designs many times, but the rapid protoyping approach we used meant that
we were able to test the validity of our designs quickly and easily.

### Electrical Progress
On the electrical side of things, we implemented a simple servo that would control the rotary pinwheel which allowed
our arm to slide up and down to compress our "rice". For the sake of validating the structural integrity of our first
design, we simply set the servo to continuously turn. From this we were able to observe if the servo was strong enough
to compress our test material enough for it to take the shape of our mold. If it wasn't strong enough, we would know
that a standard servo was not sufficient and would plan upgrades for the future. Below is an video of our servo turning
the pinwheel to operate our onigiri maker.

{% include youtube.html video="OMwqEoHgNKc" %}

### Software Progress
In terms of software, there wasnt much to add in terms of our existing mechanical integration. We did want to explore our
goal of wirelessly operating our onigiri maker, and the first step in this was to create a very basic UI that could interface
with the serial connection of our arduino over a protocol called [I2C](https://learn.sparkfun.com/tutorials/i2c/all). We were
successfully able to create a basic UI using [Processing](https://processing.org/), and below is an example of us using this UI
to toggle a simple LED circuit.

{% include youtube.html video="tQFH7VOESeo" %}