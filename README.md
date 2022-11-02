# Flappy-Birds-AI

![Flappy Birds](resouce/image/flappy_birds_demo.gif)




# Objectives 
1. **Evolutionary algorithms**. [wiki](https://en.wikipedia.org/wiki/Evolutionary_algorithm). The heart of our game involves: selection, mutation and reproduction with repsect to current flappy-birds generation, that in order to create a 'wiser generation' of birds who wisely navigate themeselves through the pillars without any human assistance. 
2. **Study Neural Networks**. [wiki](https://en.wikipedia.org/wiki/Artificial_neural_network). Each bird at each generation has its own 'brain' which is basically a neuaral-network. Our current architecture is (4:4:1) which basically means 4 inputs, 1 hidden-layer of four neurons and 1 output. 

# Motivations for (4:4:1) architecture 
* *Input*: Any bird doesn't need to know more than its own (x,y) cooridantes plus the (x,y) coordinates of the forthcoming pillar (2+2=4). 
* *Output*: Since the only option a bird has is to either jump or not, the choice of 1 neuron at the output layer is enough. Of cuorse a threshold used for this purpse in a way that whenever exceeded the bird jump. 
* *Hidden layers*: The choice of 1 layer of 4 neurons was arbitrary as first though worked well in the context of our training. Of coures other options such as more than one hidden-layer with different number of neurons might work as well.

# Future work 
It's in our intention to further develop this AI flappy bird game. Our next step is to add some sort of a feature to measure the rate of convergence regarding our birds behaviour, and then to optimize it by choosing different architectures and different mutation STDs. 
