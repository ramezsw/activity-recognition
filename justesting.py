import numpy as np
from sklearn import svm, cross_validation
from sklearn.ensemble import RandomForestClassifier


activity_label = {'1': 'WALKING',
                  '2': 'WALKING_UPSTAIRS',
                  '3': 'WALKING_DOWNSTAIRS',
                  '4': 'SITTING',
                  '5': 'STANDING',
                  '6': 'LAYING'}

# ############################# Open data set ###############################
X = []
y = []
X_fin = []
y_fin = []

print("Opening dataset...")
try:
    with open("X_train.txt", 'rU') as f:
        res = list(f)
        for line in res:#each line is one row (can be viewed as 1*561 vector)
            line.strip("\n")
            features = line.split(" ")
            while features.__contains__(""):
                features.remove("")
        #print(len(features)) is 561, applied for each line in the file --> 10000*561 feature matrix!!
            for i in range(len(features)):
                features[i] = float(features[i])
            X.append(features)
         
    #read the classes from file and put them in list.      
    with open("y_train.txt", 'rU') as f:
        res = list(f)
        for line in res:
            y.append(int(line.strip("\n")[0]))
            
except:
    print("Error in reading the train set file.")
    exit()
try:
	#do the same for test sets.
    with open("X_test.txt", 'rU') as f:
        res = list(f)
        for line in res:
            line.strip("\n")
            features = line.split(" ")
            while features.__contains__(""):
                features.remove("")
            for i in range(len(features)):
                features[i] = float(features[i])
            X_fin.append(features)
            #print(len(X_fin))
        
    with open("y_test.txt", 'rU') as f:
        res = list(f)
        for line in res:
            y_fin.append(int(line.strip("\n")[0]))
        f.close()
except:
    print("Error in reading the train set file.")
    exit()
print("Dataset opened.")
count1 = 0
count2=0
for i in range(X_fin.__len__()):
    count2 += 1
    a=X_fin[i]
    #print(a)
    print(X_fin[i])#predict class la kul row.. each i is a row.
    print()
    b = y_fin[i]
    #print("+ ", a[0])
    #print("- ", b)
    if a == [b]:
        count1 += 1

X = np.array(X) #change to matrix
y = np.array(y) #change to matrix (sklearn models only accept matrices)

print(X.shape)
print(y.shape)
y1 = y.reshape(-1,1)
print(y1.shape)
print(y_fin.__len__())

