# 🚀 FastAPI DevOps Utility Project
This project is a FastAPI-based DevOps utility application that provides:

     • 🔥 AWS EC2 old and new instance
  
     •  🚢 AWS S3 Bucket 

     • 💾 Disk usage, free space percent

     • ⚙️ CPU & Memory usage alerts

     • 📊 System health APIs 

  Designed for DevOps learning & internal infrastructure monitoring.

### 🧩 Project Architecture
    ├── app
    │   └── api.py              # FastAPI app initialization
    │
    ├── main.py                 # Application entry point
    ├── requirement.txt         # Project dependencies
    │
    ├── router                  # API route definitions
    │   ├── aws.py              # AWS related endpoints
    │   └── disk.py             # Disk & system monitoring endpoints
    │
    └── service                 # Business logic layer
        ├── aws_ec2.py          # EC2 services
        ├── aws_s3.py           # S3 services
        └── service_disk.py     # Disk, CPU, memory logic
### ▶️ How to Run the Project
  ####    1️⃣ Clone Repository
      git clone : https://github.com/Hyysuresh/python-for-devops.git
      
      cd project
  ####   2️⃣ Create Virtual Environment
      python -m venv .venv

      source .venv/bin/activate
  ####   3️⃣ Install Dependencies
      pip install -r requirement.txt

  ####   4️⃣ Run FastAPI Server
  
      python3.12 main.py
  ####  5️⃣ Open any browser

      http://localhost:8000
### 🧠 Example APIs
    Endpoint	              Description
       /                   Health check
       /doc                document
       /redoc               -------
       /aws/ec2	           All EC2 instance 
       /aws/s3	             All s3 bucket
       /disk/usage	       Disk usage percent
       /disk/free	         Free disk space
       /system/cpu	       CPU usage & alerts
           
