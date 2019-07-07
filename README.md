# Cats-And-Dogs
A web app to classify images of cats and dogs.

## Getting Started

In terminal go to the root directory of the project and run :
```
python3 manage.py runserver
```
or
```
python3 manage.py runserver -h HOST
```
to start the flask development server.

The former will start the flask-server on localhost at port 5000

Go to https://127.0.0.1:5000 to view the homepage.


### Prerequisites

Requirements can be found in requirements.txt

To Install dependencies : 

```
pip install -r requirements.txt
```

In addition to these you will require vgg19 weights fine tuned for classifying cats and dogs.
Weights can be downloaded from [here](https://drive.google.com/open?id=1OS-jRgfnhaB9vm5OfGJgPwipaoUDUkH3).
Place the weights (.h5 file) at vgg19/ml/


## Built With

* [Flask](http://www.flask.pocoo.org) - Backend Framework
* [Bootstrap 4](https://getbootstrap.com) - Frontend Framework
* [jQuery](https://jquery.com) - JavaScript Library
* [VGG19 Model](https://www.kaggle.com/keras/vgg19/home) - Pretrained Weights
* [Keras](https://maven.apache.org/) - For Fine Tuning VGG19 Model



## Author

* **Ayush Tiwari**
