FROM arm64v8/python:latest
 

# Copy the Python Script to blink LED
COPY app/ /app

# Intall the rpi.gpio python module
RUN pip install --no-cache-dir rpi.gpio gpiozero

# Trigger Python script
CMD ["python", "/app/sequence.py"]
