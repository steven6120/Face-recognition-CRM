# Face-recognition-CRM <br />人臉辨識CRM銷售系統

## 簡介
此專案為我在大學實習的時候，所製作的人臉辨識CRM銷售系統，此系統是用作一般銷售店舖，當顧客結帳的時候，透過視訊鏡頭擷取畫面，並結合人臉辨識與後端資料庫系統中，找到客人是屬於新客戶或舊客戶。

如果是舊客戶的話，可以在資料庫中找出該客戶之前在店舖裏購買了什麼東西，並且透過演算法，迅速找出客戶可能有興趣或需要什麼東西；而新客戶的話，會進行手機註冊會員流程。

開發該系統是採用分組製作，我負責為人臉辨識與接收和顯示資訊的前端部份，而另外一組的工作為製作資料庫和管理系統的後端部份。

程式是使用python語言來編寫，採用了dlib套件來研究和製作辨識部份，而顯示部份是採用OpenCV來製作。
## 使用工具
1. Visual Studio Code
1. Anaconda
1. Python 3.7
1. dlib
1. OpenCV
1. Macbook pro

## 程式流程圖
![This is a alt text.](https://lh3.googleusercontent.com/MUR0nzwUkpUHUMhhxGIoCvnq4Kt0T8EVavzVtH4pT3-jBdY7ptM72toTwm-h6eVERsPuhY3q1smazzSyLZmfeVijStO6CnrwFkGLN4Cgv00za5kZ2i1BbTvqPSfPpjMRMlhN-X13ZYoihCFiiV9vLk1Z4CRN-PXmlRN9VBSWwRysQXVBfVVb8usY8fa584x6CGJMneVWZht1ObFLwVyJVURlMdSyEYGHkDhcHN0mG1KC69dATxBvHP36OJvhyMyoCB4QOkyg3OS4o8ETbhkFvwF_0uEjQnTxkr94CBu7_p_Zjn_Ii5yQsh_ecU3pkll7ooK4sP59AR2h39yu_tqgZGJhm7so0WG7b7zvB5Yz4V6h3BS5pi1TEvxCOH2bZr4jgPG6yvI5WWqbgEfl7YlxewSVyqn2AWP1xXmtQBt9KRMW4Hx3LrBgjbVWAizeAIUTh8k3ZqvwtheggtrHBqaSpOtMn-XHrh3MvHCG1z7pEHpHey5DP2bfqXPtKBzCpqHi7VS-lCE0vo-5A_no4En1bh1Sw3uxznlyaqrKIBMOqYI7O9Gw2Th76-1hmImBOJ2D1DIF3IqGEPZfyWDhi03JaKds8pxqrWpnePaNa-ZG_cbyy5qYUXRW3HUDUzFKs9vpx_wQcqglLqRdQwfOQ58GgJFPQ7QCWxUyxsjdM8uIEOnFqlmRxgsJZhSGD_KwfsE9O2Qs1S45PvyW0f7R0dXb1DgHMA=w447-h899-no?authuser=2)
## 程式使用流程
當程式啟動後，系統會開啟連接電腦的視像鏡頭，並且開始進行辨識畫面上是否出現人臉。
<img width="600" alt="鎴湒 2020-06-10 涓嬪崍4 42 39" src="https://user-images.githubusercontent.com/67748642/131550009-edb80f82-50b5-459b-bcab-4bb469c09247.png">

當系統辨識到人臉，就會去取得後端資料進行對比，判別該名使用者是否為新的使用者或已經註冊的會員。
https://github.com/steven6120/Face-recognition-CRM/blob/ea077be6852723bfdbb17aaa9b67102b1406afa3/webcam20200530.py#L83-L101
![image](https://user-images.githubusercontent.com/67748642/131553213-1427ac1c-38d4-44de-a433-e6f3e1d73484.png)


假如是新的客戶，系統會產生唯一碼作為使用者ID，顯示在畫面上。在系統的設計中，此時店員會與客戶說，只需要電話號碼就可以加入會員，詢問有沒有興趣，如客戶有興趣，在取得電話號碼和在CRM上輸入後，客戶可以在手機上收到店舖的註冊會員信息，填寫名字和生日資料來加入會員。
<img width="600" alt="鎴湒 2020-06-11 涓嬪崍5 50 52" src="https://user-images.githubusercontent.com/67748642/131553269-711f2aa0-68a2-4a7c-ae93-1dcfa5fa733e.png">


假如是舊的用戶，系統的畫面上會顯示該名客戶在註冊時的姓名，或沒註冊時會顯示唯一碼。同時會顯示上一次的購物紀錄，並且顯示客戶可能會有興趣的商品。
![image](https://user-images.githubusercontent.com/67748642/131551819-4c7f263a-cca1-4661-80e6-18adb460ca9e.png)
## 程式圖片


