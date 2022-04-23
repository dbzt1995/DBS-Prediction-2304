#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__) #Double underscore = placeholder under __main__


# In[1]:


import joblib

@app.route("/", methods=["GET","POST"]) #@ is to pinpoint the program that they must run this line first
def index():
    if request.method=="POST":
#         rate = float(request.form.get("rate"))
#         print(rate)
        
#         model = joblib.load("DBS_Prediction")
#         pred = model.predict([[rate]])
        
        return(render_template("index.html", result = "unknown"))
    else:
        return(render_template("index.html", result = "waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run() #host, port if cannot run in the environment due to firewall


# In[ ]:




