# PMU Data Extraction and Analysis from PCAP Files

## 📌 Overview
This project implements a **Python-based PMU (Phasor Measurement Unit) data extraction and analysis tool** using packet capture (`.pcap`) files recorded with Wireshark. The script parses raw network packets, decodes IEEE-754 floating-point measurement values, converts rectangular phasor data into polar form, and exports structured time-series data for offline analysis.

The tool was developed to support **smart-grid cybersecurity and power-systems research**, enabling analysis of voltage, current, frequency, and ROCOF (Rate of Change of Frequency) data from simulated power-grid environments.

---

## 🎯 Project Objectives
- Extract PMU measurement data from raw network packets
- Decode binary IEEE-754 floating-point values from packet payloads
- Convert phasor data from rectangular to polar representation
- Organize PMU measurements into structured tabular form
- Export processed data for visualization and cybersecurity analysis

---

## ⚙️ Technologies Used
- **Python 3**
- **Scapy** – packet capture parsing
- **Pandas** – data organization and export
- **NumPy** – numerical computation
- **Struct** – binary data unpacking
- **Wireshark** – PCAP capture generation

---
## 🧠 Processing Pipeline

### 1. Packet Capture Loading
- Loads PCAP files using `scapy.rdpcap()`
- Iterates through a defined packet range containing PMU data

### 2. Raw Data Conversion
- Extracts raw byte payloads from packets
- Identifies PMU packets using a source identifier
- Combines four bytes into IEEE-754 floating-point values
- Converts hexadecimal payloads into signed floating-point measurements

### 3. Phasor Conversion
Rectangular phasor components are converted into polar form:

**Magnitude**
\[
\rho = \sqrt{x^2 + y^2}
\]

**Angle**
\[
\phi = \arctan2(y, x)
\]

Angle values are reported in degrees.

### 4. Data Structuring
- Builds a Pandas `DataFrame` for time-series PMU data
- Appends decoded measurements packet-by-packet
- Ensures consistent formatting for offline analysis

### 5. Data Export
- Writes processed PMU data to CSV format
- Enables post-processing in Python, MATLAB, Excel, or visualization tools

---

## 📊 Output Data Fields

| Column Name        | Description |
|-------------------|-------------|
| Packet            | Packet index in PCAP file |
| Voltage Mag       | Voltage phasor magnitude |
| Voltage Angle     | Voltage phasor angle (degrees) |
| Current Mag       | Current phasor magnitude |
| Current Angle     | Current phasor angle (degrees) |
| Actual Frequency  | Measured system frequency |
| ROCOF             | Rate of change of frequency |

## 📚 Learning Outcomes
This project demonstrates:
- Network packet analysis using Scapy
- Binary decoding and endianness handling
- IEEE-754 floating-point interpretation
- Phasor mathematics and signal representation
- Data engineering for cyber-physical systems
- Power-system measurement analysis
- Automation of PMU data extraction workflows
- Applied cybersecurity analysis in smart-grid environments

## 🚀 Future Enhancements
- Support for multiple PMU identifiers
- Dynamic packet filtering based on protocol headers
- Real-time packet streaming and live analysis
- Visualization dashboards (Matplotlib / Plotly)
- Integration with anomaly detection algorithms
- Automated detection of spoofing or data-manipulation attacks
- Export to additional formats (Excel, SQL databases)

## 📄 License
Educational and research use only.

## 👥 Authors
Developed as part of undergraduate research in smart-grid cybersecurity.
Maintained for academic and professional portfolio use.
