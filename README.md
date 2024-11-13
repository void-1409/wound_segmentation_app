
# Wound Detection App

This project consists of:
- A Python Flask server running a YOLOv8 segmentation model for wound detection (`server` folder).
- An Android app that captures an image, sends it to the server for processing, and displays the result (`app` folder).

## Prerequisites
- Python 3.8 or higher
- Android Studio (for app installation)
- An Android device with USB debugging enabled (if installing the app directly)
- The phone and laptop (server) should be connected to the **same Wi-Fi network**.

## Cloning the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/void-1409/wound_segmentation_app
cd wound_segmentation_app
```

## 1. Server Setup

### Step 1: Create and Activate a Virtual Environment

Navigate to the `server` folder and set up a Python virtual environment:

```bash
cd server
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 3: Start the Server

Run the Flask server:

```bash
python server.py
```

The server will start on `http://192.168.xxx.xxx:5000`. Note down this IP address of your laptop, as you will need it for the Android app setup.

## 2. Android App Installation

### Step 1: Update the Server IP

Open the `app` folder in Android Studio.

Replace the server IP address in the following two places:

- In `MainActivity.kt` (`SERVER_IP` variable).
- In `network_security_config.xml` (located in `res/xml/`).

Update both to match your server’s IP address (e.g., `http://192.168.xxx.xxx:5000`).

### Step 2: Install the App on Your Device

- Ensure USB Debugging is enabled on your Android device:
  - Go to **Settings** > **About Phone** > tap **Build Number** 7 times to enable Developer Options.
  - Go to **Settings** > **Developer Options** > enable **USB Debugging**.
- Connect your Android device to your laptop via USB.
- Click **Run** to install the APK on your device.

### Step 3: Run the App

- Launch the app on your device.
- Click the **Capture Image** button to take a photo and send it to the server for segmentation.

## Notes
- Make sure that your **phone** and **laptop (server)** are connected to the **same Wi-Fi network**.
- If you encounter a `CLEARTEXT communication not permitted` error, ensure that you have updated the IP address in `network_security_config.xml`.

## Troubleshooting

- **Cannot connect to the server**:
  - Verify that your server is running and accessible from your phone's browser (e.g., visit `http://192.168.0.107:5000`).
  - Check that both devices are on the same Wi-Fi network.

- **Camera permission denied**:
  - Go to your phone’s **Settings** > **Apps** > **Wound Predictor App** > **Permissions**, and grant camera permission.

- **Segmentation model not working**:
  - Ensure you have the correct model file (`best.pt`) in the `server` folder.
  - Verify that the Python dependencies are installed correctly.

## Acknowledgments
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Flask](https://flask.palletsprojects.com/)
- [Android Jetpack Compose](https://developer.android.com/jetpack/compose)
