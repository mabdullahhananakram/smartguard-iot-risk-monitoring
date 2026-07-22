# SmartGuard IoT Risk Monitoring System

SmartGuard is a simulation-based IoT monitoring and alert system designed to demonstrate real-time sensor communication, MQTT messaging, risk classification, and dashboard-based monitoring.

The project simulates an ESP32-connected sensor system that monitors environmental and security conditions such as temperature, humidity, motion, and air quality.

## Project Overview

The system includes:

- A Python-based DHT11 sensor simulator
- Simulated UART sensor communication
- An MQTT publisher simulator
- MQTT topics and QoS demonstrations
- A live HTML, CSS, and JavaScript dashboard
- Threshold-based risk classification
- Automated warnings and critical alerts
- Active alert history
- Alarm acknowledgement and mute controls

## System Architecture

```text
DHT11 Sensor Simulator
        |
        | UART-style sensor data
        v
ESP32 / MQTT Publisher Simulator
        |
        | MQTT messages
        v
SmartGuard Monitoring Dashboard
        |
        v
Risk Classification and Alerts
