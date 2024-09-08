import bluetooth
import time

def scan_devices():
    print("Scanning for Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
    return devices

def send_bluetooth_message(target_address, message):
    try:
        port = 1  # Port généralement utilisé pour le RFCOMM
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, port))
        sock.send(message)
        sock.close()
        print(f"Message sent to {target_address}")
    except Exception as e:
        print(f"Failed to send message to {target_address}: {str(e)}")

# Simule l'envoi du message à tous les appareils détectés
def main():
    devices = scan_devices()
    if devices:
        print(f"Found {len(devices)} devices.")
        for addr, name in devices:
            print(f"Sending message to {name} ({addr})...")
            send_bluetooth_message(addr, "Simulated phone hack! Opening YouTube link in 5 seconds...")
            time.sleep(5)  # Pause de 5 secondes avant l'ouverture
    else:
        print("No Bluetooth devices found.")

if __name__ == "__main__":
    main()
