# Performance Analysis of Cloud Providers (AWS vs GCP)

Objective: This project aimed to analyze and compare the performance of two leading cloud service providers, Amazon Web Services (AWS) and Google Cloud Platform (GCP). The focus was on evaluating their capabilities in terms of CPU processing, latency, and throughput, with the goal of assisting users in making informed decisions when selecting a cloud provider for their specific needs.

Methodology:

- Cloud Environment Setup: The project utilized AWS (t2.medium) and GCP (e2-medium) instances to ensure a comparable testing environment.
- Performance Testing Framework: The Django framework was chosen for its ability to handle API requests and facilitate performance measurements.
- Load Testing Tool: JMeter, a widely used open-source load testing tool, was employed to simulate user traffic and measure response times under heavy loads.
- Data Collection and Analysis: Data collected during the testing process, including CPU usage, latency, and throughput, was stored in a SQLite database for further analysis. This allowed for comprehensive evaluation and comparison of the two cloud platforms.


Results:

The findings revealed that AWS outperformed GCP in terms of CPU processing and throughput, while GCP demonstrated slightly better latency and zero error rate. This information is crucial for users to consider when making choices based on their specific requirements and priorities.
