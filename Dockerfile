


FROM centos:centos7
WORKDIR /usr/lib/test-trigger
COPY say-hello.py /usr/lib/test-trigger
RUN python say-hello.py
ENTRYPOINT ["/bin/ping"] 
CMD ["localhost"]
EXPOSE 8080


