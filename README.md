# Food demand forecasting and Inventory management system

*Problem statement:*

 - A food delivery company has to deal with a lot of perishable raw materials. Thus it is very important for such a company to accurately forecast daily and weekly demand.

 - Too much inventory in the warehouse means more risk of wastage, and not enough could lead to out-of-stocks  problems and push customers to seek solutions from your competitors.

*Solution:*

 - We created website using an appropriate machine learning model, to forecast number of orders to gather raw materials for next few weeks.

 - For this, a dataset having information about fulfilment center like city, area etc. and meal information like category, sub category, etc. is used.

 - We have used Gradient boost regression model for forecasting with training accuracy 92% and testing accuracy 83%.

 - The prediction model is a generalized model which means other companies or services can rebuild this model according to their data and no one can use this model for their specific prediction as this is just a generalized model for research.

 - In the web application, a separate section called ‘inventory management’ for Restaurant owners is created, where they can log in/sign up and  can keep record of available inventory and also manage their customers and orders.






## Demo of project and it's explanation

 - Youtube video: https://youtu.be/45kdILuQyTs


## Notebook of ML model

 - Food demand forecasting:https://colab.research.google.com/drive/1-IlwSyDkheIBuSZuY2EgYnS4EqRiZ9kQ?usp=sharing


## Contributor
 - Darshan Bhavsar : https://www.linkedin.com/in/darshan-bhavsar-93370721a/
 
 - Jigar Parmar : https://www.linkedin.com/in/jigar-parmar-b507a3229/
 
 - Nirmal Trivedi : https://www.linkedin.com/in/nirmal-trivedi-80929a23b/
 
## Tech Stack

*Frontend:* HTML, CSS, Javascript, Bootstrap

*Backend:* Python framework Django, SQLite

*ML model:* Gradient boost regression model





## How to setup this project on your local machine

 1. Clone This Project `git clone https://github.com/nirmaltrivedi/Foodiepy.git`
 2. Go to Project Directory
 3. Create a Virtual Environment `python3 -m venv env`
 4. Activate Virtual Environment `env/Scripts/activate`
 5. Install Requirements Package `pip install -r requirements.txt`
 6. Migrate Database `python manage.py migrate`
 7. Create Super User `python manage.py createsuperuser`
 8. Finally Run The Project `python manage.py runserver`
