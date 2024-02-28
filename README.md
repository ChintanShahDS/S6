# S6
ERA V2 - Session 6

## Part 1 - Backpropogation Excel Sheet for manual working and understanding of the same

<details>
<summary> Excel sheet Network image: This shows the Neural Network that we are using for backpropogation manual calculation </summary>
  <img width="600px" src="https://github.com/ChintanShahDS/S6/assets/94432132/a99b04f6-5c7c-4e13-8744-fba5d0d0c5ff" alt="Neural Network" />
</details>
<details>
<summary> Table formulas: This shows the formulas for forward propogation for prediction of the network</summary>
  <img width="600px" src="https://github.com/ChintanShahDS/S6/assets/94432132/7c68b319-3791-4a54-a9df-ffc3cad385d3" alt="Forward pass formulas" />
</details>
<details>
<summary> Partial derivatives: This shows the partial derivative formulas for the Error (loss) for each of the weights that will be used for calculation of the backward propogation loss </summary>
  <img width="600px" src="https://github.com/ChintanShahDS/S6/assets/94432132/9542aed7-7d4a-422f-acb1-ddc5ab46892d" alt="Partial derivatives for Back propogation" />
</details>
<details>
<summary> Table with calculations: The formulas are used in this table for backward propogation calculation using the formulas </summary>
<b>Learning rate is also a parameter used in this calculations to understand the impact of the same.</b>
  <img width="600px" src="https://github.com/ChintanShahDS/S6/assets/94432132/7989ac2b-4cd6-4b00-8aeb-a948cfc60c84" alt="Table with Back propogation calculations" />
</details>
<details>
<summary> Table for showing the images of loss or error reduction using backward propogation based on different learning rates </summary>
  
| Learning Rate | Image         |
|---------------|---------------|
| 0.1 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/7a707a39-6894-4ab9-a6c9-41460ea6e685) |
| 0.2 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/b9f245c1-0797-4d6d-9bb4-4d5866c88f6a) |
| 0.5 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/5a05ed4e-7d75-411a-8c1d-956ae7b51089) |
| 0.8 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/a1142475-a964-4b13-9974-a34ffe2366bc) |
| 1.0 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/02d3e04c-46a9-45a7-9e96-f8e1ea0f81d0) |
| 2.0 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/3444b1fe-7e30-4307-bdde-83b43defd257) |

</details>

## Part 2 - Neural Network with 20 k or less params and accuracy of 99.4% or more

## Code files
- 3 main files
    - model.py: *This file holds the model related details*
    - utils.py: *This file holds the utility functions that might be commonly required*
    - S6.ipynb: *Main Notebook file that has the variables, configuration parameters and actual calls

### S6.ipynb
- This is the main notebook file that is used for training the model and checking the outputs
- It also displays the Accuracy and loss curves for training and test across the epochs
- It utilizes the model.py and utils.py as mentioned below for doing the work
- You can run this file directly in Colab using Run all
- ***Recommended to use a GPU for running this file***
- ***2024-02: No need to install anything as per the current Colab verion***

### model.py
- Contains the Model definition
- Created a new model Net6 that is used this time to achieve the required results

### utils.py
- Planned to put utils like common functions to be used
- Contains the train and test functions and GetCorrectPredCount and drawLossAccuracyPlots
- train
    - Model training method to do forward and backward pass
    - Also to calculate the accuracy
    - Return the loss and accuracy
- test
    - Model validation method to do inference
    - Also to calculate the accuracy
    - Return the loss and accuracy
- GetCorrectPredCount: Gives the count of correct preditions
- drawLossAccuracyPlots: Draws the curves for training and test accuracy and losses

#### Model definition
| Layer (type) | Output Shape | Param # |
|-------|----------|---------------|
|       Conv2d-1 |  [-1, 4, 26, 26] |     40 |
|  BatchNorm2d-2 |  [-1, 4, 26, 26] |      8 |
|       Conv2d-3 |  [-1, 8, 24, 24] |    296 |
|  BatchNorm2d-4 |  [-1, 8, 24, 24] |     16 |
|    MaxPool2d-5 |  [-1, 8, 12, 12] |      0 |
|       Conv2d-6 | [-1, 24, 10, 10] |  1,752 |
|  BatchNorm2d-7 | [-1, 24, 10, 10] |     48 |
|      Dropout-8 | [-1, 24, 10, 10] |      0 |
|       Conv2d-9 |   [-1, 48, 8, 8] | 10,416 |
| BatchNorm2d-10 |   [-1, 48, 8, 8] |     96 |
|   MaxPool2d-11 |   [-1, 48, 4, 4] |      0 |
|      Conv2d-12 |   [-1, 10, 2, 2] |  4,330 |
| BatchNorm2d-13 |   [-1, 10, 2, 2] |     20 |
|     Dropout-14 |   [-1, 10, 2, 2] |      0 |
|   AvgPool2d-15 |   [-1, 10, 1, 1] |      0 |
<details>
<summary>Params</summary>
  
  - Total params: 17,022
  - Trainable params: 17,022
  - Non-trainable params: 0
</details>

<details>
<summary>Size</summary>
  
  - Input size (MB): 0.00
  - Forward/backward pass size (MB): 0.23
  - Params size (MB): 0.06
  - Estimated Total Size (MB): 0.30
</details>

Any forms of contribution and suggestion are very welcomed!

# News🔥

2024/02/28 - Details of the final NN that helped achieve the accuracy with the number of params
- Total params: 17,022
- Accuracy achieved: 99.40%
- Epochs: 20
    ```
      Epoch 20
      Train: Loss=0.2251 Batch_id=117 Accuracy=97.75: 100%|██████████| 118/118 [00:40<00:00,  2.95it/s]
      Test set: Average loss: 0.0214, Accuracy: 9940/10000 (99.40%)
    ```
- Applied the following transforms to the training data
  - transforms.RandomApply([transforms.CenterCrop(22), ], p=0.1),
  - transforms.Resize((28, 28)),
  - transforms.RandomRotation((-20., 20.), fill=0),
  - transforms.ColorJitter(brightness=0.05, contrast=0.05, saturation=0.05, hue=0.05),
  - transforms.RandomAffine(5),
- Model design that helped achieve this
  - Used 4 convolution layers with 4, 8, 24 and 48 output channels
  - Used 5th Convolution layer with 10 output channels instead of a FC layer
  - Used BatchNorm after each Convolutional layer
  - Used Maxpool in 2nd and 4th layers only
  - Used Dropout in 3rd and 5th layers only
  - Used AveragePool2D (GAP) as the last layer followed by flatten and softmax
- Used the following training and testing batch sizes for faster testing cycle and better training convergence
  - train_batch_size = 512
  - test_batch_size = 2048

<details>
  <summary> More update logs. </summary>
  
  - 2024/02/26 - Multiple trials on Colab to achieve the desired results
  - 2024/02/27 - Achieved the required results and uploaded the files
  - 2024/02/28 - Updated README.md with required details
</details>

# Features

***Tried various options as listed below (Excel of the different trials uploaded - Did not record first few trials***
- Having different number of Convolutional layers - 4 to 5 layers - 5th layer being replacement of fully connected layer to map to number of outputs
- Maxpool trials or having at each or couple conv layers
- Dropout at different layers
- Added Fully connected layer at end
- Changed number of output channels to Convolutional layers to check accuracy and number of params
- Change in learning rate and momentum
- Changes in transformations to the input data during training
- Next steps
    1) Calculate Receptive field
    2) 1x1 Convolution try
    3) Check Transition layer
    4) Remove Dropout to check
    5) Image Normalization check
