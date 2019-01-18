
# DeliverIT-3 Parcels
DeliverIT-3 is a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Git
* Python 3.6.5
* Virtualenv

### Quick Start

1. Clone the repository

```
$ git clone https://github.com/Harrison-Gitau/DeliverIT-3.git
$ cd into the created folder
```
  
2. Initialize and activate a virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
```

3. Install the dependencies

```
$ pip3 install -r requirements.txt
```

4. Initialize environment variables

```
$ export SECRET_KEY=<SECRET KEY>
```

5. Run the development server

```
$ python app.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

At the / endpoint you should see Welcome to DeliverIT-3 API displayed in your browser.

## Endpoints

Here is a list of all endpoints in the DelicerIT-3 Parcels API

Endpoint | Functionality 
------------ | -------------
POST   /api/v2/auth/register | Register a user
POST   /api/v2/auth/login | Log in user
GET    /api/v2/users | Get all users
GET   /api/v2/users/id | Get a single user
PUT  /api/v2/users/id | Update a single user
DELETE   /api/v2/users/id | Delete a single user
POST   /api/v2/parcels | Create new parcel
GET   /api/v2/parcels | Get all parcels
GET   /api/v2/parcels/id | Get a single parcel
GET   /api/v2/users/userid/parcels | Get all parcel delivery orders by a specific user
DELETE   /api/v2/parcels/id | Delete a single parcel
PUT   /api/v2/parcels/parcelsid/cancel | Cancel a specific parcel delivery order


## Running the tests

To run the automated tests simply run

```
nosetests tests
```

### And coding style tests

Coding styles tests are tests that ensure conformity to coding style guides. In our case, they test conformity to
PEP 8 style guides

```
pylint app.py
```

## Deployment

Ensure you use Productionconfig settings which have DEBUG set to False

## Built With

* HTML5
* CSS3
* Python 3.6.5
* Flask - The web framework used

## GitHub pages

https://harrison-gitau.github.io/

## Heroku

#https://DeliverIT-v2.herokuapp.com/apidocs

## Versioning

Most recent version is version 2

## Authors

Harrison Gitau.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration and encouragement
* etc
