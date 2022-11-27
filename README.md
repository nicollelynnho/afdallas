Title:
Automating Member Registration in Culturetheque 

Introduction:
When new members subscribe to Alliance Francaise de Dallas, or members renew their subscription, their information needs to be transfered from Arc En Ciel, our CRM software to Culturetheque, a library subscription that comes with the membership. Additionally, their emails need to be added to Constant Contact for email marketing. It was a manual data entry task to view the member data in excel, and create accounts in Culturetheque and Constant Contact. This task took approximately 5 hours weekly. 

Project Description:
The Memberships.py (not included on github for privacy) is a python script that does the following
- Reads a csv from Arc En Ciel to obtain new member data (first name, last name, email, account expiration date)
- Uses post request to determine if a new account needs to be created, or if an existing account needs to be updated.
- Uses a second post request to execute the action in the previous step
- Prints a list of emails that need to be pasted into Constant Contact

Tools & Packages:
- Python
- Pandas
- Requests

Key Accomplishments:
- Decreased processing time for membership data by 95%

Credits
- Nicolle Ho
- Alliance Francaise de Dallas

![image](https://user-images.githubusercontent.com/58828437/169741194-295ccc94-9ccf-4717-8ff6-c3e25c59dfc3.png)
