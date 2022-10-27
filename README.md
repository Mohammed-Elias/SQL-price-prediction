# File Structure
- `notebook.ipynb` is for buidling the model and connecting to the `SQL DB` and `NOSQL DB`
- `main.py` is the file where the `API` has been written, using [fastapi](https://fastapi.tiangolo.com/), and where you could start the server.
- `test_main.py` is the file where the test has been written, test and logic both, using `Mock`, `MagicMock` and `unittest`.
- `requirements.txt` is what you need to insatll in your virtual env to be able run the code locally.


# What to do first?
## Local Dev Env:
- Use `python >= 3.7`
- In order to seprate the dev envs as much as we could, `venv` has been used to work on this task.
- Create a `venv` environment, using the following command, please type in your Terminal:
    `python -m venv venv_test`, where `venv_test` is the name of the env.


## Install the required packages:
- `pip install requirements.txt` 


## Docker:
- Please make sure that you have docker installed in your local machine [Docker install](https://docs.docker.com/engine/install/).
- After Docker installtion is done, please keep Docker up and running, then run the following commands in your Terminal, the command is to insatll images from [Docker Hub](https://hub.docker.com/).
  ``` docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql ```
- Please note that you have to remember the password in MySQL image, if you're trying to connect to MySQL Worckbench or any other MYSQL IDE.
  ``` docker run --name some-mongo -p 27017:27017  -d mongo ```

## What to do now?
- Go to `notebook.ipynb` and start running the cells, please note that most of the cells has a markdown cell before it, just to give you a hint about the snippet inside.

## How to start the server?

- `cd` where the project is then, `uvicorn main:app`, ideally it has to run with `--reload` option, but I had some problems with it, so I would recommend running the server without it.

## How to run the tests:
- Just type in your Terminal in the same folder that has everything, `pytest`, and it will start running all the possible test.


## Next Steps, Further Improvment:
- First and foremost, I would recommend dockerizing the code of the `API`, and deploying it using `Kubernetes`.
- Regarding the download process of the model and the scalars, I woudl recommend using some Hyperscalers e.g: AWS, CGP, ..etc.
- Probably the code quality is not up to the high standards, so I would recommend refactoring a bit.
- Build pipelines to deploy the model.
- Build bash script to automate the building process Docker images and python virtual envs.