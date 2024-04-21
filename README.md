# webdev_workshop

## Clone or update the repository

### If you HAVE NOT already cloned the repository:
Verify that you already have `git` on your computer. If not, please download the software from [this site](https://git-scm.com/downloads). 

(I make the assumption that you are familiar with using your terminal.) Run the following command in a directory where you would like to develop your code:

`git clone https://github.com/dhasteer/webdev_workshop.git`

### If you HAVE already cloned the repository:
Run the following command in the `webdev_workshop` directory wherever you cloned it: `git pull`.

## Environment Setup
Move to the `webdev_workshop` directory wherever you cloned it. Verify that you already have `python` on your computer (version 3.8+). If not, please download the software from [this site](https://www.python.org/downloads/). Then, run the following setup commands.
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
This will install all the necessary Python libraries to go through the demo.

## Agenda
1. Understanding HTML structure
    - [Reference](https://www.w3schools.com/tags/ref_byfunc.asp) on HTML tags
    - Learning about browser "inspect element" tool to navigate HTML
    - Exercise to add an element to the about page
2. Styling via CSS
    - [Reference](https://www.w3schools.com/cssref/css_selectors.php) on CSS selectors
    - Observe "inspect element" tool to identify applied style
    - Exercise to modify color for _only_ the about page headline
3. Brief discussion about Bootstrap library
    - Observe "import" via `bootstrap.min.css`, `bootstrap.min.js`
    - [Reference](https://www.w3schools.com/bootstrap/bootstrap_grid_system.asp) on Bootstrap layout
    - [Reference](https://getbootstrap.com/docs/4.0/components/alerts/) on Bootstrap custom components
4. Aside on JS / JQuery dynamic components
    - Exercise to identify some dynamic components
---
5. Introducing the Flask framework
    - Restructuring the website source files and media
    - API requests: `GET`, `POST`
6. End-to-end flow
    - How to communicate frontend input with backend 
    - How to communicate backend output with frontend
---
7. (Bonus) [Reference](https://ngrok.com/) to ngrok to interact with webapp using any device