# 🏦 CoreBanking | هسته‌ی بانکداری

A desktop core banking application built with Python, Tkinter and ttkbootstrap. It includes login with captcha, user registration, SMS verification (OTP) delivered through a RabbitMQ microservice, role-based home pages, and performance monitoring (database logging, Prometheus metrics and a Grafana dashboard).

<div dir="rtl">

برنامه‌ی دسکتاپ هسته‌ی بانکداری که با Python و Tkinter و ttkbootstrap ساخته شده است. شامل ورود با کپچا، ثبت‌نام کاربر، تأیید پیامکی (OTP) از طریق یک میکروسرویس مبتنی بر RabbitMQ، صفحه‌ی اصلی بر اساس نقش کاربر و پایش عملکرد (ذخیره‌ی لاگ در دیتابیس، متریک‌های Prometheus و داشبورد Grafana) است.

</div>

---

# 📌 Features | امکانات

- ✅ Login with username, password and captcha
- ✅ "Remember Me" option
- ✅ User registration with captcha
- ✅ SMS verification code (OTP) after login
- ✅ Retry button with a 2-minute countdown
- ✅ OTP delivery through RabbitMQ and a separate Notification microservice
- ✅ Role-based home page (Administrator / Banker)
- ✅ Layered architecture (Presentation / Business Logic / Data Access)
- ✅ SQL Server database with SQLAlchemy
- ✅ Secrets stored in a `.env` file
- ✅ Function execution logs saved in the database
- ✅ Execution metrics exposed to Prometheus
- ✅ Metrics displayed in a Grafana dashboard

<div dir="rtl">

- ✅ ورود با نام کاربری، رمز عبور و کپچا
- ✅ گزینه‌ی «مرا به خاطر بسپار»
- ✅ ثبت‌نام کاربر با کپچا
- ✅ کد تأیید پیامکی (OTP) بعد از ورود
- ✅ دکمه‌ی ارسال مجدد با شمارش معکوس ۲ دقیقه‌ای
- ✅ ارسال OTP از طریق RabbitMQ و یک میکروسرویس جداگانه‌ی Notification
- ✅ صفحه‌ی اصلی بر اساس نقش (مدیر / بانکدار)
- ✅ معماری لایه‌بندی‌شده (Presentation / Business Logic / Data Access)
- ✅ پایگاه داده‌ی SQL Server با SQLAlchemy
- ✅ نگهداری رمزها و کلیدها در فایل `.env`
- ✅ ذخیره‌ی لاگ اجرای توابع در پایگاه داده
- ✅ ارسال اطلاعات اجرا به Prometheus
- ✅ نمایش اطلاعات در داشبورد Grafana

</div>

### 🚧 In Progress | در حال توسعه

- Employee Management (Administrator)
- Account Management (Banker)
- My Profile editing

<div dir="rtl">

- مدیریت کارمندان (مدیر)
- مدیریت حساب‌ها (بانکدار)
- ویرایش پروفایل من

</div>

---

# 🏗 Architecture | معماری

CoreBanking does not call the SMS provider directly. It publishes the verification code to RabbitMQ, and the Notification microservice consumes it and sends the SMS through sms.ir.

<div dir="rtl">

CoreBanking مستقیم به سرویس پیامک وصل نمی‌شود. کد تأیید را در RabbitMQ منتشر می‌کند و میکروسرویس Notification آن را برمی‌دارد و از طریق sms.ir پیامک می‌فرستد.

</div>

[![Architecture diagram](https://raw.githubusercontent.com/zahrasalimzadeh/NotificationMicroservice/main/diagram.jpg)](https://raw.githubusercontent.com/zahrasalimzadeh/NotificationMicroservice/main/diagram.jpg)

[Open the interactive diagram | باز کردن نمودار تعاملی](https://zahrasalimzadeh.github.io/NotificationMicroservice/diagram.html)

1. After a successful login, CoreBanking generates a verification code.
2. It publishes the message (`phone`, `content`) to RabbitMQ through `NotificationPublisher`.
3. [NotificationMicroservice](https://github.com/zahrasalimzadeh/NotificationMicroservice) consumes the message and sends the SMS to sms.ir.
4. The user enters the code, and CoreBanking validates it and opens the home page.

<div dir="rtl">

1. بعد از ورود موفق، CoreBanking یک کد تأیید می‌سازد.
2. پیام (`phone` و `content`) را با `NotificationPublisher` در RabbitMQ منتشر می‌کند.
3. [NotificationMicroservice](https://github.com/zahrasalimzadeh/NotificationMicroservice) پیام را برمی‌دارد و پیامک را به sms.ir می‌فرستد.
4. کاربر کد را وارد می‌کند و CoreBanking آن را بررسی می‌کند و صفحه‌ی اصلی را باز می‌کند.

</div>

---

# 📈 Monitoring | پایش عملکرد

Every function decorated with `@performance_logger` is measured on each call. The result goes to two places: a SQL Server table (the log) and Prometheus (the metrics). Grafana reads the metrics from Prometheus and shows them in a dashboard.

<div dir="rtl">

هر تابعی که با `@performance_logger` علامت‌گذاری شده باشد در هر بار اجرا اندازه‌گیری می‌شود. نتیجه در دو جا ثبت می‌شود: یک جدول در SQL Server (لاگ) و Prometheus (متریک‌ها). Grafana متریک‌ها را از Prometheus می‌خواند و در یک داشبورد نشان می‌دهد.

</div>

[![Monitoring diagram](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/9.png)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/9.png)

## 1. Database log | لاگ در پایگاه داده

The decorator lives in `Common/Decorators/performance_logger.py` and the table model in `DataAccess/Models/performance_logger.py`. The table is created automatically on the first run (`Base.metadata.create_all`).

<div dir="rtl">

دکوراتور در `Common/Decorators/performance_logger.py` و مدل جدول در `DataAccess/Models/performance_logger.py` قرار دارد. جدول در اولین اجرا به‌صورت خودکار ساخته می‌شود.

</div>

| Column / ستون    | Type / نوع       | Description / توضیح                |
|------------------|------------------|------------------------------------|
| `id`             | int (PK)         | Auto-increment key / کلید خودکار   |
| `function_name`  | nvarchar(100)    | Name of the function / نام تابع    |
| `execution_time` | numeric(18, 10)  | Execution time in seconds / زمان اجرا به ثانیه |
| `call_date_time` | datetime         | When it was called / زمان فراخوانی |

Example functions that are measured: `login_button_clicked` and `get_by_username_password`.

<div dir="rtl">

نمونه توابعی که اندازه‌گیری می‌شوند: `login_button_clicked` و `get_by_username_password`.

</div>

## 2. Prometheus metrics | متریک‌های Prometheus

`main.py` starts a metrics server with `start_http_server(8000)`. While the application is running, the metrics are available at `http://127.0.0.1:8000/metrics`.

<div dir="rtl">

فایل `main.py` یک سرور متریک با `start_http_server(8000)` راه‌اندازی می‌کند. تا وقتی برنامه روشن است، متریک‌ها در آدرس `http://127.0.0.1:8000/metrics` در دسترس هستند.

</div>

| Metric / متریک                              | Type / نوع | Description / توضیح                              |
|---------------------------------------------|------------|--------------------------------------------------|
| `app_function_calls_total`                  | Counter    | Number of calls per function / تعداد فراخوانی هر تابع |
| `app_function_duration_seconds`             | Histogram  | Execution time distribution / توزیع زمان اجرا    |
| `app_function_last_duration_seconds`        | Gauge      | Execution time of the last call / زمان اجرای آخرین فراخوانی |
| `app_function_last_call_timestamp_seconds`  | Gauge      | Unix time of the last call / زمان آخرین فراخوانی |

Every metric has a `function` label with the function name.

<div dir="rtl">

هر متریک یک برچسب `function` با نام تابع دارد.

</div>

Save this as `prometheus.yml` next to `prometheus.exe`, then run `prometheus.exe`:

<div dir="rtl">

این را با نام `prometheus.yml` کنار `prometheus.exe` ذخیره کنید و سپس `prometheus.exe` را اجرا کنید:

</div>

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "core_banking_app"
    static_configs:
      - targets: ["127.0.0.1:8000"]
```

Open `http://localhost:9090/targets`. Both `prometheus` and `core_banking_app` must be **UP**.

<div dir="rtl">

آدرس `http://localhost:9090/targets` را باز کنید. هر دو مورد `prometheus` و `core_banking_app` باید **UP** باشند.

</div>

## 3. Grafana dashboard | داشبورد Grafana

1. Open Grafana at `http://localhost:3000`.
2. Add a Prometheus data source with the URL `http://localhost:9090`.
3. Create a dashboard named **Core Banking Monitoring** with two panels:

| Panel                     | PromQL query                                    |
|---------------------------|-------------------------------------------------|
| **Function Calls**        | `sum by (function) (app_function_calls_total)`  |
| **Function Execution Time** | `app_function_last_duration_seconds`          |

<div dir="rtl">

1. Grafana را در `http://localhost:3000` باز کنید.
2. یک Data source از نوع Prometheus با آدرس `http://localhost:9090` اضافه کنید.
3. یک داشبورد با نام **Core Banking Monitoring** و دو پنل بالا بسازید.

</div>

---

# 🛠 Technologies Used | تکنولوژی‌های استفاده‌شده

- Python
- Tkinter
- ttkbootstrap
- SQLAlchemy
- SQL Server (pyodbc, pymssql)
- RabbitMQ (pika)
- python-dotenv
- Captcha (Pillow)
- Prometheus (prometheus_client)
- Grafana
- Layered Architecture
- Microservice Architecture

---

# 📂 Project Structure | ساختار پروژه

```
CoreBanking/
│
├── BusinessLogic/
│   └── user_business_logic.py
│
├── Common/
│   ├── Decorators/
│   │   └── performance_logger.py
│   ├── DTOs/
│   ├── Entities/
│   ├── Enums/
│   ├── Repositories/
│   └── Services/
│       ├── notification_publisher.py
│       └── sms_service.py
│
├── DataAccess/
│   ├── Config/
│   ├── Models/
│   │   └── performance_logger.py
│   └── Repositories/
│
├── Presentation/
│   ├── Component/
│   ├── Frames/
│   │   ├── login.py
│   │   ├── register.py
│   │   ├── otp.py
│   │   ├── home.py
│   │   └── profile.py
│   ├── main_view.py
│   └── window.py
│
├── .env.example
├── .gitignore
├── CreateDatabase.sql
├── main.py
└── requirements.txt
```

| Layer / لایه    | Responsibility                                  | وظیفه                                         |
|-----------------|-------------------------------------------------|-----------------------------------------------|
| `Presentation`  | Tkinter windows and frames                      | پنجره‌ها و صفحه‌های Tkinter                   |
| `BusinessLogic` | Login, registration and validation rules        | قوانین ورود، ثبت‌نام و اعتبارسنجی             |
| `DataAccess`    | SQLAlchemy models and repositories              | مدل‌ها و ریپازیتوری‌های SQLAlchemy            |
| `Common`        | Entities, enums, DTOs, decorators, shared services | موجودیت‌ها، Enum ها، DTO ها، دکوراتورها و سرویس‌های مشترک |

---

# 🔐 Roles | نقش‌ها

| Role          | Home page options                       | گزینه‌های صفحه‌ی اصلی             |
|---------------|-----------------------------------------|-----------------------------------|
| Administrator | Employee Management, My Profile, Logout | مدیریت کارمندان، پروفایل من، خروج |
| Banker        | Account Management, My Profile, Logout  | مدیریت حساب‌ها، پروفایل من، خروج  |

---

# ⚙️ Environment Variables | متغیرهای محیطی

Copy `.env.example` to `.env` and fill in the values. The `.env` file is ignored by Git and must never be uploaded.

<div dir="rtl">

فایل `.env.example` را به `.env` کپی کنید و مقدارها را پر کنید. فایل `.env` توسط Git نادیده گرفته می‌شود و هرگز نباید آپلود شود.

</div>

| Variable                | Description                                           | توضیح                                                      |
|-------------------------|-------------------------------------------------------|------------------------------------------------------------|
| `DB_SERVER`             | SQL Server address                                    | آدرس SQL Server                                            |
| `DB_NAME`               | Database name                                         | نام پایگاه داده                                            |
| `DB_USERNAME`           | Database username                                     | نام کاربری پایگاه داده                                     |
| `DB_PASSWORD`           | Database password                                     | رمز عبور پایگاه داده                                       |
| `DB_DRIVER`             | ODBC driver used by pyodbc, installed on your machine | نام ODBC Driver نصب‌شده روی سیستم که pyodbc استفاده می‌کند |
| `RABBITMQ_HOST`         | RabbitMQ server address                               | آدرس سرور RabbitMQ                                         |
| `RABBITMQ_PORT`         | RabbitMQ port (5672)                                  | پورت RabbitMQ (معمولاً 5672)                               |
| `RABBITMQ_USERNAME`     | RabbitMQ username                                     | نام کاربری RabbitMQ                                        |
| `RABBITMQ_PASSWORD`     | RabbitMQ password                                     | رمز عبور RabbitMQ                                          |
| `RABBITMQ_VIRTUAL_HOST` | RabbitMQ virtual host                                 | Virtual Host در RabbitMQ                                   |
| `SMSIR_API_KEY`         | sms.ir API key                                        | کلید API سایت sms.ir                                       |
| `SMSIR_LINE_NUMBER`     | sms.ir line number                                    | شماره‌ی خط sms.ir                                          |

---

# 🚀 How To Run | نحوه اجرا

Make sure SQL Server and RabbitMQ are installed and running, then clone the repository:

<div dir="rtl">

مطمئن شوید SQL Server و RabbitMQ نصب و روشن هستند، سپس پروژه را کلون کنید:

</div>

```
git clone https://github.com/zahrasalimzadeh/CoreBanking.git
```

Open the project folder:

```
cd CoreBanking
```

Install the requirements:

```
pip install -r requirements.txt
```

Create the database by running `CreateDatabase.sql` in SQL Server Management Studio. The `performance_logger` table is created automatically on the first run.

<div dir="rtl">

پایگاه داده را با اجرای فایل `CreateDatabase.sql` در SQL Server Management Studio بسازید. جدول `performance_logger` در اولین اجرا به‌صورت خودکار ساخته می‌شود.

</div>

Create your `.env` file from the example and fill in the values:

```
copy .env.example .env
```

Start the [NotificationMicroservice](https://github.com/zahrasalimzadeh/NotificationMicroservice) (it must be running to deliver the SMS), then run the application:

<div dir="rtl">

میکروسرویس [NotificationMicroservice](https://github.com/zahrasalimzadeh/NotificationMicroservice) را اجرا کنید (برای ارسال پیامک باید روشن باشد)، سپس برنامه را اجرا کنید:

</div>

```
python main.py
```

To see the monitoring part, also start Prometheus (`prometheus.exe`) and Grafana, as described in the [Monitoring](#-monitoring--پایش-عملکرد) section.

<div dir="rtl">

برای دیدن بخش پایش، Prometheus (`prometheus.exe`) و Grafana را هم طبق بخش [پایش عملکرد](#-monitoring--پایش-عملکرد) اجرا کنید.

</div>

---

# 🎥 Demo | دمو

### 📸 Screenshots | تصاویر

**1. Login page with captcha | صفحه‌ی ورود با کپچا**

[![Login](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/1.jpg)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/1.jpg)

**2. Verification code page | صفحه‌ی وارد کردن کد تأیید**

[![OTP](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/2.jpg)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/2.jpg)

**3. Registration page | صفحه‌ی ثبت‌نام**

[![Register](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/3.jpg)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/3.jpg)

**4. Administrator home page | صفحه‌ی اصلی مدیر**

[![Administrator home](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/4.png)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/4.png)

**5. Banker home page | صفحه‌ی اصلی بانکدار**

[![Banker home](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/5.png)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/5.png)

**6. Logs saved in the `performance_logger` table | لاگ‌های ذخیره‌شده در جدول `performance_logger`**

[![Database log](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/6.png)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/6.png)

**7. Prometheus targets (both UP) | Targetهای Prometheus (هر دو UP)**

[![Prometheus targets](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/7.png)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/7.png)

**8. Grafana dashboard | داشبورد Grafana**

[![Grafana dashboard](https://github.com/zahrasalimzadeh/CoreBanking/raw/main/8.png)](https://github.com/zahrasalimzadeh/CoreBanking/blob/main/8.png)

### 🎬 Videos | ویدیوها

The demo videos are published on LinkedIn:

<div dir="rtl">

ویدیوهای دمو در LinkedIn منتشر شده‌اند:

</div>

| Video                                       | ویدیو                            | Link                                                                                           |
|---------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------|
| Architecture diagram                        | نمودار معماری                    | [Watch on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7516609310831845376/) |
| Login and waiting for the verification code | ورود و منتظر ماندن برای کد تأیید | [Watch on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7516609963180367874/) |
| Receiving the code                          | دریافت کد                        | [Watch on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7516611332004061185/) |
| Home page after verification                | صفحه‌ی اصلی بعد از تأیید         | [Watch on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7516611776558301184/) |

---

# 📝 Notes | نکات

- The verification SMS is delivered by the NotificationMicroservice through sms.ir. An sms.ir account with enough credit is required to receive the real SMS.
- The queue and exchange names must be the same in CoreBanking and in the NotificationMicroservice.
- The metrics endpoint (port 8000) only exists while the application is running. When the application is closed, the `core_banking_app` target in Prometheus becomes DOWN. This is expected.

<div dir="rtl">

- پیامک تأیید توسط NotificationMicroservice و از طریق sms.ir ارسال می‌شود. برای دریافت پیامک واقعی، حساب sms.ir باید اعتبار کافی داشته باشد.
- نام Exchange و Queue باید در CoreBanking و NotificationMicroservice یکسان باشد.
- آدرس متریک‌ها (پورت 8000) فقط تا وقتی برنامه روشن است وجود دارد. وقتی برنامه بسته شود، target با نام `core_banking_app` در Prometheus به حالت DOWN می‌رود. این رفتار طبیعی است.

</div>

---

# 👩‍💻 Developer | توسعه‌دهنده

**Zahra Salimzadeh**

- LinkedIn: [https://www.linkedin.com/in/zahra-salimzadeh-5767582ab/](https://www.linkedin.com/in/zahra-salimzadeh-5767582ab/)
- Email: zahrasalimzadeh7@gmail.com
