import pickle
#Example data
data={'name':'Samrat','age':21,'is_student':True}
#Serialize to a file 
with open ('data.pkl','wb') as file:
    pickle.dump(data,file)
#Deserialize to a file 
with open ('data.pkl','rb') as file:
    loded_data=pickle.load(file)
print(loded_data)
