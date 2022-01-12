# AutomateSearch

Company names will be taken from row 2 on Sheet 2\
Results will be exported to Sheet 3

![Screenshot1](/Images/RangeAndSheetId.PNG)

Keywords included in the search query are "API" and "developer"\
Keywords excluded in the search are "apidashboard", "apitracker" and "linkedin"

![Screenshot2](/Images/keywords.PNG)

In case of adding, removing any keyword, or changing Sheet names these should be modified in the code.


Once the code is run, results in sheet 3 (3. Results!A1:C) will be overwritten.		
			
      

## To run the code in Digital Ocean:

Environment variables normally defined in a .env file, spreadsheet Id and google api credentials:

![Screenshot3](/Images/env.PNG)

![Screenshot4](/Images/spreadsheetId.PNG)

should be defined inside as:

G_SPREADSHEET_ID\
GOOGLE_APPLICATION_CREDENTIALS

like in this heroku screenshot:

![Screenshot5](/Images/heroku_vars.PNG)

you can follow this information:

[Digital Ocean Docs](https://docs.digitalocean.com/products/app-platform/how-to/use-environment-variables/)

then this guide on how to create a droplet (which I think would be the best way) which will run on a specific date:

[Running automated python scripts in the cloud with cronjobs](https://medium.com/@cprkrn/running-automated-python-scripts-in-the-cloud-with-cronjobs-47476b33f817)

this guide in DO docs also talks about running a script on an automated schedule:

[Cómo usar Cron para automatizar tareas en Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804-es)




			
      
   
