# 경희대학교 2020-1학기 데이터분석캡스톤디자인
## 주제: 스미싱 문자를 판독해주는 챗봇
### 웹사이트: ec2-3-34-36-125.ap-northeast-2.compute.amazonaws.com:5000  
   (챗봇: 라인 Messaging API를 이용한 개발 중) <br>
   (과금문제로 디버깅할 때만 서버돌리고 있음) <br>

### Flow-chart
<img src = https://user-images.githubusercontent.com/41279466/85946418-16a33000-b97f-11ea-9d3e-8bd6fdc90c35.png>

------------
### Classification Analysis 결과

#### 1. LGBM: 정확도: 99.6% 모델링 시간: 45분 
<img src = https://user-images.githubusercontent.com/41279466/85946798-ead57980-b981-11ea-8d63-ad820c1e8817.PNG width = 60%>

#### 2. SVM 정확도: 99.7% 모델링 시간: 2분 
<img src = https://user-images.githubusercontent.com/41279466/85946844-1f493580-b982-11ea-8b03-0fdaf263b0bb.PNG width = 60%>

#### 3. LSTM 정확도: 99.5% 모델링 시간: 12시간
<img src = https://user-images.githubusercontent.com/41279466/85946850-2e2fe800-b982-11ea-961b-df18ea41bf51.PNG width = 60%>

#### 4. Interpretable MachineLearning LIME 적용 결과
<img src = https://user-images.githubusercontent.com/41279466/85946904-8830ad80-b982-11ea-98a9-ad939e16130e.PNG width = 60%>

### 5. SVM + LGBM 모델 적용의 분석 결과
<img src = https://user-images.githubusercontent.com/41279466/85949948-a1daf080-b994-11ea-89b0-a87ffc401984.PNG width = 60%>

<br>


------------
### 핵심 라이브러리

|역 할|이 름|주요 기능|
|:----|:-----:|----:|
|탐색적 데이터 분석|DTM(문서 단어행렬)| 문서의 단순 최다 노출 단어 빈도 분석|
|탐색적 데이터 분석|TF-IDF|문서 내부에서 중복도를 고려한 최다 노출 단어 빈도 분석|
|데이터 전처리|Konlpy - Mecab|한국어 형태소 분석기|
|데이터 전처리|TfIdfVectorizer|Tfidf 결과가 반영된 워드 임베딩 진행|
|데이터 모델링|k-fold cross validation|동일한 데이터셋을 교차검증하는 기법|
|데이터 모델링|Support Vector Machine(SVM)|classification model1|
|데이터 모델링|LightGBM|classification model2|
|데이터 모델링|Long Short Term Memoy model|classifcation model3|
|결과 분석|classifcation reprot|Recall, Precision, F-score 결과분석|
|결과 분석|LIME|classification의 판단 근거를 시각적으로 보여줌|
|웹프로그래밍|Python-Flask|웹프로그래밍 프레임워크|
|웹프로그래밍|AWS-EC2|웹 배포 소프트웨어|
<br>


-----------
### 코드를 통한 진행상황 설명 (세부 내용은 weekly_colab 폴더 참조)

1. 0409_EDA.ipynb<br>
   탐색적 데이터 분석 과정 <br>
   1) Konlpy - Mecab 이용한 형태소 분석 
      colab 내부에서 konlpy 및 mecab 설치 후 Mecab() 라이브러리 이용<br>
      문자메시지 내용을 형태소분석하여 새로운 칼럼을 추가함<br>
   2) TF-IDF 
      각 Label에 대해 TF-IDF 기준 상위 빈출 100개 단어 도출<br>
      분석 결과, 공통적인 단어 31개, 각 label에 대한 단어 69개가 도출됨<br>

2. 0415_Cleansing.ipynb<br>
   전처리하는 과정이 주된 내용임<br>
   1) 알파벳을 소문자로 통일함
   2) 불용어(한글의 형식형태소인 '은/는/이/가'처럼 의미가 없는 단어) 및 1-2)의 결과인 공통적인 빈출단어 제거
   3) 특수문자 제거

3. 0423_Word_Embedding.ipynb<br>
   워드임베딩: 자연어를 컴퓨터가 이해하고, 효율적으로 처리하게 하기 위해서 컴퓨터가 이해할 수 있도록 자연어를 정수로 나타냄<br>
   1) TfIdf를 이용한 정수임베딩 진행
   
4. 0430_LGBM.ipynb<br>
   1) classification 모델로 lgbm을 사용함
   k-fold cross-validation에서 k를 4로, seed를 3번 줌으로써 12번 모델링을 진행함<br>
   -> 12개의 모델의 예측값으로 결과분석함<br>
   2) classification 모델로 svm을 사용함
   세부 내용은 lgbm 방식과 동일함<br>
   
5. 0506_Modeling 검증.ipynb<br>
   seed를 랜덤시드로 30번 반복하여 4번의 LGBM 및 SVM의 분석결과를 재검증함<br>
   
6. 0514_LIME.ipynb<br>
   Interpretable Machine Learning 기법인 LIME 적용<br>
   
7. 0526_FocusingOnFalseDel.ipynb<br>
   LGBM과 SVM의 False record를 비교분석하여 더 정확도, F1-score가 높은 모델 조합을 분석함<br>
   
8. 0603_LSTM_Modeling.ipynb<br>
   LSTM 딥러닝 모델 기법을 적용하여 추가적으로 classification 분석 진행<br>
   
9. 0617_svmNlgbm.ipynb<br>
   SVM과 LGBM을 직렬적으로 조합하여 더 나은 모델 구성<br>
   (메인모델인 SVM의 예측확률이 5:5 ~ 2:8로 확신을 갖지 못할 때 적용)<br>
     

-------------
### 스미싱 문자 데이터 출처
#### 데이콘 금융 문자 분석 경진대회 https://dacon.io/competitions/official/235401/overview/
#### 데이콘, 스폰서의 협의로 인해 대회 종료 후 데이터 다운로드 불가능합니다. 
#### 따라서 repository에서도 제공받은 데이터를 공개하지 않을 것입니다.
<br>

-------------

### 보완점
1. Interpretable MachineLearning 기법인 LIME을 웹프로그래밍에 적용하지 못함<br>
2. Chat-bot 서비스를 하기 위해서는 도메인을 따서 https 주소를 확보해야 함<br>


-------------
### 추진일정 [간략]
|순 번|추진 내용|4월|5월|6월|비고
|:----|:-----:|:-----:|:-----:|:-----:|:-----:|
|1|개발환경 구축(Colab을 이용한 Mecab형태소 분석 패키지 설정)|1주|||완료|
|2|탐색적 데이터 분석(EDA)|2주|||완료|
|3|불용어(비식별화된 정보, 한국어 조사, 공통적으로 많이 쓰인 단어) 제거|3주|||완료|
|4|모델학습을 위해 텍스트 데이터를 시퀀스 데이터로 변환해줌(Keras Tokenizer 이용)|3주|||sklearn Tfidfvectorizer 이용|
|5|층화추출 (class label 94%:6%로 불균형), 변수 선택 |4주|||완료|
|6|LightGBM, SupportVectorMachine 모델 구축 및 검증||1주||완료|
|7|하이퍼 파라미터 선택||1주||완료|
|8|LSTM 모델 구축 및 검증||2주||LGBM, SVM 성능이 우수함 -> 생략|
|9|하이퍼 파라미터 선택||2주||LGBM, SVM 성능이 우수함 -> 생략|
|10|LightGBM과 LSTM 모델 중 정확도, 속도를 고려하여 더 우수한 모델 선택||2주||메인모델: SVM, 보조모델: LGBM|
|11|LIME 학습 및 모델 적용||3주||완료|
|12|카카오톡·라인 플러스 친구, 웹사이트 중 이번 모델에 적합한 플랫폼 선정||4주||카카오톡·라인 모두 고려 중 -> 라인 선정|
|13|8)의 a에 의해 선정된 플랫폼 학습||4주||진행 중|
|14|웹 서비스 개발|||1, 2주|완료|
|15|웹서비스 배포|||2, 3주|완료|
|16|챗봇서비스 개발|3, 4주|진행 중|

-------------


<br>

### 추진일정(안) [상세]
   1) 4월 3일 ~ 4월 9일<br>
   : 개발환경 구축(Colab을 이용한 Mecab 설치) 및 관련 연구 조사, 문자메시지 형태소 분류<br>
 
   2) 4월 10일 ~ 4월 16일<br>
   : 탐색적 데이터 분석(EDA) <br>
     a. Positive, Negative data 비율 확인<br>
     b. Bag of Words를 이용한 DTM 분석, TF-IDF 분석 -> 스미싱, 일반 문자의 내용 분석<br>    

   3) 4월 17일 ~ 4월 23일<br>
    a. 4월 17일 ~ 4월 20일.<br>
    : 불용어(비식별화된 정보, 한국어 조사, 공통적으로 많이 쓰인 단어) 제거<br>
    b. 4월 21일 ~ 4월 23일<br>
    : 모델학습을 위해 텍스트 데이터를 시퀀스 데이터로 변환해줌(Keras Tokenizer 이용)<br>
   
   4) 4월 24일 ~ 4월 30일<br>
     a. 층화추출 (class label 94%:6%로 불균형)<br>
     b. 변수 선택 (ex. 문자 메시지 길이, 형용사, 명사, 동사, 빈도)<br>
       : Accuracy(Information Gain)를 확인하여 모델에 유의미한 영향력을 끼치는 변수 선택<br>

   5) 5월 1일 ~ 5월 7일<br>
     a. LightGBM 모델 구축 및 검증<br>
     b. 하이퍼 파라미터 선택<br>

   6) 5월 8일 ~ 5월 14일<br>
     a. LSTM 모델 구축 및 검증<br>
     b. 하이퍼 파라미터 선택<br>
     c. LightGBM과 LSTM 모델 중 정확도, 속도를 고려하여 더 우수한 모델 선택<br>

   7) 5월 15일 ~ 5월 21일<br>
     a. LIME (Local Interpretable Model-agnostic Explanations) 학습<br>
       (https://christophm.github.io/interpretable-ml-book/)<br>
     b. LIME 듀토리얼 예제<br>
       (https://github.com/marcotcr/lime/tree/ce2db6f20f47c3330beb107bb17fd25840ca4606)<br>
     c. 6)의 c에 의하여 선택된 모델에 LIME 적용<br>

   8) 5월 22일 ~ 5월 28일<br>
     a. 카카오톡·라인 플러스 친구, 웹사이트 중 이번 모델에 적합한 플랫폼 선정<br>
     b. 8)의 a에 의해 선정된 플랫폼 학습<br>

   9) 5월 29일 ~ 6월 4일<br>
     a. 웹 서비스 개발<br>

   10) 6월 5일 ~ 6월 18일<br>
     a. 웹서비스 개발 및 배포<br>
     
----------
### Developers
- 김동구(Kim Dong Gu) ehdrn463@naver.com
