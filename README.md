# THB/USD Exchange Rate Forecasting Project

โปรเจคพยากรณ์อัตราแลกเปลี่ยน THB/USD โดยใช้ Machine Learning (XGBoost) และ Deep Learning (LSTM, TFT) พร้อมระบบ Data Pipeline อัตโนมัติด้วย Airflow และ API สำหรับ Deployment บน Render

## 🌟 ฟีเจอร์หลัก (Key Features)
*   **Automated Data Pipeline:** ใช้ **Airflow** ดึงข้อมูล (Yahoo Finance), ทำความสะอาด, และสร้าง Features อัตโนมัติทุก 10 นาที
*   **Advanced Modeling:** เปรียบเทียบโมเดล XGBoost, LSTM, และ TFT เพื่อหาโมเดลที่ดีที่สุด
*   **Deployment Ready:** มี API (FastAPI) พร้อม Deploy ขึ้น Render ได้ทันที
*   **Database:** ใช้ PostgreSQL ในการจัดเก็บข้อมูลทั้งหมด

## 📂 โครงสร้างโปรเจค (Project Structure)
```
THB_Forecast/
├── airflow/                     # Airflow Configuration
│   ├── dags/                    # DAGs (Data Pipeline Logic)
│   ├── docker-compose.yaml      # Docker Setup for Airflow
│   └── Dockerfile               # Custom Airflow Image
├── src/
│   ├── de/                      # Data Engineering (ETL)
│   ├── ds/                      # Data Science (Model Training)
│   ├── app.py                   # FastAPI Application (Inference)
│   └── inference_xgboost.py     # Model Inference Logic
├── .env                         # Environment Variables (Database Config)
├── render.yaml                  # Render Deployment Config
├── requirements.txt             # Python Dependencies
└── README.md                    # Documentation
```

## 🛠️ การติดตั้งและใช้งาน (Installation & Usage)

### 1. สิ่งที่ต้องเตรียม (Prerequisites)
*   **Docker Desktop** (สำหรับรัน Airflow)
*   **Python 3.9+** (สำหรับรัน Model Training / API)
*   **PostgreSQL** (Database)

### 2. การตั้งค่า (Setup)
1.  **Clone Project:**
    ```bash
    git clone <repository_url>
    cd THB_Forecast
    ```
2.  **สร้างไฟล์ `.env`:** (ที่ root directory)
    ```env
    DB_HOST=host.docker.internal  # สำหรับ Docker ให้มองเห็น Host
    DB_PORT=5432
    DB_NAME=thb_forecasting
    DB_USER=postgres
    DB_PASS=your_password
    ```

### 3. การรัน Data Pipeline (Airflow)
ระบบนี้ใช้ Airflow ในการดูดข้อมูลและเตรียมข้อมูลอัตโนมัติ

1.  เข้าไปที่โฟลเดอร์ airflow: `cd airflow`
2.  เริ่มระบบ: `docker-compose up -d --build`
3.  เข้าใช้งาน: [http://localhost:8080](http://localhost:8080) (User/Pass: `airflow`)
4.  เปิดสวิตช์ DAG `thb_data_pipeline` ให้ทำงาน

### 4. การเทรนโมเดล (Model Training)
เมื่อมีข้อมูลใน Database แล้ว สามารถเทรนโมเดลได้:

```bash
# สร้าง Virtual Environment
python -m venv venv
source venv/bin/activate  # หรือ .\venv\Scripts\activate ใน Windows

# ติดตั้ง Library
pip install -r requirements.txt

# เทรนโมเดล XGBoost
python -m src.ds.models.train_xgboost
```

### 5. การรัน API (Local Testing)
```bash
uvicorn src.app:app --reload
```
*   API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🚀 การ Deploy ขึ้น Render
โปรเจคนี้รองรับการ Deploy บน Render.com

1.  Push โค้ดขึ้น GitHub
2.  สมัคร Render และเลือก **New Web Service**
3.  เชื่อมต่อ GitHub Repo
4.  ตั้งค่า Environment Variables ใน Render Dashboard (เหมือนใน .env แต่แก้ `DB_HOST` เป็น Host จริงของ Database)
5.  สั่ง Deploy!

## 📊 รายละเอียดโมเดล (Model Details)
*   **Input Features:** ราคาทอง, น้ำมัน, Bond Yield, DXY, RSI, MACD, Lag Features ฯลฯ
*   **Target:** การเปลี่ยนแปลงของราคา (Price Diff)
*   **Performance:** ดูได้จาก Notebook `modeling_comparison.ipynb`

## 👥 ผู้พัฒนา
*   **Data Engineering:** [ชื่อของคุณ/ทีมงาน]
*   **Data Science:** [ชื่อของคุณ/ทีมงาน]
