FROM python:2.7.10
COPY temp_http.py /tmp
EXPOSE 3000
RUN chmod u+x /tmp/temp_http.py

CMD /tmp/temp_http.py

