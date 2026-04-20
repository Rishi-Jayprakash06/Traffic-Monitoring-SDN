# Traffic Monitoring and Statistics Collector

## Problem Statement
Build a controller module that collects and displays traffic statistics.

## Objective
This project uses SDN (Software Defined Networking) with POX controller and Mininet to monitor and control network traffic.

## Features
- Packet and byte counting
- Periodic monitoring
- Traffic blocking (h1)
- Flow-based control

## Setup
1. Install Mininet
2. Clone POX
3. Run controller:
   ./pox.py traffic_monitor
4. Run Mininet:
   sudo mn --topo single,3 --controller remote

## Testing
- pingall (normal traffic)
- h1 ping h2 (blocked traffic)

## Output
- Controller logs show packet and byte stats
- Traffic from h1 is blocked
