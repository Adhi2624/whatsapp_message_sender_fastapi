# WhatsApp Message Sender API

A FastAPI application for sending WhatsApp messages using `pywhatkit` and `pyautogui`. This API allows users to send predefined test messages to specified phone numbers via WhatsApp.

## Features
- Send WhatsApp messages instantly to international phone numbers.
- Basic phone number validation for international format.
- Logging for request tracking and error handling.
- Simple REST API with FastAPI.

## Prerequisites
- Python 3.8+
- WhatsApp account logged in on the system (via WhatsApp Web or desktop app).
- Required Python packages:
  - `fastapi`
  - `uvicorn`
  - `pywhatkit`
  - `pyautogui`

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/Adhi2624/whatsapp_message_sender_fastapi
   cd https://github.com/Adhi2624/whatsapp_message_sender_fastapi
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   - **Root Endpoint**: `GET /`
     - Returns a simple status message to confirm the API is running.
     - Example response:
       ```json
       {"message": "WhatsApp Message Sender API is running."}
       ```
   - **Send Message Endpoint**: `GET /send_message?phone_number=<phone_number>`
     - Sends a predefined test message to the specified phone number.
     - Phone number must be in international format (e.g., `+1234567890`).
     - Example request:
       ```bash
       curl "http://127.0.0.1:8000/send_message?phone_number=+1234567890"
       ```
     - Example success response:
       ```json
       {"status": "success", "message": "Message sending initiated successfully."}
       ```

3. **Access the API documentation**:
   - Open `http://127.0.0.1:8000/docs` in a browser for interactive Swagger UI.
   - Alternatively, use `http://127.0.0.1:8000/redoc` for ReDoc documentation.

## Configuration
- **Message Content**: The message sent is hardcoded as `"Hello, this is a test message from our TMBC bot!"`. Modify the `MESSAGE_CONTENT` variable in the code to change the message.
- **Logging**: Logs are configured to output at the `INFO` level. Check the console or configure a log file for debugging.

## Notes
- Ensure WhatsApp is logged in on the system, as `pywhatkit` uses WhatsApp Web or the desktop app to send messages.
- The application uses `pyautogui` to simulate an Enter key press to send the message, which may require the system to be active (not locked or minimized).
- Phone numbers must be in international format starting with `+` followed by digits only.
- The application does not support sending messages to WhatsApp groups or handling media attachments.

## Limitations
- Requires an active WhatsApp session on the system.
- Dependent on `pywhatkit` and `pyautogui`, which may have compatibility issues on some systems or environments.
- No support for customizing messages via the API (message is hardcoded).
- May fail if WhatsApp Web takes longer than the specified `wait_time` (default: 10 seconds) to load.

## Troubleshooting
- **Invalid phone number format**: Ensure the phone number is in international format (e.g., `+1234567890`).
- **Message not sent**: Check the server logs for errors. Common issues include:
  - WhatsApp not logged in.
  - Network issues preventing WhatsApp Web from loading.
  - `pyautogui` failing to press Enter (e.g., if the system is locked).
- **API not starting**: Verify all dependencies are installed and the Python environment is correctly set up.
