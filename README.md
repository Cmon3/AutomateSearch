# AutomateSearch

Company names will be taken from row 2 on Sheet 2\
Results will be exported to Sheet 3

![Screenshot1](/Images/RangeAndSheetId.PNG)

screadsheet id can be found in:

![Screenshot4](/Images/spreadsheetId.PNG)

Keywords included in the search query are "API" and "developer"\
Keywords excluded in the search are "apidashboard", "apitracker" and "linkedin"

![Screenshot2](/Images/keywords.PNG)

In case of adding, removing any keyword, or changing Sheet names these should be modified in the code.


Once the code is run, results in sheet 3 (3. Results!A1:C) will be overwritten.		
			
      

## To run the code in Digital Ocean:

Environment variables normally defined in a .env file, spreadsheet Id and google api credentials:

![Screenshot3](/Images/env.PNG)


should be defined in DO as:

G_SPREADSHEET_ID\
GOOGLE_APPLICATION_CREDENTIALS

like in this heroku screenshot:

![Screenshot5](/Images/heroku_vars.PNG)

you can follow the next guide, and take into account pasting the whole json of your google credentials:

[Digital Ocean Docs](https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/)

then this guide on how to create a droplet (which I think would be the best way) that will run on a specific date:

[Running automated python scripts in the cloud with cronjobs](https://medium.com/@cprkrn/running-automated-python-scripts-in-the-cloud-with-cronjobs-47476b33f817)

this guide in DO docs also talks about running a script on an automated schedule:

[Cómo usar Cron para automatizar tareas en Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804-es)

## How to run the code in Heroku

First create a new app 

![Screenshot6](/Images/heroku_newapp.PNG)

Define the enviromental variables in settings as seen before:

![Screenshot5](/Images/heroku_vars.PNG)

Deploy the app using git hub or the Heroku CLI

![Screenshot7](/Images/heroku_github.PNG)

Now to run the app once, first check that dynos are OFF otherwise the script will run endlessly:

![Screenshot8](/Images/dynosOff.PNG)

![Screenshot9](/Images/dynosOff2.PNG)

you can either add a ‘scheduler’ in Add-ons as in the following guide: 

[Schedule a Python script in Heroku](https://medium.com/analytics-vidhya/schedule-a-python-script-on-heroku-a978b2f91ca8)

Or run the script from the command line as a one-off dyno:

[One-off dyno execution syntax](https://devcenter.heroku.com/articles/one-off-dynos#:~:text=heroku%20run%20bash%0A...%0A~%20%24-,One%2Doff%20dyno%20execution%20syntax,-heroku%20run%20takes)

In this case as the app is defined in the procfile as app: python automatesearch.py, using the command Heroku run app, would be enough.

Be aware that before executing the app from the command line, to do "Heroku login" and initialize the app from there

### Extra links

[Deploying with Git](https://devcenter.heroku.com/articles/git)

[Running Apps Locally](https://devcenter.heroku.com/articles/heroku-local)

## Other simple way to run the app without having to deploy it

Another way to running the code without deploying it, would be create a notebook in https://colab.research.google.com/

Copy the code there, create and upload a .env file to the root directory:

![Screenshot10](/Images/colab_env.PNG)

![Screenshot3](/Images/env.PNG)

Be sure to remove spaces in the GOOGLE_APPLICATION_CREDENTIALS variable inside the .env file.

Ready to run the script!

## Cheers!

			
      
   
