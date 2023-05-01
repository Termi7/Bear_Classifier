# Bear Image Classifier

The Bear Image Classifier is a program that classifies bear images into three categories: black, grizzly, and teddy. This repository contains  the backend.

## Installation

To run the Bear Image Classifier, you must have both the backend and the React app for the frontend installed on your machine. 

1. Clone the repository by running the following command in your terminal: 
```
git clone https://github.com/Termi7/Project_4AI.git
```

2. Open the folder make sure your inside the Project4_AI folder
3. The project directory is composed of the source codes , the bears data set, Bear testing images and the report.  

4. Install the following packages for the backend:

```pip install --upgrade pip
pip install tensorflow==2.12.*
pip install Pillow
pip install fastapi
pip install "uvicorn[standard]"
pip install python-multipart
```

5.  Run the following command to build the model and the train the neutral network:
```commandline
python build-model.py
```

6. Start the Fast API by running the following command in the terminal:
```
uvicorn main:app --reload
```

If the server started correctly it should look like this below. 

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to 
INFO: Started reloader process [30708] using WatchFiles 
1/1 [==============================] - 0s 150ms/step 
Predicted class: grizzly 
INFO: Started server process [25568] 
INFO: Waiting for application startup. 
INFO: Application startup complete.
