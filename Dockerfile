


FROM centos:centos7
WORKDIR /usr/lib/test-trigger
COPY say-hello.py /usr/lib/test-trigger
#RUN python say-hello.py
#ENTRYPOINT ["/bin/ping"]
ENTRYPOINT ["python","say-hello.py"] 
#CMD ["localhost"]
EXPOSE 8080


