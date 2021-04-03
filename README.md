# <b>Study app</b>
This is a site where students share their knowledge and a enviornment where they can post ideas, so that their classmates can also learn from it. And this website is hosted on Heroku. <br>
<i><b>

        If you ask me what inspired me then let me tell you, one day i was usually doing my homework and i had a dout and i wanted to clear it, but i didn't knew any one so close in my school and it was also lockdown. I could have use facebook messenger or whatsapp but you know all those unnessesary messages, it is enough for any one to be distracted from there work and more over those fake forwards and useless ads.
    
        I thought of building a website where students can interact with each other without any of those useless ads and those unresistable distractions.

        I then started researching on google how to build a dynamic website using python and i came to this article which was telling about a pyhton module Django. And I started learning Django.

        Initially there were a lot of issues and errors. The first difficulty was the setup of a enviornment, even though I am using parrot os a unix based OS. I resolved it using a pipenv enviornment.
    I installed it using :- pip3 install pipenv 
    And :- $ pipenv install --python=3.8 -r requirements.txt

        I then started the project and also learning new fuctions. Finally i had coded the backend and hosted it on heroku. But there was a issue, heroku was flushing out the sqllite database(django default database) and thus anything posted was been deleted when you revisit the website. So, I again googled and found that postgresql is the best for production ready websites. So, I choose postgresql as my Django database manager but again the local setup on my laptop was very painfull. The postgresql was not running on port 5432 and there remained a connection issue even if I restarted postgresql using:- 
                $ sudo service postgresql restart
        I finally had to create a new user giving it all rights to the database and also changing the postgresql configration file by changing 'peer' to 'password'.

        And then I started thinking about the frontend, at first i thought of react js but i was entirly new to it and javascript so, I googled and found Bootstap(https://getbootstrap.com/) and then started working with it and soon I completed my frontend.
        Now I had to setup a smtp connection for sending meesages to users for resetting password and I choose gamil as it was easy and got a app password from google and stated setting up things.
        And atlast i wanted my website to be look cool so I wanted a cool background. I googled for free stock images and found unsplash, and the i found that it has a api which generates random images from a collection. The api is at https://source.unsplash.com . You have to refresh the page to see these random background images.

        And finally got a domain from Godaddy free for a year.The domain name is adityababar.co.

        And that is how this project was made possible.

</b></i>

## You can visit the website at https://adityababar.co | (https://chitchatchithere.herokuapp.com)

## <i>And thanks for MHL, porkbun and godaddy for providing a free domain.

### (The free domain was helpfull in url and mail forwading. It is cool having a custom domain.)</i>

## <b>This website has a lot of functions have modern dynamic websites have.And they are :-</b><hr>

$ reseting password<br>

$ a individual account<br>

$ a profile page<br>

$ a randomlly changing backgound after every refresh<br>

$ soon we would also be adding a personal feed page where all the posts, that you posted would appear.<br>

$ every user is given a unique id<br>

$ any irrelevant post can be reported at 'help@adityababar.co' with the link to the post and ur team would be inspecting the post and if the post is found irrelevent, then it would be deleted and the user would be given a warning. After 3 warnings! the user is baned from the website.<br>

$ Baned users can appolazise and give a valid reason, our team would inspect it and can unban the user.<br>

$ each post is shown with the date on which it was posted and by whom.<br>

$ each post also has a comment page, but currently the option is only in backend and not executed in frontend. <br>

## <b>Frameworks, Modules, Apis and domain and hosting used in the project. </b><hr>

### $ <u><b>Framework Used is :-</b></u>
### > Bootstarp
### $ <u><b>Api Used is :-</b></u>
### > unsplash(https://source.unsplash.com)
### $ <u><b>Modules used are :-</b></u>                 
### > django ==3.0
### > gunicorn ==19.9.0
### > whitenoise ==5.2.0
### > dj-database-url ==0.5.0
### > psycopg2-binary ==2.8.6
### > pylint
### $ <u><b>Hosted on :-</b></u>
### > Heroku
### $ <u><b>Domain used for url and email forwarding :-</b></u>
###   > adityababar.co  (-By porkbun)


