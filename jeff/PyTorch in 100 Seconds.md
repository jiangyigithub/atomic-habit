PyTorch an open source deep learning framework used to build some of the world's most famous artificial intelligence products.

It was created at The Meta AI research lab in 2016 but is actually derived from the LUA based torch library that dates back to 2002.

Fundamentally it's a library for programming with tensors 

which are basically just multi-dimensional arrays that represent data and parameters in deep neural networks .
 
Sounds complicated but its focused on usability will have you training machine learning models with just a few lines of python.

In addition it facilitates high performance parallel computing on a GPU

thanks to nvidia's CUDA platform.

Developers love prototyping with it 

because it supports a dynamic computational graph allowing models to be optimized at runtime.

It does this by constructing a directed acyclic graph consisting of functions that keeps track of all the executed operations on the tensors

allowing you to change the shape size and operations after every iteration if needed.




PyTorch has been used to train models for computer vision AI like Tesla autopilot, image generators like stable diffusion and speech recognition models like OpenAI whisper.

just to name a few .

to get started install PyTorch and optionally Cuda 

if you want to accelerate Computing on your GPU .

now import it into a python file or notebook.

like I mentioned a tensor is similar to a multi-dimensional array 

create a 2d array or Matrix with python 

then use torch to convert it into a tensor 

now we can run all kinds of computations on it 

like we might convert all these integers into random floating points 

we can also perform linear algebra by taking multiple tensors and multiplying them together 

what you came here to do though is build a deep neural network 

like an image classifier 

to handle that 

we can define a new class that inherits from the neural network module class 

inside the Constructor we can build it out layer by layer 

the flattened layer will take a multi-dimensional input 

like an image and convert it to one dimension 

from there sequential is used to create a container of layers that the data will flow through

each layer has multiple nodes where each node is like its own mini statistical model 

as each data point flows through it 

it'll try to guess the output and gradually update a mapping of weights to determine in the importance of a given variable 

linear is a fully connected layer that takes the flat and 28 by 28 image 

and transforms it to an output of 512.

this layer is followed by a non-linear activation function 

when activated it means that feature might be important and outputs the node 

otherwise it just outputs zero.

and finally we finish with a fully connected layer that outputs the 10 labels the model is trying to predict 

with these pieces in place 

that next step is to define a forward method that describes the flow of data 

and now instantiate the model to a GPU and pass it some input data 

this will automatically call its forward method for training and prediction.

congratulations you just built a neural network 

this has been PyTorch in 100 seconds 

thanks for watching and I will see you in the next one