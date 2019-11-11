# BLOGGERS
## Author

[Alex-Mwaura](https://github.com/alexmwaura)

# Description
This is a django application that display images for different categories and locations

## Live Link
[View Site]()




## User Story

* A user can click on the image and modal pops.
* A user can be able to copy the image link.
* A user can search art based on category name.
* After search a user can click on image to view it on another page
* A user can click on location to view art for that location


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** |  Select Image or search category|
| Select Location | **Location** | Redirected to page location|
| Click on Image | **Modal** | Modal opens and user can copy link to image|
| Select comment button | **Category** | View Categories to search for|






## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/alexmwaura/ARTGALLA
  ```
2. Move to the folder and install requirements
  ```bash
  cd ARTGALLA
  pip install -r requirements.txt
  ```
3. Exporting Configurations

4. Running the application
  ```bash
  python manage.py runserver
  ```
5. Testing the application
  ```bash
  python manage.py art test
  ```
Open the application on your browser `127.0.0.1:8000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Djano](http://flask.pocoo.org/)
* [Javascript](http:javascript.com)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [alexmwaura2015@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Alex Mwaura**