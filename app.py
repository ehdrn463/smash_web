import flask
import pickle
import gzip
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


vectorizer=TfidfVectorizer(ngram_range=(1, 3),
    min_df=2,       
    max_features=10000,
    sublinear_tf=True,
    lowercase=False,
    use_idf=True)

# SVM 모델 호출
svm_model = joblib.load('model/svm_model.pkl')


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
        prediction = svm_model.predict(message_data)
        # 예측 label에 대한 확률
        proba = svm_model.predict_proba(message_data)

        # 일반 혹은 스미싱 문자를 가르킬 확률이 0.8이 높다면
        if (proba[0][0] > 0.8 or proba[0][1] >0.8):
            if (prediction == 1):
                prediction = "스미싱 문자"
                proba = proba[0][1]
            else:
                prediction = "일반 문자"
                proba = proba[0][0]

        # 일반 혹은 스미싱 문자를 가르킬 확률이 0.8보다 낮다면
        else:
            lgbm_model = joblib.load('model/lgbm_model.pkl')
            proba2 = lgbm_model.predict_proba(message_data)
            smishing_prbo = (proba[0][1] + proba2[0][1])/2

            if (smishing_prbo > 0.5):
                prediction = "스미싱 문자"
                proba = smishing_prbo
            else:
                prediction = "일반 문자"
                proba = 1 - smishing_prbo


        return flask.render_template('main.html',
                                     original_input={'확인할 문자 메세지 내용':message,
                                                    '확률':proba,
                                                    },
                                     
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


# svm_model = joblib.load('svm_model/svm_svm_model.pkl')


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
#         prediction = svm_model.predict_proba(message)

#         return flask.render_template('main.html',
#                                      original_input={'Message':message},
#                                      result=prediction,
#                                      )

# if __name__ == '__main__':
#     app.run()