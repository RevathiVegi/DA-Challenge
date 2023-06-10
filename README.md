# Introduction to the DA Challenge Problem

The goal of this challenge problem is to give you an introduction to real data questions that you will 
be asked to solve at our company. Not only are we interested in whether you can answer all of the questions,
but we are also interested in following:
* how well can you follow the instructions (and update if needed)?
* can you use github, commit your code, and submit a pull request for our team to review?
* can you get the docker container to run?
* can you get the pytests to run?
* can you query the postgres database from python?
* how do you attack the problem?
* how well do you code?
* are you able to create visualizations to support your analysis?  


REQUIREMENTS: In order to complete this challenge, you will need the following:
* A computer with internet and python
* A Github account. At the end of this challenge you will be committing your code to github, and inviting 
our team to review your code and results.

PLEASE NOTE: It is very possible that the directions included in this README.md are not 100% correct. 
We simply ask that you update the README to reflect what worked for you.

You will have 4 days to work on the problem, but the problem was designed to take no 
more than 4 hours on the problem. You can work longer than 4 hours, if you like, but please be honest
with the amount of time you spent. And if you are wondering why we give you 4 days if it only takes 
4 hours, here is the answer: we know you are busy and may not have 4 hours on one day to work on the problem.

You are welcome to use any internet resources to help you with the problem. 
The only restrictions are that you work independently, do not share the data, or the results. 

Please insert your name and start date on the next line:
```markdown
I <insert your name> started the challenge on <enter the current date and time>
```

# Getting Started with the Github Repo

## Create a new private repository in your Github Account
No instructions are given for this step as it is something we think you should have the ability to do or look up.
Please invite the following people as collaborators to this repo:
* aeevered
* ed-nykaza
* lamdoanduc
* dankorelitz

## Unzip the .zip file
Unzip the da_challenge_problem-main.zip file that was given to you.
Take note of where you put the file, as you will need to navigate to that location in your terminal (below).

## Add .csv file extensions to gitignore
We suggest that you do not commit the .csv data files to Git, so first add .csv file extension to the .gitignore
file.

NOTE: Depending on how you approach the challenge problem, you may want to add other file extensions (such as certain
configuration files) to the .gitignore, but this is not required.

If any of your challenge problem answers are formatted as .csv files, do make sure these are still added to your
repository.

## Make an initial commit the files (from the zip file) to your new private repository
No instructions are given for this step as it is something we think you should have the ability to do or look up.

## Create a branch that you will be doing the challenge problem in
No instructions are given for this step as it is something we think you should have the ability to do or look up.

# Install Docker, Build, & Start the Docker Container
If you haven't installed Docker yet, you'll need to do so first. Docker provides a convenient installation script for most major operating systems, which you can find on their website. Here are some instructions for common operating systems:
NOTE: you will have to keep docker running in the background, in order to complete the rest of the challenge problem.

## Install Docker
### Linux
```commandline
sudo apt-get update
sudo apt-get install docker.io
```

### macOS
Install Docker Desktop for Mac by downloading and running the installer from [Docker's website](https://docs.docker.com/desktop/install/mac-install/).
Note: there is a version for Macs with Intel Chips and Apple M1/M2 Silicon Chips

### Windows
Install Docker Desktop for Windows by downloading and running the installer from [Docker's website.](https://docs.docker.com/desktop/install/windows-install/)
NOTE: you may need to update your wsl.kernel

## Build the Docker Image
Make sure that the Docker App you downloaded is running on your machine. 
Then pull up a terminal on your computer and navigate to folder or directory where you put contents of the zip file.
NOTE: not where you put the zip file, but inside the folder 'da_challenge_problem'
```commandline
docker build -t my-postgres-db . 
```
Confirm the image has been created successfully
```commandline
docker images
```

You should see somthing like:
```commandline
REPOSITORY                          TAG                    IMAGE ID       CREATED             SIZE
my-postgres-db                      latest                 886af37dc68c   10 minutes  ago   407MB
```

## Start (run) the Docker Container 
```commandline
docker run --name my-postgres-container -d -p 5432:5432 my-postgres-db
```

## Confirm your docker container is running
```commandline
 docker ps
```
You should see something like:
```markdown
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                    NAMES
9eed46417d9f   my-postgres-db   "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds   0.0.0.0:5432->5432/tcp   my-postgres-container
```

## Confirm that you can access postgres from python
From your favorite python IDE (e.g., Pycharm, VSCode, Spyder) or from the terminal, 
run `test_db_connection_and_data.py` with pytest to be sure that your connection to 
postgres is working and that the data needed for the challenge has properly loaded. 

HINT: you will need to pip install the python packages needed to run the script.
ADVANCED: you can load the requirements.txt file into your virtual environment.

If your docker container was installed correctly, then all 3 pytests should pass. You should get something like
```markdown
============================= test session starts ==============================
collecting ... collected 3 items

test_db_connection_and_data.py::test_db_connection PASSED                [ 33%]
PostgreSQL server version: ('PostgreSQL 15.2 (Debian 15.2-1.pgdg110+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit',)

test_db_connection_and_data.py::test_that_my_db_in_postgres PASSED       [ 66%]
test_db_connection_and_data.py::test_table_count PASSED                  [100%]
users table row count: 5699
device_syncs table row count: 504733
webapp_pageviews table row count: 5792
bridge_clinics_to_patients table row count: 5991
bridge_clinics_to_professionals table row count: 113


============================== 3 passed in 0.21s ===============================
```

### Extra Steps (if/when needed) Stop/Start/Remove the Docker Container
#### Stop the container
Here is the command to stop the docker container.

NOTE: you will need the docker container running to complete the challenge, 
so you probably don't want to stop or delete it now, but when that time comes, here are the commands:
```commandline
docker stop my-postgres-container-id
```
#### Start the container
Here is the command to re-start the docker container.
```commandline
docker start my-postgres-container 
```

#### Get Status of docker container
You can use `docker ps` to check that it has been stopped or started.

#### Remove docker container
And if you want to destroy/delete the image you can remove with.
But, to state the obvious, if you remove the container, you will need to re-build it.
```commandline
 docker rm my-postgres-container
```

## Let's Pause: Wrapping up the Docker Container Section
Please be honest, how long did it take you to get to this point in process. 
Please fill in the <> with your response: 
```markdown
It took me <insert amount of time > to get to this point in the instructions.
I was <able, not able> to get the docker container to run.
I was <able, not able> to get pytests to pass.
```

# The DA Challenge Problem
For this challenge problem, please assume that the current date is 2023-02-01.
All the data you are working with is FAKE but inspired by real data, including the column names that we use 
in our database tables. 

For this challenge problem you have 5 tables in your postgres database to work with:
* users - a list of users and some basic demographics
* device_syncs - a list of users' diabetes device sync timestamps, which also include the device source  
* webapp_pageviews - a list of users that logged into our web app and viewed patients data, along with some basic stats
* bridge_clinics_to_patients - a bridge table that associates patient-users to the clinics they are associated with 
* bridge_clinics_to_professionals - a bridge table that associates professional-users to the clinics they are associated wtih

NOTE: if you are curious about the datatypes in each of the columns, please take a look at `database/load_data.sql`
 
## Example showing you how to run a query from a .sql file
From your favorite python IDE (e.g., Pycharm, VSCode, Spyder) or from the terminal, 
run `example_get_data_from_sql_file.py` which should return the first 10 rows a `users` table in your `my_db` database.
The result should look something like:
```markdown
                                       user_id__deid  ... diabetes_type
0  9e29552bb0a70b9fe8ca05ab739fc916c8e2217ef0d95d...  ...        type_1
1  f9717d46496141d9fa6ffeb74a8403d8326495015323fd...  ...        type_1
2  f8a6d183ee48480361c8242a830f17da12abd6229ae62b...  ...        type_1
3  a972c60b9cfbe375a3c88d0e39c3c5a6e510af26f59853...  ...          None
4  4d8ff20367fc9da5ea37ea8a5fe9aac38ff169a6d73387...  ...          None
5  6c4f90d59ee14f4d0a1a999e3bd8d1ffb09381e9dd56b7...  ...        type_1
6  417c250defab38541cfda49f5ebae34a0235567f36b6cd...  ...        type_1
7  8530b64e0647c30fd00576c6a4a33c0ebc3a454fa35ec3...  ...        type_2
8  c9b6d17ce9012cf06f4cfc16a34ea440d36d7d6a1f5e8e...  ...          None
9  6683d8c12de977298c1c4d8770035d5b349c56d18eec52...  ...          None
```

## Challenge Questions
As a data analyst our company, you will be asked to provide insights to our internal customers (e.g., 
the partner management team, the account management team, executive team, and product teams) and to some of our
external partners as well. They often want to know information on users, clinics, and devices. Please answer 
the following questions using the 5 tables described above. Please document your work. You can add your answers
to this readme or can create a separate document, we only ask that you make it easy for us to review your results
and to see how you got your results (e.g., the code and SQL you wrote). 

### Users: How many users do we have?
NOTE: we have two types of users: patient users and professional users. Starting with the `users` table, 
please answer the following:
* [ ] how many all-time users do we have? 
    * [ ] please break the counts down by patient, professional, and combined (patient and professional) users
    * [ ] what is the age distribution of our users?
    * [ ] what is the distribution of diabetes type?

* [ ] how many active patient users have we had over the past year? and over the past month? 
NOTE: To answer this question, an active patient user is one that is actively syncing device data
    * [ ] do you see any trends with our active patient users? 
    * [ ] please use your favorite python plotting tool to visualize the trends

* [ ] how many active professional users have we had over the past year and the past month? 
NOTE: To answer this question, an active professional user is one that is viewing patients data in our webapp
    * [ ] do you see any trends with our active professional users?
    * [ ] please use your favorite python plotting tool to visualize the trends

### clinics and professional users
* [ ] how many active professional users does each clinic have?
* [ ] of the clinics that have professional users, which clinic has the most and least active patient users?
* [ ] do you see any trends regarding our clinics?
* [ ] please use your favorite python plotting tool to visualize the trends

### devices
* [ ] the product team wants to understand which devices (and combinations of devices) our users are syncing (uploading)
into our platform. Please quantify the types of devices people are using. 
* [ ] please comment on whether some clinics use certain devices or combinations of devices more than others
  
# Final Steps
Once you have completed all of your work, please take a minute to update this readme with instructions on how to 
review your work. Please commit all of the files/code you created, and submit a pull request to the 
gihub handles list above. Also let Mark know that you completed the challenge. 

## Final Wrap Up
How long did it take you to do the challenge?  
Please fill in the <> with your response: 
```markdown
I spent <insert amount of time > on the challenge problem.
I thought it was <easy, moderate, difficult>.
<pile on anything else you want us to know>
```
