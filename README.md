# Carrot

The goal of this project is to implement a neural network that can play Diep.io. It will be trained using reinforcement learning. Those are the only requirements. 

I think it's very likely I will have several convolution layers in the neural network. I'm not sure how accurately we are going to be able to reward the network. Diep.io's score is not an element in the DOM as far as I know. Rather, it's a font drawn to the screen with the Canvas API or whatever graphics API they are using to draw their game. Right now I expect that score will be the only plausible rewardable action. Destroying polygons and other tanks will be incredibly hard to detect because I think my input will just a screenshot of the current screen. It's gonna be tough.

Worst case: I either implement Diep.io in Python or I go and find an implementation I can run on my computer and whose state I can access programatically.

### References

1. [diepindepth](https://github.com/ABCxFF/diepindepth)
2. [rich library](https://github.com/Textualize/rich)

### Prompts

## Score Retrieval

In this file, my goal is to write some code that pulls the value of some variable which is a score in a game. The game runs in a browser. It is a WASM game. I also don't really think the score is an HTML element, so I don't think it can be read that way. I think I'll have to read memory addresses, but I have no clue how to do that. I want your help investigating this. Guide me step by step on how to find the address and then how to read it with code. I can manipulate the value of this variable and so maybe I can change it to some value that's recognizable and then look for that value in memory? That's my best lead right now but I don't really even know how to go further.