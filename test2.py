import pandas as pd
import statistics
import csv
df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
#Mean for height and Weight
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
#Median for height and weight
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
#Mode for height and weight
# height_mode = statistics.mode(height_list)
# weight_mode = statistics.mode(weight_list)
#Printing mean, median and mode to validate
print("Mean, Median of height is {}, {} respectively".format(height_mean, height_median))
print("Mean, Median of weight is {}, {} respectively".format(weight_mean, weight_median))

heightSD = statistics.stdev(height_list)
weightSD = statistics.stdev(weight_list)

heightFirstSDStart, heightFirstSDEnd = height_mean-heightSD, height_mean+heightSD
heightSecondSDStart, heightSecondSDEnd = height_mean-(2*heightSD), height_mean+(2*heightSD)
heightThiredSDStart, heightThiredSDEnd = height_mean-(3*heightSD), height_mean+(3*heightSD)

weightFirstSDStart, weightFirstSDEnd = weight_mean-weightSD, weight_mean+weightSD
weightSecondSDStart, weightSecondSDEnd = weight_mean-(2*weightSD), weight_mean+(2*weightSD)
weightThiredSDStart, weightThiredSDEnd = weight_mean-(3*weightSD), weight_mean+(3*weightSD)

heightData1Sd = [result for result in height_list if result > heightFirstSDStart and result < heightFirstSDEnd]
heightData2Sd = [result for result in height_list if result > heightSecondSDStart and result < heightSecondSDEnd]
heightData3Sd = [result for result in height_list if result > heightThiredSDStart and result < heightThiredSDEnd]

weightData1Sd = [result for result in weight_list if result > weightFirstSDStart and result < weightFirstSDEnd]
weightData2Sd = [result for result in height_list if result > weightSecondSDStart and result < weightSecondSDEnd]
weightData3Sd = [result for result in height_list if result > weightThiredSDStart and result < weightThiredSDEnd]

print('{}% of Data of height lies between 1 Sd'.format(len(heightData1Sd)*100/len(height_list)))
print('{}% of Data of height lies between 2 Sd'.format(len(heightData2Sd)*100/len(height_list)))
print('{}% of Data of height lies between 3 Sd'.format(len(heightData3Sd)*100/len(height_list)))

print('{}% of Data of weight lies between 1 Sd'.format(len(weightData1Sd)*100/len(weight_list)))
print('{}% of Data of weight lies between 2 Sd'.format(len(weightData2Sd)*100/len(weight_list)))
print('{}% of Data of weight lies between 3 Sd'.format(len(weightData3Sd)*100/len(weight_list)))