# How to Run
You can review the final work [here](https://github.com/ajkarella/tj07182023/blob/main/docker_proj/notebooks/clean_data_exploration.ipynb). This is the cleaned-up notebook where I presented all 4 answers, and it's pretty readable in GitHub.

If you want to recreate the project:
 - download the repo
 - download the datasets ([here](https://www.kaggle.com/datasets/gauthamp10/apple-appstore-apps) and [here](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps))
 - extract and drop the dataset's CSVs into `docker_proj\csvloader\data`
 - run in docker using `cd docker_proj` and `docker-compose up -d`
 - wait for postgres and the python data loader to run (takes about 5 minutes)
 - go to http://localhost:8888/
 - run the notebook(s)
