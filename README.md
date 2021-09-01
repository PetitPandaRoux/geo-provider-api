# GEO-PROVIDER-API

A webservice that give you provider availibility on 3G,4G and 5G based on your location

## I. PROJECT STACK

- Django
- Django REST framework
- Gunicorn
- Configuration for Heroku Deployment

## II. SETUP

How to set up the project on a local machine

### REQUIREMENTS

## Requirements

Be sure to have those elements before starting

- Python 3 - [installation et doc](https://wiki.python.org/moin/BeginnersGuide)
- pipenv - [installation et doc](https://virtualenv.pypa.io/en/latest/)
- Git - [installation et doc](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Settings up project - using bash

```bash
git clone https:
cd geo-provider-api
```

```bash
pipenv install
pipenv shell
python manage.py migrate
```

## PROJECT STRUCTURE

You have 4 main directories

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

### 5.Others files

**env.prototype** contains definition about environmental variables used in the project
**api.swagger.docs** is the definition of our api following SWAGGER/OPEN API documentation

## FURTHER FEATURES

### COORDINATES CIRCLE PERIMETERS

In the near future we will check if coordinates given by user 
