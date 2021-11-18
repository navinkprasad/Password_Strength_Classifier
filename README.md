# Password Strength Classifier
![image](https://user-images.githubusercontent.com/89060452/142377380-f48f086d-1407-42c9-b4ba-36713a40e8f3.png)

kaggle : https://www.kaggle.com/bhavikbb/password-strength-classifier-dataset

Description:

The passwords used in our analysis are from 000webhost leak that is available online. How did we figure out which passwords were stronger and which were weaker? Well, there is a tool called PARS by Georgia Tech university which have all the commercial password meters integrated into it. All I did was give that tool all the passwords and it gave me new files for each commercial password strength meter. The files contained the passwords with one more column i.e their strength based on the commercial password strength meters.
The commercial password strength algorithms I used are of Twitter, Microsoft and battle. How is this algorithm different from these strength meters? First of all, it is entirely based on machine learning rather than on rules. Secondly, I only kept those passwords that were flagged weak, medium and strong by all three strength meters. This means that all the passwords were indeed either weak, medium or strong.

**accuracy achieved 0.9808255181888776** 


I have build the app using streamlit and deployed on streamlit cloud. You can check it at

https://share.streamlit.io/navinkprasad/password_strength_classifier/main/app.py

![image](https://user-images.githubusercontent.com/89060452/142406164-bde5f3be-9b43-4a92-b210-0cd2b03e1431.png)

