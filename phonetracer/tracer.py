import phonenumbers
from phonenumbers import geocoder
import time
import random

def start_phone_tracer(target):
    print("[+] PhoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print("[*] Initiating trace...")
    time.sleep(1)  # Added for dramatic effect
    
    try:
        # Parse the phone number
        p = phonenumbers.parse(target, None)
        
        # Get the location description (region info)
        location = geocoder.description_for_number(p, "en")
        
        print(f"[+] Country/Region: {location}")
        
        # Additional checks could be added here
        print("[+] Trace complete")

    except phonenumbers.NumberParseException as e:
        print(f"[!] Error: {e}")
        print("[!] Please enter a valid phone number in international format (e.g., +12125551234)")

# Example usage
if _name_ == "_main_":
    print("Phone Number Tracer")
    print("-------------------")
    phone_number = input("Enter phone number in international format (e.g., +12125551234): ")
    start_phone_tracer(phone_number)
