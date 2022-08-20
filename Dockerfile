From python:3.10.0-alpine
COPY . /app
WORKDIR /app
RUN pip install -r ./requirements.txt
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f  http://localhost:5000/health || exit 1
CMD ["python3", "app.py"]