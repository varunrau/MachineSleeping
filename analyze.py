import csv
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from datetime import datetime
from features import *

class SleepCruncher(object):

    def main(self):
        prior_data, classifications = self.getData()
        print prior_data
        naive_bayes = MultinomialNB()
        naive_bayes.fit(prior_data, classifications)
        import ipdb; ipdb.set_trace() # BREAKPOINT

    def getData(self):
        titles = []
        stack = None
        features = []
        classifications = []
        with open("sleepdata.csv", "rb") as csvfile:
            sleepreader = csv.reader(csvfile, delimiter=";")
            header = True
            for row in sleepreader:
                if header:
                    header = False
                    titles = row
                    continue
                arr = self.createFeatureArray(row)
                #x = np.array(arr)
                features.append(arr)
                classifications.append(row[-2])
        stack = np.array(features)
        classes = np.array(classifications)
        return stack, classes


    def createFeatureArray(self, row):
        start_time = row[0]
        end_time = row[1]
        start_date, end_date, seconds = getTime(start_time, end_time)
        modNinety = ninetyMinuteCycle(seconds)
        return [seconds, modNinety]

if __name__ == "__main__":
    SleepCruncher().main()

