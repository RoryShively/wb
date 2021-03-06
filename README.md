# Project

This project runs a web application with a rest api using Docker and Flask. Download the project, get it up and running using the instructions below, then upload the "us-500.csv" file provided in this repo to populate the database.

## Requirements

This project has been tested using:
 - Docker version `v 1.12.3`
 - Docker-compose `v 1.8.1`

## Installation

1. Open up your terminal under the directory you want to put this project in and clone this repo

    `git clone https://github.com/RoryShively/wb.git`

2. cd into the project

    `cd wb`

3. Build the containers with docker-compose and run them

    `docker-compose up --build`'

4. In another terminal window and cd into the project directory

    `cd /path/to/directory/`

5. Initiaize the database to create tables

    `docker-compose exec website wayblazer db init`

6. Open up your browser and go to the website

#### From here you should:
 - Click Sign Up in the top right corner to create an account
 - Once logged in, click CSV Upload in the top right corner
 - Upload `us-500.csv`

## Command line Tools

### Database commands

 - Initialize the database
 
 `docker-compose exec website wayblazer db init`
 
 - Seed the database with one user
 
 `docker-compose exec website wayblazer db seed`
 
 _user: roryshively1@gmail.com_
 
 _password: asdfasdf_
 
 - Reset the database
 
 `docker-compose exec website wayblazer db reset`
 
 _clears the database, runs init, then runs seed_

 - Access the database in the terminal
 
 `docker-compose exec postgres psql -U wayblazer`
 
<!--### Testing commands-->

 <!--- Run test suite-->
 <!---->
 <!--`docker-compose exec website wayblazer test`-->
 <!---->
 <!--- Run test coverage-->
 <!---->
 <!--`docker-compose exec website wayblazer cov`-->
 <!---->
 <!--- Run flake8-->
 <!---->
 <!--`docker-compose exec website wayblazer flake8`-->
 
## REST docs and Interview questions

View REST API docs at `<base_url>/rest-docs` 



 
<!--Who works for Rapid Trading Intl?-->
  <!--<base_url>/api/employee?company=Rapid%20Trading%20Intl-->

<!--Do any employees have the same personal phone number? 504-845-1427-->
  <!--<base_url>/api/employee?duplicate_number=true-->

<!--Bonus: Find all employees with a personal Gmail email address but exclude-->
 <!--anyone from CA.-->
  <!--<base_url>/api/employee?email_provider=gmail&exclude_state=CA-->


