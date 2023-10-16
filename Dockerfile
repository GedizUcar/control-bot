FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# Set environment variable to prevent prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and Python 3.10
RUN apt-get update && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    wget \
    unzip \
    python3.10 \
    python3.10-distutils \
    python3.10-venv \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/* 

# Install pip for Python 3.10
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    /usr/bin/python3.10 get-pip.py && \
    rm get-pip.py

# Install dependencies for Google Chrome
RUN apt-get update && apt-get install -y \
    libxss1 \
    libappindicator1 \
    libindicator7 \
    libasound2 \
    libnss3 \
    libxtst6 \
    libx11-xcb1 \
    libxss1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    xdg-utils \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Install Chromedriver
RUN wget https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin/chromedriver \
    && chown root:root /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

USER root

# Install dependencies using Python 3.10 pip
RUN /usr/bin/python3.10 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables (if needed)
ENV BOT_TOKEN=MTE0MjQ1NDYwMTYzMTY3MDM5NA.GsIaz1.nVgXI2tO731FQ_czq8OT4nL4yIsiR7vmahiIiY
ENV CHANNEL_ID=1142455185038397543
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python3.10", "-u", "main.py"]