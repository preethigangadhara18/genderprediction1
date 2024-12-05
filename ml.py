import pickle
import os

with open('model.pkl','rb') as f:
    model=pickle.load(f)  
sample_data =[[1,2,3]]
predictions=model.predict(sample_data)[0]
print('predictions:',predictions)

if predictions ==0:
    print('female')
elif predictions ==1:
    print('male')


    
