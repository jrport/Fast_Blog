Simple blog using FastAPI and SQLite3 for the backend and Vue.js with Pico.css for the frontend.

Take a look at 

To run the application locally, simply:

- Clone the project

  `git clone https://github.com/jrport/Fast_Blog.git`
- Build the Docker image and tag it however you'd like

  `docker build --tag <name_of_tag> .`
- Create, name and run the Docker container

  `docker run --name <name_of_container> -d -p 80:80 <name_of_tag>`
- Open the [blog](http://127.0.0.1/)
