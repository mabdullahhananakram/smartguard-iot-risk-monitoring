"""
SmartGuard - Sensor Simulator
Simulates DHT11 temperature/humidity sensor communication via UART
"""

import random
import time
from datetime import datetime

class DHTSensorSimulator:
    def __init__(self, sensor_id="SENSOR_001"):
        self.sensor_id = sensor_id
        self.temp_range = (18.0, 35.0)
        self.humidity_range = (40.0, 75.0)
        print("\n" + "="*50)
        print("UART SENSOR SIMULATOR STARTED")
        print("="*50)
        print(f"Sensor ID: {sensor_id}")
        print(f"Protocol: UART | Baud Rate: 9600 | 8N1")
        print("="*50 + "\n")
    
    def read_sensor(self):
        # Simulate sensor reading time
        time.sleep(1)
        
        # Generate random temperature between 20-30°C
        temperature = round(random.uniform(20.0, 32.0), 1)
        
        # Generate random humidity between 40-70%
        humidity = round(random.uniform(40.0, 70.0), 1)
        
        # Create UART frame simulation
        uart_frame = {
            'start_bit': 1,
            'data_bytes': [
                int(temperature),  # Temp integer
                int((temperature % 1) * 10),  # Temp decimal
                int(humidity),  # Humidity integer
                int((humidity % 1) * 10),  # Humidity decimal
            ],
            'stop_bit': 0
        }
        
        # Calculate checksum
        uart_frame['checksum'] = sum(uart_frame['data_bytes']) & 0xFF
        
        # Display UART communication
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] UART READ OPERATION")
        print(f"  TX ← RX: Requesting data from DHT11 sensor")
        print(f"  TX → RX: Sending 40-bit data frame")
        print(f"  └─ Start Bit: {uart_frame['start_bit']}")
        print(f"  └─ Data: Temp={temperature}°C, Humidity={humidity}%")
        print(f"  └─ Bytes: {uart_frame['data_bytes']}")
        print(f"  └─ Checksum: {uart_frame['checksum']} (0x{uart_frame['checksum']:02X})")
        print(f"  └─ Stop Bit: {uart_frame['stop_bit']}")
        print(f"  ✓ UART frame received and validated")
        
        return {
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': datetime.now().isoformat(),
            'sensor_id': self.sensor_id
        }

def main():
    print("\n" + "="*60)
    print("SMARTGUARD - UART SENSOR SIMULATION")
    print("="*60)
    print("\nThis simulates a DHT11 sensor connected via UART to ESP32")
    print("Press Ctrl+C to stop\n")
    
    sensor = DHTSensorSimulator("DHT11_001")
    
    try:
        reading_count = 0
        while reading_count < 5:  # Run 5 times
            reading_count += 1
            print(f"\n--- READING #{reading_count} ---")
            data = sensor.read_sensor()
            
            # Show data ready for MQTT
            print(f"\n  📊 DATA READY FOR MQTT PUBLISH:")
            print(f"     Topic: smartguard/room1/sensors")
            print(f"     Payload: {data}")
            print(f"     QoS: 1 | Retain: False")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\nSimulation stopped by user")
    
    print("\n" + "="*60)
    print("UART SIMULATION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()