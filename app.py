import flask
import pickle
import pandas as pd

from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from scipy import sparse
import joblib

from flask import Flask, jsonify, request
import os

#####################################################
############# INPUT DATA 전처리 ######################
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

######################################################
############ Interpretable Machine Learning ##########
# from lime import lime_text
# from lime.lime_text import LimeTextExplainer
# from sklearn.pipeline import make_pipeline
# import streamlit as st



vectorizer=TfidfVectorizer(ngram_range=(1, 3),
    min_df=2,       
    max_features=10000,
    sublinear_tf=True,
    lowercase=False,
    use_idf=True)

# SVM 모델 호출
model = joblib.load('model/svm_model.pkl')


app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just redner the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input (원본 메시지)
        message = flask.request.form['message']
        # ================== 예측 모델 ======================
        # loaded_vectorizer: vectorizer 모델 호출
        loaded_vectorizer = pickle.load(open('model/test_vec.pickle', 'rb'))
        
        # INPUT DATA를 loaded_vectorizer로 변환시켜줌
        message_data = loaded_vectorizer.transform([message])
        
        # 예측 label
        prediction = model.predict(message_data)
        # 예측 label에 대한 확률
        proba = model.predict_proba(message_data)

        if (prediction == 1):
            prediction = "스미싱 문자"
            proba = proba[0][1]
        else:
            prediction = "일반 문자"
            proba = proba[0][0]

        # ================ Interpretable Machine Learing ===============
        # class_names = ['normal', 'smishing']
        # explainer = LimeTextExplainer(class_names=class_names)
        # classifier = make_pipeline(loaded_vectorizer, model)
        # explanation = explainer.explain_instance(message, classifier.predict_proba, num_features=6)
       
        return flask.render_template('main.html',
                                     original_input={'확인할 문자 메세지 내용':message,
                                                    '확률':proba,
                                                    
                                                    # '판단 근거2': lime_html 
                                                    },
                                                    # explanation.show_in_notebook(text=True)
                                     
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()














# input data 변환 전
# import flask
# import pickle


# from sklearn.svm import LinearSVC
# from sklearn.calibration import CalibratedClassifierCV
# import joblib


# from flask import Flask, jsonify, request
# import os


# model = joblib.load('model/svm_model.pkl')


# app = flask.Flask(__name__, template_folder='templates')

# @app.route('/', methods=['GET', 'POST'])
# def main():
#     if flask.request.method == 'GET':
#         # Just redner the initial form, to get input
#         return(flask.render_template('main.html'))
    
#     if flask.request.method == 'POST':
#         # Extract the input
#         message = flask.request.form['message']
#         # 벡터화하는 것 추가해야 함.
#         prediction = model.predict_proba(message)

#         return flask.render_template('main.html',
#                                      original_input={'Message':message},
#                                      result=prediction,
#                                      )

# if __name__ == '__main__':
#     app.run()