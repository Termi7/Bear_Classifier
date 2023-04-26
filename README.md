The source code of both the bear image classifier back end
and the react app for the front end must be installed on your
machine for it to run.


For the back end install the listed files below.
• Before you do anything install python on your machine
from https://www.python.org/ and make sure you install
the pip package manager too.
 next run pip install –upgrade pip
 after run pip install TensorFlow==2.12.*
 Next run pip install Pillow
 Next run pip install fastapi
 Next run pip install ”uvicorn[standard]”
 pip install python-multipart
 Then proceed to run the model by navigating to the
Project4-AI folder and run python build-model.py


• After this start up the Fast API by doing uvicorn
main:app –reload in the command prompt.
If the server started correctly it should look like this below.
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to
INFO: Started reloader process [30708] using WatchFiles
1/1 [==============================] - 0s 150ms/step
Predicted class: grizzly
INFO: Started server process [25568]
INFO: Waiting for application startup.
INFO: Application startup complete.



