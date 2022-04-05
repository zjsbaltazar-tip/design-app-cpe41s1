FROM python
RUN pip install flask
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY designapp.py /home/myapp
EXPOSE 5050
CMD python3 /home/myapp/designapp.py
