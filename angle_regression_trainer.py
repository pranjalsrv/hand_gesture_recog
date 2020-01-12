from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import statsmodels.api as sm
from unitvec import calc_unit_vector
from  sklearn.svm import SVC
import math

embeddings_angles = pickle.load(open("embeddings/embeddings_and_angles.pkl", 'rb'))

embeddings = []
targets = []
for i in embeddings_angles:
    current_embed = i[0]
    proper_embed = []
    # print(current_embed)
    # unit_v = calc_unit_vector(current_embed)
    # print(current_embed)

    #al = [(-10, -10) if x == (None, None) else x for x in [j for j in [k for k in current_embed]]]
    temp_inn = []
    for j in current_embed:
        temp_in = []
        for k in j:
            if k == (None, None):
                temp_in.append((-10,-10))
            else:
                temp_in.append(k)
        temp_inn.append(temp_in)

    angle_degrees = math.degrees(i[1])
    if angle_degrees < 0:
        angle_degrees = 180 + angle_degrees
    embeddings.append(temp_inn)
    targets.append(int(angle_degrees))

np_embeds = np.array(embeddings)

print("Raw embedding shape = ", np_embeds.shape)
nsamples, nx, ny, each = np_embeds.shape
flattened_embeds = np_embeds.reshape((nsamples, nx * ny * each))
print("Flattened embeddings shape =", flattened_embeds.shape)

x_train, x_test, y_train, y_test = train_test_split(flattened_embeds, targets, shuffle=True, test_size=0.3)
model = SVC()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy = ", acc)
clf_report = classification_report(y_test, y_pred)
print(clf_report)
# model = sm.OLS(x_train, y_train, missing='none')
# results = model.fit()
