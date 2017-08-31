FROM python:2.7.10
COPY temp_http.py /tmp
EXPOSE 3000
RUN chmod u+x /tmp/temp_http.py

HEALTHCHECK CMD curl -f http://localhost:3000/ || exit 1

CMD ["python", "-u", "/tmp/temp_http.py"]

