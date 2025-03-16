# 🚀 Sales Lead Conversion Prediction API

## 🧠 Problem Statement
Sales teams struggle to identify which leads have the highest probability of converting into paying customers. This project aims to build an **ML-powered Sales Lead Conversion API** that predicts the likelihood of a lead becoming a customer.

---

## 🔍 Project Workflow

### 1️⃣ Develop Flask API (`app.py`)
- **Build a Flask API** that:
  - Accepts lead details as input (JSON format).
  - Utilizes a trained ML model to predict conversion probability.
  - Returns the prediction in JSON format.

**Sample Request Format:**
```json
{
  "features": [34, "Male", "Online Campaign", 45, 7, "Hot Lead", "Email", "Mobile"]
}
```

**Sample Response:**
```json
{
  "conversion_probability": 0.82
}
```

---

### 2️⃣ Dockerize the Application
Create a **`Dockerfile`** to containerize the Flask API for consistent deployment.

**Sample Dockerfile:**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

**Commands to Build & Run Locally:**
```sh
docker build -t sales_lead_api .
docker run -p 5000:5000 sales_lead_api
```

---

### 3️⃣ Push Docker Image to Docker Hub
1. **Log in to Docker Hub:**
   ```sh
   docker login
   ```
2. **Tag the Docker image:**  (Note: dockerhub username is same as github username)
   ```sh
   docker tag sales_lead_api <your_dockerhub_username>/sales_lead_api
   ```
3. **Push the image to Docker Hub:**
   ```sh
   docker push <your_dockerhub_username>/sales_lead_api
   ```

---

### 4️⃣ Deploy on AWS EC2
1. **Launch an AWS EC2 instance.**
2. **Install Docker on the instance:**
   ```sh
   sudo apt update
   sudo apt install docker.io
   ```
3. **Pull and run the Docker image:**
   ```sh
   docker pull <your_dockerhub_username>/sales_lead_api
   docker run -p 80:5000 <your_dockerhub_username>/sales_lead_api
   ```
4. The API will be accessible at: `http://<EC2-public-IP>/predict`

---

## 📂 Folder Structure
```
📂 LEAD_CONVERSION_AAD
├── 📂 archive
├── 📂 data
│   ├── customer_conversion_testing_dataset.csv
│   ├── customer_conversion_training_dataset.csv
├── 📂 models
│   ├── model_rf.pkl
│   ├── model_rf1.pkl
├── 📂 notebooks
├── 📂 static
├── 📂 templates
│   ├── index.html
├── .gitignore
├── **app.py**
├── archive.zip
├── **dockerfile**
├── LICENSE
├── **README.md**
├── **requirements.txt**
```

---

## 📋 Tech Stack
✅ **Python 3.9**  
✅ **Flask**  
✅ **Docker**  
✅ **AWS EC2**  
✅ **Machine Learning Algorithms** (e.g., Logistic Regression, XGBoost)  

---

## 🧪 Testing
- Test the API using **Postman** or **`curl`**:
```sh
curl -X POST -H "Content-Type: application/json" \
-d '{"features": [34, "Male", "Online Campaign", 45, 7, "Hot Lead", "Email", "Mobile"]}' \
http://<EC2-public-IP>/predict
```

---

## 🛠️ Requirements
Install dependencies using:
```sh
pip install -r requirements.txt
```

---

## 🚨 Key Tips
✅ Ensure `model.pkl` is included in your project directory.  
✅ For AWS deployment, open port `80` for HTTP requests.  
✅ Add appropriate error handling in `app.py` for better reliability.

---

## ❤️ Contributions
Contributions are welcome! Feel free to submit issues or pull requests to improve this project. 😊

---

## 📧 Contact
For queries or collaborations, reach out at: **maykat425@gmail.com**

