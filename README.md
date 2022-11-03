# Flappy-Birds-AI

![Flappy Birds](resource/image/flappy_birds_demo.gif)




# Objectives 
1. Study **Evolutionary algorithms**. [wiki](https://en.wikipedia.org/wiki/Evolutionary_algorithm). The heart of our game involves: selection, mutation and reproduction with repsect to current flappy-birds generation, that in order to create a 'wiser generation' of birds who wisely navigate themeselves through the pillars without any human assistance. 
2. Study  **Neural Networks**. [wiki](https://en.wikipedia.org/wiki/Artificial_neural_network). Each bird at each generation has its own 'brain' which is basically a neuaral-network. Our current architecture is (4:4:1) which basically means 4 inputs, 1 hidden-layer of four neurons and 1 output. 
3. Implement **PyTorch** library in Python. [wiki](https://en.wikipedia.org/wiki/PyTorch). As mentioned, our birds' brain is a neural-network that evolve over time according to their navigations and with respect to evolutionary algorithm. The network infrastructure is implemented by PyTorch.     

# Motivations for (4:4:1) architecture 
* *Input*: Any bird doesn't need to know more than its own (x,y) cooridantes plus the (x,y) coordinates of the forthcoming pillar (2+2=4). 
* *Output*: Since the only option a bird has is to either jump or not, the choice of 1 neuron at the output layer is enough. Of cuorse a threshold used for this purpse in a way that whenever exceeded the bird jump. 
* *Hidden layers*: The choice of 1 layer of 4 neurons was arbitrary as first though worked well in the context of our training. Of coures other options such as more than one hidden-layer with different number of neurons might work as well.

# Remarks
The aim of this project was initially to explore neuro-evolution algrorithm with the emphasize of neural-networks. Therefore as being such I didn't pay attention to game-graphics in advance. Of course it's possible to add more graphics with the aid of *pygame* library in order to beautify the game.   

# Future work 
It's in our intention to further develop this AI flappy birds game. Our next step is to add some sort of features to measure the rate of convergence regarding our birds behaviour, and then to optimize it by choosing different architectures and different mutation STDs. 
