#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Return a dictionary, where each key is a region and each value is a list of all average 
    avocado prices between 2015 - 2018 
    """
    
    file=open(csv_filename, 'r')
    temp=[]
    
 
    file.readline()
    regions=[]
    for line in file:
        row=line.split(",")
        fixed_row = []
        fixed_row.append(float(row[2].strip('\'')))
        fixed_row.append(row[13].strip('\n'))
        
        if fixed_row[1] not in regions:
            regions.append(fixed_row[1])

        temp.append(fixed_row)
  
    data = dict.fromkeys(regions, [])

    for line in temp:
        data[line[1]].append(line[0])
   
    return data
    
    """

    return(np.genfromtxt(csv_filename, delimiter=';', skip_header=1)[:,0:11])
    """
   
    
def split_data(dataset, ratio):

    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training.  
    """

    train = dict.fromkeys(dataset.keys(), [])
    test = dict.fromkeys(dataset.keys(), [])

    for region in dataset.keys():
        trainingCount = (int(len(dataset[region])*ratio))
        train[region] = dataset[region][0:trainingCount]
        test[region] = dataset[region][trainingCount::]

    trainingCount=(int(len(dataset)*ratio))
    return(train,test)
    
   
    
def compute_centroid(data):
    """
    Returns a numpy of centroids, one for each region
    """
    centroids = dict.fromkeys(data.keys(), 0)
    
    for region in data.keys():
        centroids[region] = sum(data[region])/len(data[region])

    return centroids

    
def experiment(train, test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy.
    """

    centroids=compute_centroid(train) 
    
    predictions=0
    correct_predictions=0
  
    for region in test:
        
        region_correct = len(test[region])

        for sample in test[region]:
            
            minimum = euclidean_distance(centroids[region], sample)
            predictions+=1

            for r in test.keys():
                
                if euclidean_distance(centroids[r], sample) < minimum:
                    region_correct -=1
                    break

        print("Total predictions for ",region, ": "+str(len(test[region])))
        print("Correct predictions for", region,": "+str(region_correct))
        print("Accuracy for ",region,": "+str((region_correct/len(test[region])*100)),"%")
        correct_predictions += region_correct
 
    print("Total predictions: "+str(predictions))
    print("Correct predictions: "+str(correct_predictions ))
    
    return (correct_predictions/predictions)

"""  
Shuffle the two training sets. 
Run n training/testing experiments (by using the experiment function), where n, 
is the size of region with the smallest number of avocado price samples

plot a graph in which the x-axis is the number of training items used and the y-axis is the accuracy.
"""

def learning_curve(train, test):
    """
    Perform a series of experiments to compute and plot a learning curve.
    """

    minimum = len(train['Albany'])

    for region in train:
        np.random.shuffle(train[region])
        if len(train[region]) < minimum:
            minimum = len(train[region])


    accuracies=[]
    
    for i in range (0, minimum):
        temp = dict.fromkeys(train.keys(), [])

        for region in train.keys():
            temp[region] = train[region][:i+1]

        accuracies.append(experiment(temp,test))
      
    plt.xlabel("Number of training items used")
    plt.ylabel("accuracy")
    plt.plot(list(range(1,len(accuracies)+1)),accuracies)
     
"""
Our avocado dataset is comparatively small. To improve veracity
Perform k-fold cross validation on the data, printing accuracy for each
"""
def cross_validation(data, k): 
    
    data_per_partition = dict.fromkeys(data, [])

    for region in data:
        data_per_partition[region] = int(len(data[region])/k)
    
    average_sum=0
    ##average_sum=experiment(ww_data[ww_data_per_partition:],rw_data[rw_data_per_partition], ww_data[0:ww_data_per_partition], rw_data[0:rw_data_per_partition])
    
    for i in range(0,k): 

        test = dict.fromkeys(data, [])
        train = dict.fromkeys(data, [])

        for region in data:
            start = i * data_per_partition[region]
            end = start + data_per_partition[region]
            test[region] = data[region][start:end]

            train[region] = data[region][list(range(0,start))+list(range(end, len(data[region])))]
        
        average_sum+=experiment(train, test)
    
    return(average_sum/k)


    
if __name__ == "__main__":
    
    data = load_data('avocado.csv')

    #splitting the data
    train, test = split_data(data, 0.9)
    experiment(train, test)
    
    learning_curve(train, test)
    
    k = 5
    acc = cross_validation(data, k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
    
