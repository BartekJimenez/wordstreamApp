import json
import requests
import itertools
import operator
from collections import Counter



class DataHarvester:
        def __init__(self, dataSource):
                self.dataSource = dataSource
                self.todos = json.loads(response.text)
                self.data = self.todos['data']
                self.amountOfVariables = len(self.data)
                self.diffVariables = self.getAmountOfDifferentVariables(self.data)
                self.glossary = self.createGlossary(self.diffVariables)
                # self.results = self.createMeasurementList()
        def getAmountOfDifferentVariables(self,data):
                val = -1
                tempSet = set()
                for x in data:
                        val = val + 1
                        try: 
                                curr = data[val]['targeting']['geo_locations']
                                for z in curr:
                                        tempSet.add(z)
                        except:
                                pass
                
                return tempSet

        def searchByCritiera(self,data, critiera, max):
            # this might be unused/worth of deletion
                temp = []
                final = []
                multiples = []
                counter = 0
                while counter < max:
                        try: 
                                curr = data[counter]['targeting']['geo_locations'][critiera]
                                if len(curr) > 1:
                                        multiples.append(curr)
                                else:
                                        temp.append(curr)
                        except:
                                pass
                        counter = counter + 1
                #combine both as lists of dictionaries
                for x in temp:
                        for y in x:
                                final.append(y)

                for x in multiples:
                        for y in x:
                                final.append(y)
                #returns a list of dictionaries
                return final

        def createGlossary(self,diffVars):
                tempGlossary = {}
                for x in diffVars:
                        results = self.searchByCritiera(self.data, x ,self.amountOfVariables)
                        tempGlossary[x] = results
                return tempGlossary

        def createMeasurementList(self, dataset='skip', criteria='skip'):
                tempList = []
                if dataset == 'skip' and criteria == 'skip':
                        for x in self.glossary:
                                tempList.append(x)
                elif dataset != 'skip ' and criteria == 'skip':
                        for x in self.glossary[dataset]:
                                tempList.append(x)    
                elif dataset != 'skip' and criteria != 'skip':
                        for x in self.glossary[dataset]:
                                tempList.append(x[criteria])           
                return tempList  
        def returnTopMetric(self,dataset, criteria):
                temp = self.createMeasurementList(dataset,criteria)
                data = Counter(temp)
                return (data.most_common(5))
        def sort(self,unsortedList,criteria=0):
            return sorted(unsortedList, key=lambda k: k[criteria])
            

response = requests.get("https://app.wordstream.com/services/v1/wordstream/interview_data")

# def runner():
#     run = DataHarvester(response)
#     return run.createMeasurementList()
    
# 

# words_to_count = (word for word in results if word[:1].isupper())
# c = Counter(words_to_count)
# print(diffVariables)
# print (c.most_common(5))







