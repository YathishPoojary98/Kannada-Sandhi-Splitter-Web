# 🌐 Kannada Sandhi Splitter Web Application

This repository contains a **Flask-based web application** for **Kannada Sandhi Splitting**. It allows users to input Kannada words, process them for **Sandhi splitting**, and provide feedback on the results.

---

## 🚀 Features

✅ **Kannada Sandhi Splitting** – Uses a **Sandhi splitting algorithm** to process Kannada words.  
✅ **User Authentication** – Uses **session management** for user login/logout.  
✅ **Feedback Collection** – Users can provide corrections and feedback to improve the model.  
✅ **Web-Based UI** – Built using **Flask** with **HTML templates** for interaction.  
✅ **Cross-Origin Support** – CORS enabled for seamless requests.

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YathishPoojary98/Kannada-Sandhi-Splitter-Web.git
```
Navigate into the cloned directory:
```bash
cd Kannada-Sandhi-Splitter-Web/Kannada-Sandhi-Splitter-Web/Web
```

### 2️⃣ Install Dependencies
Install the required Python packages:
```bash
pip install flask flask-session flask-cors
```

### 3️⃣ Run the Application
Start the Flask server:
```bash
python app.py
```

The application will run on `http://0.0.0.0:<port>`.

---

## 🎮 How to Use

1️⃣ **Login** – Enter your **name and institution** to start using the application.  
2️⃣ **Enter Kannada Word** – Input a Kannada word for **Sandhi splitting**.  
3️⃣ **View Results** – The system will display **split components** of the input word.  
4️⃣ **Provide Feedback** – Users can correct or confirm the Sandhi splitting results.  
5️⃣ **Logout** – Clear session data and return to login page.

---

## 📂 Repository Structure

```
Kannada-Sandhi-Splitter-Web/Kannada-Sandhi-Splitter-Web/Web/
│── app.py                    # Flask application
│── templates/
│   ├── index.html            # Home page
│   ├── login.html            # User login page
│   ├── result.html           # Displays Sandhi split results
│   ├── feedback.html         # Collects user feedback
│   ├── out.html              # Stores feedback submissions
│── static/                   # Static files (CSS, JS, images)
│── Splitter/
│   ├── correct_sandhi_mod.py # Sandhi splitting logic
│   ├── utf2wx.py             # UTF to WX conversion
│── feedbacks.txt             # Stores user feedback
│── correctoutputs.txt        # Stores correct split outputs
```

---

## 🎯 API Endpoints

### `/` → Home Page
Redirects users to **login** if not authenticated.

### `/login` → User Login
Allows users to enter their **name and institution**.

### `/logout` → Logout
Clears session data and redirects to login.

### `/result` → Sandhi Splitting
- Accepts Kannada word input.
- Processes word using `sandhi_splitter`.
- Displays **split results** and **Sandhi rule used**.

### `/feedback` → Collects Feedback
- Accepts corrections from users.
- Stores feedback in `feedbacks.txt`.

### `/out` → Stores Correct Outputs
- Saves correct split words and Sandhi rules.
- Stores data in `correctoutputs.txt`.

---
