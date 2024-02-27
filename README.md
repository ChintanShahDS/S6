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
