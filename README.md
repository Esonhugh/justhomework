# justhoemwork 

## simple api server by flask app

## Usage :

```
pipenv --version || pip3 install pipenv
pipenv install  # install dependencies

flask initdb  # init database
python3 app.py # start server 

```

## Api docs

1. access the server.it will show on screen
2. comments in app.py

# Docker build

```yarn
$ sudo docker build . -t flask1.0                                                                                                                                                                          1 ⨯
Sending build context to Docker daemon  113.2kB
Step 1/8 : FROM python:3.9.7-buster
3.9.7-buster: Pulling from library/python
5e7b6b7bd506: Pull complete 
fd67d668d691: Pull complete 
1ae016bc2687: Pull complete 
0b0af05a4d86: Pull complete 
ca4689f0588c: Pull complete 
a4f7d469d2a7: Pull complete 
384a20add4c7: Pull complete 
9994334777a6: Pull complete 
c7be20aeb0a3: Pull complete 
Digest: sha256:097bd0cda01b32d79ca4db7ab0ee8dbe45d75758da86d016abdad43ea21adca0
Status: Downloaded newer image for python:3.9.7-buster
 ---> cfbbdf2f1490
Step 2/8 : WORKDIR /app
 ---> Running in 20df9b378dfa
Removing intermediate container 20df9b378dfa
 ---> 2fed7b2ddcd6
Step 3/8 : COPY . .
 ---> 5e3b31b7be7f
Step 4/8 : RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv
 ---> Running in 707f8db3f7bf
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting pipenv
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/c1/a3/d266421362565864f130cb97f55f70c763b843c9a67311d215d75b7ec464/pipenv-2021.5.29-py2.py3-none-any.whl (3.9 MB)
Collecting virtualenv-clone>=0.2.5
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/21/ac/e07058dc5a6c1b97f751d24f20d4b0ec14d735d77f4a1f78c471d6d13a43/virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
Collecting certifi
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/05/1b/0a0dece0e8aa492a6ec9e4ad2fe366b511558cdc73fd3abc82ba7348e875/certifi-2021.5.30-py2.py3-none-any.whl (145 kB)
Requirement already satisfied: pip>=18.0 in /usr/local/lib/python3.9/site-packages (from pipenv) (21.2.4)
Requirement already satisfied: setuptools>=36.2.1 in /usr/local/lib/python3.9/site-packages (from pipenv) (57.5.0)
Collecting virtualenv
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/fe/45/3c419850680999c43f5e3d005e2f54bb3a24184255ebc5244369e49674bd/virtualenv-20.8.1-py2.py3-none-any.whl (5.3 MB)
Collecting filelock<4,>=3.0.0
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/e0/a5/23349971aaf2bb56cf0bb084e51b4020098e53465c97eeb730e2e2a1da13/filelock-3.1.0-py2.py3-none-any.whl (8.4 kB)
Collecting backports.entry-points-selectable>=1.0.4
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/0c/cd/1e156227cad9f599524eb10af62a2362f872910a49402dbd2bea2dedc91c/backports.entry_points_selectable-1.1.0-py2.py3-none-any.whl (6.2 kB)
Collecting six<2,>=1.9.0
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting distlib<1,>=0.3.1
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/28/36/4bdfb663826d6deedc30b179a7b7876a86943cec9fcfc3f1638489fd8b09/distlib-0.3.3-py2.py3-none-any.whl (496 kB)
Collecting platformdirs<3,>=2
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/b1/78/dcfd84d3aabd46a9c77260fb47ea5d244806e4daef83aa6fe5d83adb182c/platformdirs-2.4.0-py3-none-any.whl (14 kB)
Installing collected packages: six, platformdirs, filelock, distlib, backports.entry-points-selectable, virtualenv-clone, virtualenv, certifi, pipenv
Successfully installed backports.entry-points-selectable-1.1.0 certifi-2021.5.30 distlib-0.3.3 filelock-3.1.0 pipenv-2021.5.29 platformdirs-2.4.0 six-1.16.0 virtualenv-20.8.1 virtualenv-clone-0.5.7
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv                                                                                                                                                                                                     
Removing intermediate container 707f8db3f7bf                                                                                                                                                                     
 ---> 813bb2eb3e0e
Step 5/8 : RUN python3 -m pipenv install
 ---> Running in d86d0d21c13f
Creating a virtualenv for this project...
Pipfile: /app/Pipfile                                                                                                                                                                                            
Using /usr/local/bin/python3.9 (3.9.7) to create virtualenv...                                                                                                                                                   
⠦ Creating virtual environment...created virtual environment CPython3.9.7.final.0-64 in 1098ms                                                                                                                   
  creator CPython3Posix(dest=/root/.local/share/virtualenvs/app-4PlAip0Q, clear=False, no_vcs_ignore=False, global=False)                                                                                        
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)                                                                          
    added seed packages: pip==21.2.4, setuptools==58.1.0, wheel==0.37.0                                                                                                                                          
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator                                                                                                    
                                                                                                                                                                                                                 
✔ Successfully created virtual environment!                                                                                                                                                                      
Virtualenv location: /root/.local/share/virtualenvs/app-4PlAip0Q                                                                                                                                                 
Installing dependencies from Pipfile.lock (23b4fc)...                                                                                                                                                            
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Removing intermediate container d86d0d21c13f
 ---> 943874a31bf2
Step 6/8 : EXPOSE 8080
 ---> Running in c007a33d4f73
Removing intermediate container c007a33d4f73
 ---> 7927d6640197
Step 7/8 : CMD [ "python3", "-m" , "flask", "initdb"]
 ---> Running in 9638f2215fc7
Removing intermediate container 9638f2215fc7
 ---> 11355aa61205
Step 8/8 : CMD ["python3","app.py"]
 ---> Running in acaa2d98fcd9
Removing intermediate container acaa2d98fcd9
 ---> 9cae08a886ec
Successfully built 9cae08a886ec
Successfully tagged flask1.0:latest


```

