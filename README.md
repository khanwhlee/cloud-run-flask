# python-flask-swagger-demo on Google Cloud Run
My Readme
我拿了 flasgger demo code 來改寫，並演示如何部署到 Cloud Run 上面。

我一共做了兩件事
1. 更新 requirements 原本的太舊了
2. 增加 Dockerfile

Pull 後只需要執行打包
```
gcloud builds submit --tag gcr.io/{project_id}/{cloud_run_server_name}
```

再到 Cloud Run UI 選擇剛剛建立的 image 就可以


---
Original Readme

### Make sure python 3.X.X and virtualenv is installe in you PC

* Clone project in some dir
* Open terminal/command prompt
* Navigate to folder where the project is cloned
* For Windows run commands
  * python -m venv env
  * ./env/Scripts/activate
  * pip install -r dependency.txt
  * python app.py
* For Mac run commands
  * python3 -m venv env
  * source ./env/bin/activate
  * pip install -r dependency.txt
  * python3 app.py
* Now application is started 
* You can access the swagger page on http://localhost:8000/apidocs 

![Swagger UI](https://github.com/ashishkrgupta/python-flask-swagger-demo/blob/master/Screenshot%202019-07-11%20at%2011.32.00%20PM.png)


# Reference  
   https://pypi.org/project/flasgger/
