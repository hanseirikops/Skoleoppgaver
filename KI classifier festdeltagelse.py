import pandas as pd
import numpy as np
import sklearn
import sklearn.linear_model
import sklearn.model_selection
import sklearn.neighbors
import sklearn.preprocessing
import sklearn.tree
import sklearn.metrics

data=pd.read_csv('c:/Users/hanse/OneDrive/ITØK/INFO 180/Oblig 2/party_data.csv')

dummy_data=pd.get_dummies(data)

encoder=sklearn.preprocessing.OrdinalEncoder()

train, test=sklearn.model_selection.train_test_split(encoder.fit_transform(dummy_data), test_size=0.2, train_size=0.8)

test_answers=[]
for i in test:
    test_answers.append([i[-2],i[-1]])

remove_answers=[-2],[-1]

new_test = np.array([np.delete(sub_array, remove_answers) for sub_array in test])

train_answers=[]
for i in train:
    train_answers.append([i[-2],i[-1]])

new_train = np.array([np.delete(sub_array, remove_answers) for sub_array in train])

def k_naboersjekk(antall_k=5):
    k_naboer=sklearn.neighbors.KNeighborsClassifier(n_neighbors=antall_k)

    k_naboer.fit(new_train,train_answers)

    guesses=(k_naboer.predict(new_test))

    guesscheck=[]
    for i in guesses:
        guesscheck.append(i[0])
    
    for selected in guesscheck:
        if selected==0:
            print('ok')

    test_answerscheck=[]
    for i in test_answers:
        test_answerscheck.append(i[0])

    correct=0
    total=0
    party_pooper=0

    for i in range(len(guesscheck)):
        total+=1
        if guesscheck[i]==test_answerscheck[i]:
            correct+=1
        if guesscheck[i]!=test_answerscheck[i]:
            if guesscheck[i]==1:
                party_pooper+=1

    print('accuracy is', correct/total, 'for k=', antall_k)
    print('k nærmeste naboer med', (antall_k), 'k sendte', (party_pooper), 'dårlige feståere')
    print(sklearn.metrics.confusion_matrix(test_answerscheck,guesscheck))


k_naboersjekk(3)
k_naboersjekk(5)
k_naboersjekk(11)
k_naboersjekk(17)

def avgjøringstre(kriterie='gini'):
    three=sklearn.tree.DecisionTreeClassifier(criterion=kriterie)

    three.fit(new_train,train_answers)

    guesses=(three.predict(new_test))

    guesscheck=[]
    for i in guesses:
        guesscheck.append(i[0])

    for selected in guesscheck:
        if selected==0:
            print('ok')

    test_answerscheck=[]
    for i in test_answers:
        test_answerscheck.append(i[0])

    correct=0
    total=0
    party_pooper=0

    for i in range(len(guesscheck)):
        total+=1
        if guesscheck[i]==test_answerscheck[i]:
            correct+=1
        if guesscheck[i]!=test_answerscheck[i]:
            if guesscheck[i]==1:
                party_pooper+=1

    print('accuracy is', correct/total, 'for', kriterie)
    print('valgtre med', (kriterie), 'sendte', (party_pooper), 'dårlige feståere')
    print(sklearn.metrics.confusion_matrix(test_answerscheck,guesscheck))



avgjøringstre('gini')
avgjøringstre('entropy')

dummy_data_log=pd.get_dummies(data,drop_first=True)

train_log, test_log=sklearn.model_selection.train_test_split(encoder.fit_transform(dummy_data_log), test_size=0.2, train_size=0.8)

test_answers_log=[]
for i in test_log:
    test_answers_log.append([i[-1]])

train_answers_log=[]
for i in train_log:
    train_answers_log.append(i[-1])

new_test_log = np.array([np.delete(sub_array, [-1]) for sub_array in test_log])
new_train_log = np.array([np.delete(sub_array, [-1]) for sub_array in train_log])

def logiskregresjon(penalty='l2'):
    logic=sklearn.linear_model.LogisticRegression(penalty=penalty)

    logic.fit(new_train_log,train_answers_log)
    guesses=logic.predict(new_test_log)

    '''for guess in guesses:
        if guess==1:
            print('ok')'''

    total=0
    correct=0
    party_pooper=0

    for i in range(len(guesses)):
        if guesses[i]==test_answers_log[i]:
            correct+=1
        total+=1
        if guesses[i]!=test_answers_log[i]:
            if guesses[i]:
                party_pooper+=1
    print('accuracy is', correct/total, 'for logisk regresjon med penalty', (penalty))
    print('Logisk regresjon med penalty', (penalty), 'sendte', (party_pooper), 'dårlige feståere')
    print(sklearn.metrics.confusion_matrix(test_answers_log,guesses))

    
logiskregresjon('l2')
logiskregresjon(None)