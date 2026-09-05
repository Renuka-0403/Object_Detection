# 🔍 Object Detection using AI

An AI-powered **object detection application built with Python, Streamlit, Hugging Face Transformers, and PIL** as part of the Generative AI task.

The application allows users to upload an image and use an AI object-detection model to identify objects present in the image.

> **Upload Image → AI Object Detection → Detected Objects**

---

## 📌 Overview

**Object Detection using AI** is an interactive web application that detects objects present in an uploaded image.

Users can upload an image in **JPG, JPEG, or PNG** format. The application displays the uploaded image and provides a **Detect** button. When the button is clicked, the AI model processes the image and returns the detected objects.

The application uses the **Hugging Face Transformers object-detection pipeline** and provides a simple interface through **Streamlit**.

---

## 🤖 Generative AI Creation

The application was developed with the assistance of **Generative AI** using a prompt-based development approach.

A natural-language prompt was provided describing the required:

* Image upload functionality
* Supported image formats
* Image display
* Object detection functionality
* Detect button
* Detection result display

Generative AI assisted in generating the application code.

The generated application was then executed using **Streamlit** and tested with uploaded images.

This demonstrates how Generative AI can assist in transforming a natural-language idea into a functional AI-powered application.

---

## ✨ Features

* 🔍 AI-powered object detection
* 📤 Image upload functionality
* 🖼️ Uploaded image preview
* 🤖 Hugging Face Transformers object-detection pipeline
* 🎯 Detect objects from uploaded images
* 📊 Display detection results
* 🖥️ Simple Streamlit interface
* 📁 Supports JPG, JPEG, and PNG images
* 🌐 Browser-based application

---

## 🧠 How It Works

The application follows a simple object-detection workflow:

```text
        📤 Upload Image
              ↓
      🌐 Streamlit Interface
              ↓
       🖼️ PIL Image Loading
              ↓
    🤗 Hugging Face Transformers
       Object Detection Pipeline
              ↓
       🔍 AI Object Detection
              ↓
        📊 Detection Results
              ↓
       🖥️ Display to User
```

### 🔍 Process Explanation

**1. Upload Image**

The user uploads an image in JPG, JPEG, or PNG format.

**2. Image Loading**

The uploaded image is opened and processed using **PIL (Python Imaging Library)**.

**3. Object Detection**

The image is passed to the Hugging Face Transformers object-detection pipeline.

**4. AI Processing**

The object-detection model analyzes the image and identifies objects present in it.

**5. Result Display**

The detected objects and their corresponding detection information are displayed in the Streamlit application.

---

## 🛠️ Tools & Technologies Used

| Tool / Technology             | Purpose                                     |
| ----------------------------- | ------------------------------------------- |
| **Python**                    | Application logic and implementation        |
| **Streamlit**                 | Interactive web application interface       |
| **Hugging Face Transformers** | Provides the object-detection pipeline      |
| **PIL / Pillow**              | Opens and processes uploaded images         |
| **AI Object Detection Model** | Detects objects in uploaded images          |
| **Generative AI**             | Assisted in generating the application code |
| **Web Browser**               | Running and testing the application         |

---

## 🤖 AI Model

The application uses the **Hugging Face Transformers object-detection pipeline**.

The pipeline is initialized using:

```python
detector = pipeline("object-detection")
```

The pipeline provides a convenient interface for performing object detection on an uploaded image.

The model analyzes the image and returns information about the objects identified.

---

## 💡 Prompt-Based Development

The development process followed these steps:

### 1. 💭 Idea

An idea for an AI-powered object-detection application was identified.

### 2. 📝 Prompt Creation

A natural-language prompt was created describing the required application functionality and interface.

### 3. 🤖 Generative AI

The prompt was provided to a Generative AI tool.

### 4. 💻 Application Generation

Generative AI assisted in generating the application code.

### 5. ▶️ Application Execution

The generated application was run using Streamlit.

### 6. 🧪 Testing

The application was tested by uploading images and running object detection.

---

## 🔄 Development Workflow

```text
       💭 Application Idea
              ↓
     📝 Natural-Language Prompt
              ↓
        🤖 Generative AI
              ↓
        💻 Generated Code
              ↓
       🌐 Streamlit Interface
              ↓
         📤 Image Upload
              ↓
       🔍 Object Detection
              ↓
       📊 Detection Results
```

---

## 🎮 How to Use

### Step 1 — Install the Required Libraries

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 2 — Run the Application

Run the following command:

```bash
streamlit run object_detector.py
```

### Step 3 — Upload an Image

Click the **Upload an image** button and select an image in JPG, JPEG, or PNG format.

### Step 4 — View the Uploaded Image

The uploaded image will be displayed in the application.

### Step 5 — Detect Objects

Click the **Detect** button to start the object-detection process.

### Step 6 — View Detection Results

The AI model processes the image and displays the detected objects and their detection information.

---

## 📦 Requirements

The main libraries required for this project are:

```text
streamlit
transformers
torch
pillow
```

Create a `requirements.txt` file containing:

```text
streamlit
transformers
torch
pillow
```

Then install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Testing

The application was tested to verify that its main functionality works correctly.

### Testing Checklist

* ✅ Application opens successfully
* ✅ Streamlit interface loads correctly
* ✅ Image upload works correctly
* ✅ JPG images are supported
* ✅ JPEG images are supported
* ✅ PNG images are supported
* ✅ Uploaded image is displayed
* ✅ Detect button works
* ✅ AI object detection is performed
* ✅ Detection results are displayed

---


## 📊 Application Details

| Feature                 | Details                   |
| ----------------------- | ------------------------- |
| 🔍 Application Type     | Object Detection          |
| 🖥️ Framework           | Streamlit                 |
| 🐍 Programming Language | Python                    |
| 🤖 AI Library           | Hugging Face Transformers |
| 🖼️ Image Library       | PIL / Pillow              |
| ✍️ Input                | Uploaded Image            |
| 📊 Output               | Detected Objects          |
| 📁 Supported Formats    | JPG, JPEG, PNG            |
| 🌐 Interface            | Web Application           |

---

## 🎯 Project Objective

The primary objective of this project is to demonstrate the practical use of **AI-based object detection** through an interactive application.

The project combines:

* 🤖 Generative AI-assisted development
* 🐍 Python
* 🌐 Streamlit
* 🤗 Hugging Face Transformers
* 🖼️ PIL / Pillow
* 🔍 AI-based object detection
* 🧪 AI application testing

The application demonstrates how an AI model can analyze an uploaded image and identify objects within it.

---

## 🌟 Key Learning

Through this project, the following concepts were explored:

* 🤖 Generative AI
* 🔍 Object detection
* 🖼️ Image processing
* 📝 Natural-language prompting
* 🐍 Python programming
* 🌐 Streamlit application development
* 🤗 Hugging Face Transformers
* 🧩 AI pipelines
* 🧪 Testing AI applications

---

## 💭 Generative AI Development Concept

Traditional application development can follow:

```text
Idea
  ↓
Requirements
  ↓
Manual Coding
  ↓
Testing
  ↓
Application
```

This project demonstrates an AI-assisted development approach:

```text
Idea
  ↓
Natural-Language Prompt
  ↓
Generative AI
  ↓
Generated Code
  ↓
Run Application
  ↓
Testing
  ↓
Working AI Application
```

This demonstrates how Generative AI can assist in accelerating the development and prototyping of AI-powered applications.

---

## 🚀 Project Outcome

The **Object Detection using AI** application was successfully created and tested as a functional image-analysis application.

The project demonstrates how an AI object-detection pipeline can be integrated into a Streamlit application to analyze uploaded images and return detected objects.

It also demonstrates how Generative AI can assist in converting natural-language requirements into working application code.

---

## 👤 Task Information

| Category                 | Details                          |
| ------------------------ | -------------------------------- |
| **Task**                 | Generative AI – Object Detection |
| **Application**          | Object Detection using AI        |
| **AI Library**           | Hugging Face Transformers        |
| **Framework**            | Streamlit                        |
| **Programming Language** | Python                           |
| **Image Processing**     | PIL / Pillow                     |
| **Development Approach** | Prompt-Based Development         |
| **Application Type**     | AI-Powered Web Application       |

---

## ⭐ Key Highlight

```text
       💡 IDEA
          ↓
       📝 PROMPT
          ↓
    🤖 GENERATIVE AI
          ↓
     💻 GENERATED CODE
          ↓
       🌐 STREAMLIT
          ↓
      📤 IMAGE INPUT
          ↓
     🔍 AI DETECTION
          ↓
      📊 RESULTS
```

## 📌 Conclusion

The **Object Detection using AI** project demonstrates the practical use of AI-based object detection through an interactive Streamlit application.

By integrating **Hugging Face Transformers**, **PIL**, and **Streamlit**, the project provides a simple interface for uploading images and obtaining object-detection results.

The project also demonstrates how Generative AI can assist in developing and prototyping AI-powered applications using natural-language instructions.

---

🔍 **Upload. Detect. Discover.**
