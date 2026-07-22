"""
SmartGuard - MQTT Publisher Simulator
Simulates MQTT communication for IoT device
"""

import json
import time
from datetime import datetime

class MQTTClientSimulator:
    def __init__(self, client_id="ESP32_001"):
        self.client_id = client_id
        self.broker = "test.mosquitto.org"
        self.port = 1883
        self.is_connected = False
        self.message_id = 0
        
        # MQTT topics
        self.topics = {
            'sensor': f"smartguard/{client_id}/sensors",
            'alert': f"smartguard/{client_id}/alerts",
            'status': f"smartguard/{client_id}/status"
        }
        
        print("\n" + "="*60)
        print("MQTT CLIENT SIMULATOR INITIALIZED")
        print("="*60)
        print(f"Client ID: {client_id}")
        print(f"Broker: {self.broker}:{self.port}")
        print(f"Protocol: MQTT v5")
        print("="*60 + "\n")
    
    def connect(self):
        """Simulate MQTT connection"""
        print("\n🔌 MQTT CONNECTION SEQUENCE")
        print("  Step 1: Establishing TCP connection...")
        time.sleep(0.5)
        print("  Step 2: Sending CONNECT packet...")
        time.sleep(0.5)
        print("  Step 3: Setting Last Will and Testament...")
        time.sleep(0.5)
        print("  Step 4: Receiving CONNACK from broker...")
        time.sleep(0.5)
        
        self.is_connected = True
        print("\n  ✅ MQTT Connected successfully!")
        print(f"     Client: {self.client_id}")
        print(f"     Broker: {self.broker}")
        print(f"     Keep Alive: 60 seconds")
        print(f"     Clean Session: True")
        print(f"     LWT Topic: {self.topics['status']}")
        print(f"     LWT Message: offline")
        
        return True
    
    def publish(self, topic, data, qos=1):
        """Simulate MQTT publish"""
        if not self.is_connected:
            print("❌ Not connected to broker")
            return False
        
        self.message_id += 1
        
        print(f"\n📤 MQTT PUBLISH (Message ID: {self.message_id})")
        print(f"  Topic: {topic}")
        print(f"  QoS Level: {qos}")
        
        # Show QoS explanation
        if qos == 0:
            print("  ├─ QoS 0: At most once (fire and forget)")
        elif qos == 1:
            print("  ├─ QoS 1: At least once (acknowledged)")
            print("  ├─ Sending PUBLISH packet...")
            time.sleep(0.3)
            print("  ├─ Waiting for PUBACK...")
            time.sleep(0.3)
            print("  └─ ✓ PUBACK received")
        elif qos == 2:
            print("  ├─ QoS 2: Exactly once (four-way handshake)")
        
        # Show payload
        print(f"\n  Payload ({len(json.dumps(data))} bytes):")
        print(f"  {json.dumps(data, indent=2)}")
        print(f"\n  ✅ Published successfully")
        
        return self.message_id
    
    def disconnect(self):
        """Simulate MQTT disconnect"""
        print("\n🔌 MQTT DISCONNECT")
        print("  Sending DISCONNECT packet...")
        time.sleep(0.3)
        print("  Closing TCP connection...")
        self.is_connected = False
        print("  ✅ Disconnected cleanly")

def main():
    print("\n" + "="*70)
    print("SMARTGUARD - MQTT COMMUNICATION SIMULATION")
    print("="*70)
    print("\nThis simulates an ESP32 publishing sensor data via MQTT")
    print("Press Ctrl+C to stop\n")
    
    # Create MQTT client
    mqtt = MQTTClientSimulator("ESP32_ROOM101")
    
    # Connect to broker
    mqtt.connect()
    
    try:
        # Publish 3 sensor readings
        for i in range(1, 4):
            print(f"\n{'='*50}")
            print(f"📡 TRANSMISSION #{i}")
            print(f"{'='*50}")
            
            # Generate sensor data
            sensor_data = {
                'device_id': mqtt.client_id,
                'timestamp': datetime.now().isoformat(),
                'temperature': round(22.5 + (i * 2.5), 1),
                'humidity': round(65 - (i * 4), 1),
                'battery': 85 - i,
                'rssi': -65 + i,
                'reading_id': i
            }
            
            # Check if this is an alert condition
            if sensor_data['temperature'] > 28:
                print("\n⚠️ ALERT CONDITION DETECTED!")
                sensor_data['alert'] = 'High temperature'
                sensor_data['severity'] = 'warning'
                mqtt.publish(mqtt.topics['alert'], sensor_data, qos=2)
            else:
                mqtt.publish(mqtt.topics['sensor'], sensor_data, qos=1)
            
            time.sleep(1.5)
        
        # Demonstrate Last Will
        print("\n" + "="*50)
        print("💀 LAST WILL AND TESTAMENT DEMONSTRATION")
        print("="*50)
        print("If device disconnects unexpectedly:")
        print(f"  Broker automatically publishes to: {mqtt.topics['status']}")
        print("  Message: {'status': 'offline', 'device': 'ESP32_ROOM101'}")
        print("  QoS: 1 | Retain: True")
        print("\n  This allows the system to detect offline devices instantly!")
        
    except KeyboardInterrupt:
        print("\n\nSimulation stopped by user")
    
    # Clean disconnect
    mqtt.disconnect()
    
    print("\n" + "="*70)
    print("MQTT SIMULATION COMPLETE")
    print("="*70)

if __name__ == "__main__":
    main()