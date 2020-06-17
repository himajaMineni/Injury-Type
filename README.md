# Injury-Type
Dataset Description:

To apply classification analysis I have selected the Monroe-county-crash-data2003-to-2015 dataset. This dataset contains the data about counters of traffic and the data about accidents in Monroe County in the United States. It contains a total of 12 attributes including the target variable. The total number of rows in this dataset are 53943. The list of columns is, master record number, year, month, day, weekend or not, hour, collision type, Injury type, primary factor, reported location. Form these my feature variables are collision type, weekend, primary factor, and my target variable is injury type.

My target variable is a categorical variable that has four categories namely, fatal, incapacitating, non-injury or unknown, non-incapacitating. My feature variable contains an attribute named primary factor, which has the data of the factors that lead to the injury. The collision type contains the data about the number of vehicles and the type of vehicles that lead to the injury. The weekend attribute contains the data when the accident occurred during a weekend or on weekdays.

Imputing missing values:

There are few missing values in the feature variables like the weekend attribute has 68 missing values, collision type has 6 missing values and the primary factor has 1121 missing values. To impute these missing values I imported the simple imputer from the sklearn and replaced the missing values with a constant value using the imp.fit_transform function from the impute library. Now the data is free from missing values but the next task is to preprocess the data and convert the string into numbers. For this, I imported the preprocessing function from the sklearn library, I created a variable with the name number and stored the label encoder function of preprocessing into that variable. Later I used the number.fit_transform function and called the variable, number.
Later I stored my feature attributes in variable x and target attribute in variable y, and then I split the data into the train set and the test set in the ratio of 70:30. i.e 70 percent of data is for training and the rest is testing data. I had split the data using the train¬_test_split function that I have imported from the sklearn library. 

Decision Tree:

Now I have to give the split data to the model I have selected. The model I selected is the decision tree. The decision tree algorithm is a supervised learning model, i.e we guide the model with corresponding output for a particular input. In this decision tree, the data is split continuously into daughter nodes based on certain parameters or based on certain conditions. The process continues until there are no further entities left to be split. It is explained by two entities the root node and the child node, every decision tree or a binary tree will have only one parent node and many child nodes.

Now to apply this model I imported decision tree classifier from the sklearn model selection library. Then I used the fit function to fit the x_train  and y_trrain, where x contains the values of the feature variables and y contains the values of the target attribute. Later I found the predicted values using the predict function and then found the accuracy of y_test and y_predicted values using the metrics.accuracy_score function to find accuracy. Here, it gave an accuracy of 80 percent.
