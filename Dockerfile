# Gunakan base image Python
FROM python:3

# Set working directory di dalam container
WORKDIR /app
EXPOSE 80

# Copy file requirements.txt ke dalam container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh konten direktori saat ini ke dalam container
COPY . .


# Jalankan skrip Python
CMD ["python3", "kuso.py"]
