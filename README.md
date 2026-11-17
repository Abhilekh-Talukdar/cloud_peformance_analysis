# Performance Analysis of Cloud Providers (AWS vs GCP)

Objective: This project aimed to analyze and compare the performance of two leading cloud service providers, Amazon Web Services (AWS) and Google Cloud Platform (GCP). The focus was on evaluating their capabilities in terms of CPU processing, latency, and throughput, with the goal of assisting users in making informed decisions when selecting a cloud provider for their specific needs.

Methodology:

- Cloud Environment Setup: The project utilized AWS (t2.medium) and GCP (e2-medium) instances to ensure a comparable testing environment.
- Performance Testing Framework: The Django framework was chosen for its ability to handle API requests and facilitate performance measurements.
- Load Testing Tool: JMeter, a widely used open-source load testing tool, was employed to simulate user traffic and measure response times under heavy loads.
- Data Collection and Analysis: Data collected during the testing process, including CPU usage, latency, and throughput, was stored in a SQLite database for further analysis. This allowed for comprehensive evaluation and comparison of the two cloud platforms.

Results:

The findings revealed that AWS outperformed GCP in terms of CPU processing and throughput, while GCP demonstrated slightly better latency and zero error rate. This information is crucial for users to consider when making choices based on their specific requirements and priorities.

## Running the Django API safely

The Django signing key is no longer stored in source control. The key that was previously committed to this public repository must be treated as compromised; generate a replacement and rotate it in every deployment. Rotation invalidates existing Django sessions.

Required configuration:

- `DJANGO_SECRET_KEY`: a randomly generated secret, supplied through a deployment secret manager.
- `DJANGO_ALLOWED_HOSTS`: comma-separated hostnames served by the deployment. The default is limited to `localhost` and `127.0.0.1`; wildcard hosts are rejected.
- `DJANGO_DEBUG`: optional strict boolean (`true/false`, `1/0`, `yes/no`, or `on/off`). It defaults to `false`.
- `DJANGO_SQLITE_PATH`: optional SQLite database path. Relative paths are resolved from the project directory; the default is `db.sqlite3` in the project directory.

For local development, create a fresh key and explicitly enable debug mode:

```sh
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
export DJANGO_DEBUG=true
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
python manage.py runserver
```

For production, keep `DJANGO_DEBUG=false`, set `DJANGO_ALLOWED_HOSTS` to the actual service hostnames, provide the key through a secret manager, and terminate HTTPS at the application or trusted reverse proxy. Secure session and CSRF cookies are enabled automatically whenever debug mode is disabled.
