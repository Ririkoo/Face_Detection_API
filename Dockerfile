FROM jjanzic/docker-python3-opencv

# Install Flask
RUN cd ~ && \
    pip3 install flask flask-cors

# Copy web service script
RUN mkdir -p /root/face_detect_api
ADD . /root/face_detect_api

EXPOSE 5000
# Start the web service
CMD ["python3", "/root/face_detect_api/app.py"]
