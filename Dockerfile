#
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app 

#
COPY ./static /code/static

#

COPY ./art-museum-master /code/art-museum-master


# 
CMD ["uvicorn", "app.mainv2:app", "--host", "0.0.0.0", "--port", "80"]
