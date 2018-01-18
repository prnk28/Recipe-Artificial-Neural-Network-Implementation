# Recipe-Artificial-Neural-Network-Implementation

I tried to compare simple regression and artificial neural network (ANN), but found that the ANN would be the ideal algorithm to utilize with the given problem. I wanted to use the ANN because deep learning is the most budding concentration of machine learning. First I imported the data set from JSON, and split it into two different arrays with the dependent variable being cuisine and the independent variable being ingredients. After that I split the data frame to create individual columns for each ingredient. In order to encode the categorical data, the strings were converted into floats. The data set was then split into a Training set and a Testing set. Next, I had to make the ANN. After importing the necessary libraries and packages, the ANN was initialized. Then I added the input layer and the first hidden layer. Afterwards, I added the second and hidden layer, and finally, the output layer. Once this was complete, I compiled the ANN. The ANN was then fit to the Training set. Finally, I made predictions by predicting the Test set results and made the confusion matrix in order to evaluate the model.

## 6-Fold Cross Validation:

| Fold        | Generalization Error (25 Epochs) |
| ------------- |:-------------:|
|   0   | 0.4863 |
|   1   | 0.4912 |
|   2   | 0.4906 |
|   3   | 0.4926 |
|   4   | 0.4842 |
|   5   | 0.4931 |

|         | Generalization Error (25 Epochs) |
| ------------- |:-------------:|
| AVERAGE | 0.4897 |
	
## Conclusion:	

Using the 6-fold cross validation, I obtained 6 different values for generalization error depending on which of the 6 sets was used as the training set. The maximum generalization error was 0.4931 (49.31%) while the minimum generalization error was 0.4842 (48.42%). The average generalization error was 0.4897 (48.97%). For the 6-fold cross validation, 25 epochs were used since more epochs resulted in only little variation. Using our machine, the time to compute was <5 minutes (for 25 epochs). The machine utilized a Quad Core 2.6 GHz i7 processor with 16 GB RAM. The GPU was Radeon pro 450 2GB.
