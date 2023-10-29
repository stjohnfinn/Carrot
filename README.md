# Carrot

The goal of this project is to implement a neural network that can play Diep.io. It will be trained using reinforcement learning. Those are the only requirements. 

I think it's very likely I will have several convolution layers in the neural network. I'm not sure how accurately we are going to be able to reward the network. Diep.io's score is not an element in the DOM as far as I know. Rather, it's a font drawn to the screen with the Canvas API or whatever graphics API they are using to draw their game. Right now I expect that score will be the only plausible rewardable action. Destroying polygons and other tanks will be incredibly hard to detect because I think my input will just a screenshot of the current screen. It's gonna be tough.

Worst case: I either implement Diep.io in Python or I go and find an implementation I can run on my computer and whose state I can access programatically.

### References

1. [diepindepth](https://github.com/ABCxFF/diepindepth)
2. [rich library](https://github.com/Textualize/rich)
