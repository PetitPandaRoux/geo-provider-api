# GEO-PROVIDER-API

A webservice that give you provider availibility on 3G,4G and 5G based on your location

## I. PROJECT STACK

- Django
- Django REST framework
- Configuration for Heroku Deployment

## II. SETUP

How to set up the project on a local machine

### 1.REQUIREMENTS

Be sure to have those elements before starting

- Python 3.6.9 - [installation et doc](https://wiki.python.org/moin/BeginnersGuide)
- pipenv - [installation et doc](https://virtualenv.pypa.io/en/latest/)
- Git - [installation et doc](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 2.Settings up project - using bash

Get repo from github

```bash
git clone https://github.com/PetitPandaRoux/geo-provider-api
cd geo-provider-api
```

Run python classic setup using pipenv

Install dependencies

```bash
pipenv install
```

Run local environment for python

```bash
pipenv shell
```

Run python classic setup for django project

Create database

```bash
python manage.py migrate
```

Create superuser to access backend and create some provider geolocation by hand if needed

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

### 3.Filling local database

Finally you can fill database (locally) using one of the two following scripts :

```bash
python scripts/fill_database_dev.py
python scripts/fill_database_bulk_dev.py
```

### 4. How it works

**first step**: The webservice use data.gouv API to retrieve coordinates from address given.

**second step**: With thoses GPS coordinates we will look in our database for all provider gps coordinates around the given point. The coordinate will be the center of a square : 0.02 long by 0.02 lat by default

## III. PROJECT STRUCTURE

You have 4 main directories.

### 1.Project

A django project

It is where you will find project settings for dev and production environnements, urls

### 2.Api

A django app

It is where we handle serializers, views, integration test and api endpoints

### 3.Provider

A django app

It contains all element relative to our model, coordinate converter using pyproj and some unit tests

### 4.Scripts

The folder script contains all independant scripts

Using Heroku scheduler and one off dynos, it can be used to clean, purge, save or any other independant operations

**fill_database_dev.py** : Insert all row from the following csv https://www.data.gouv.fr/s/resources/monreseaumobile/20180228-174515/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv

**fill_database_bulk.py** : Insert all row from the following csv https://www.data.gouv.fr/s/resources/monreseaumobile/20180228-174515/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv using bulk_api

***warning*** Both scripts are slow. The first one because its goes one by one. The second because bulk_create doesn't trigger post_save signal, we need to create all fields/columns and it slows the script. There is also a risk of too much memory for second script.

### 5.Others files

**env.prototype** contains definition about environmental variables used in the project

**schema.yml** is the definition of our api following SWAGGER/OPEN API documentation using yml format

You can access the schema using the following endpoint : /openapi/

## IV FURTHER FEATURES

### COORDINATES AROUND CIRCLE AREA

In the near future we will check if coordinates given by user is inside a certain radius(1000 meters for example) of our coordinates instead of using a square area

***warning*** Because we use latitude and longitude in our square area, the area is not same depending on the **earth curvature**. The square will be smaller if the coordinate given is at the pole.

We will implement something like :
https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python
