# catalog_cars_project


## What it is and does
Runs a website called catalog car app.
It shows details about car companies and their models.
The user can login via Google or Facebook in order to create their own makes and models. They can add descriptions, pricing, and an image for each model they add.


You can run the project in a Vagrant managed virtual machine (VM) which includes all the
required dependencies (see below for how to run the VM). For this you will need
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from [Vagrant](https://www.vagrantup.com/downloads). Install the version for your operating system.
Virtual Box is the software that actually runs the VM. You can download it from [VirtualBox](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.
You will need to set up a vagrant enviroment to run this code. That environment can be downloaded from [Environment](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip). 

## Project contents
This project consists for the following files in the `catalog_cars_project` directory:

* `lotsofcars.py` - Is used to populate the database.
* `app.py` - The main Python script that serves the website.
* `fb_client_secrets.json` - Client secrets for Facebook OAuth login.
* `client_secrets.json` - Client secrets for Google OAuth login.
* `README.md` - This read me file.
* `/catalog_cars_project` - Directory containing the `catalog_cars_project` package.
    * `/static` - Directory containing CSS for the website.
    * `/templates` - Directory containing the HTML templates for the website, using
        the [Jinja 2](http://jinja.pocoo.org/docs/dev/) templating language for Python.
        See next section for more details on contents.

### Templates
The `/templates` directory contains the following files, written in HTML and the Jinja2
templating language:

* `deleteMake.HTML` - Delete a car make confirmaton page.
* `deleteModel.html` - Delete a car model confirmation page.
* `editMake.html` - Form to edit the details of a car make.
* `editModel.html` - Form to edit the details of a car model.
* `latestCars.html` - Home page for logged in users to show the latest models there were added.
* `login.html` - A login page that features OAuth Google and Facebook logins.
* `main.html` - This defines the common layout for all the templates. It contains the navbar and headers.
* `makes.html` - A home page that would be shown to non-logged in users.
* `newMake.html` -  A form for creating a new make.
* `newModel.html` -  A form for creating a new model.
* `oneModel.html` - A page that shows details on one model.
* `selections.html` - A page that shows all the models of a specific make.

## How to Run the Project
After you have downloaded and unzipped the vagrant [Environment](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip) file. 

Download the project zip file to you computer and unzip the file. Or clone this
repository into the vagrant directory of the vagrant environment.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and then enter the `vagrant` directory.

### Bringing the VM up
Bring up the VM with the following command:

```bash
vagrant up
```

This step can take a while if it is your first time running it.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

To get into the VM directory

```bash
cd /vagrant/
```

### Run application.py
On the first run of the application there will be no database present, so to create one populates it with sample data. Type this into the command line:

```bash
python lotsofcars.py
```

To start the webserver run `app.py` Type this into the command line:

```bash
python app.py
```

It then starts a web server that serves the application. To view the application,
go to the following address using a browser on the host system:

```
http://localhost:8000/
```

You should see three of the latest cars that were added. To make changes you will have to login either through google or facebook. 

