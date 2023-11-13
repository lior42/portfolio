# My Portfolio Website

A small website, made for my portfolio.

## Features
- Responsive design
- Working "Contact Me" Form

## Technologies in use

- [FastAPI](https://fastapi.tiangolo.com/): The web framework used in this project.
- [MongoDB](https://www.mongodb.com/): The NoSQL database used for data storage.
- [Jinja2](https://jinja.palletsprojects.com/): The template engine for Python used for rendering HTML.


## Configurations
done via environment variables
- *LPDB_URL* - Mongo connection string (default: `mongodb://localhost:27017`)
- *LPDB_NAME* - The database name (default: `lior_portfolio`)
- *LPBIND_IP* - The ip address to bind too (default: `127.0.0.1`)
- *LPPORT* - The port to bind too (default: `8000`).

## Project structure

- Root directory: Contains various configurations, also contains any 3th party licenses.
- `static` directory: Contains the static assets of the project.
- `templates` directory: Contains the Jinja2 templates for the project, in the root we have the layout related templates, under `comp` directory we have small templates that encapsulate a single item (for example: `company.j2` is the template for a single company), and in `pages` directory we have the layouts for the actual pages.
- `src` directory: contains all the python code, its a flat structure since there are no many files and it is kind of unnecessary.

## Usage
You can use that project as a template for your own portfolio/resume website.
you can start with the following commands:

```sh
$ git clone git@github.com:lior42/portfolio.git
$ cd portfolio
$ pip3 install -r ./requirements.txt
$ python3 ./src/main.py
```
you may want to create a virtual environment though.

## License

- This project is licensed under the [MIT License](LICENSE).
- The favicon is under [SIL Open Font License, 1.1](http://scripts.sil.org/OFL), see [Favicon License](favicon-license.txt) for more details.
