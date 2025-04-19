import os
import logging
import pywhatkit
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv
import pyautogui
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="WhatsApp Message Sender",
    description="A FastAPI application to send WhatsApp messages.",

)


MESSAGE_CONTENT = "Hello, this is a test message from our TMBC bot!"

def send_whatsapp_message(phone_number: str, message: str) -> bool:
   
    try:
        # Ensure phone number starts with '+' for international format
        if not phone_number.startswith('+'):
            phone_number = f'+{phone_number}'
        
        # Send message instantly
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
        pyautogui.press('enter')
        logger.info(f"Message sent successfully to {phone_number}")
        return True

    except Exception as e:
        logger.error(f"Error sending message to {phone_number}: {str(e)}")
        return False

@app.get("/send_message")
async def send_message_endpoint(
    phone_number: str = Query(...)
):
   
    logger.info(f"Received request to send message to: {phone_number}")

    # Basic phone number format check
    if not phone_number.strip() or not phone_number.replace('+', '').isdigit():
        logger.error(f"Invalid phone number format: {phone_number}")
        raise HTTPException(
            status_code=400,
            detail="Invalid phone number format. Use international format (e.g., +1234567890)."
        )

    success = send_whatsapp_message(
        phone_number=phone_number,
        message=MESSAGE_CONTENT
    )

    if success:
        logger.info(f"Successfully initiated message sending to {phone_number}")
        return {"status": "success", "message": "Message sending initiated successfully."}
    else:
        logger.error(f"Failed to send message to {phone_number}")
        raise HTTPException(
            status_code=500,
            detail="Failed to send WhatsApp message. Check server logs for details."
        )

@app.get("/")
async def root():
    return {"message": "WhatsApp Message Sender API is running."}