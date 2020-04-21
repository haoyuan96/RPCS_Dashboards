# Plume

[![Python 3.6](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

Plume is a web application to track and visualize PD patients' health status. It provide three dashboard for doctors, caregiver and patients.


## Background
The goal for the whole system is to design and engineer a system that can intervene during in-home situations to improve the life quality of the patient and track crucial physiological and a few cognitive data for doctors and caregivers.

## Install

💥Please make sure you have python 3.6/3.7.

**Install Plume from the Github source:**
```
git clone https://github.com/haoyuan96/RPCS_Dashboards.git
cd RPCS_Dashboards
```

Set up python virtual environment(you can skip this step if you don't want to set up venv):
```shell
python3 -m venv plume
source plume/bin/activate
# you are a windows user, please use following command to activate venv:
plume\Scripts\activate.bat
```

**Install dependency:**
```
pip3 install -r requirements.txt
```

**Run the Django Framework:**
```
cd Plume
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

😉Now you can see the web page on the http://127.0.0.1:8000/

## Contributing
Feel free to dive in! [Open an issue](https://github.com/haoyuan96/RPCS_Dashboards/issues/new) or submit PRs.

