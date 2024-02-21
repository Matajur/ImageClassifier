# Final teamwork of the section "Python Data Science"

A web service that classifies images using convolutional neural networks.

## Technical Description

* a web service with asynchronous engine and adaptive layout that classifies images using convolutional neural networks;
* a convolutional neural network capable of assigning the image transferred to it to one of the 10 classes proposed in the CIFAR-10 dataset;
* custom architecture with 92.1% accuracy on test images from the CIFAR-10 dataset;
* the web interface is implemented using the Django framework;
* the application is be containerized in Docker and the image uploaded to Docker Hub;
* the application is deployed in the Azure cloud and is available from the [link](http://172.214.52.28:8095/upload/);
* the source code is available on GitHub at the [link](https://github.com/Matajur/ImageClassifier);
* to download an image with app from Docker Hub, run:
> docker pull matajur/imageclassifier:imageclassifier
* to run the web application:
> docker run -p 8000:8000 imageclassifier
* using Docker-Compose:
> docker-compose up -d

> docker-compose down
* for more information see the [presentation](Project_Presentation.pdf)

## License

Apache License 2.0

## Contributions

### Lonely Debuggers:
* Dmytro Gavrylchenko - Team Leader
* Yurii Serhiienko - Scrum Master
* Hanna Sagan - Deployment Manager
* Vladyslav Stelmakh - Data Analyst
* Andriy Vovchok - QA Engineer
