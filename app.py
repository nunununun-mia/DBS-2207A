#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template


# In[ ]:


import joblib


# In[ ]:


app = Flask(__name__)


# In[ ]:


@app.route("/", methods = {"GET", "POST"})
def index():
    if request.method =="POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = "OK", result2 = "OK"))
    else:
        return(render_template("index.html", result1 = "WAITING", result2 = "WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




