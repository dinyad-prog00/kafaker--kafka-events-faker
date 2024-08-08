# Kafaker: Kafka Events Faker

Kafaker is a Python-based tool designed to simulate and generate events such as user orders, customer authentications, and more. It can send these events to Kafka brokers for testing and development purposes or display them on the console for quick analysis.

## Features

- **Multi-threaded Simulation**: Simulate multiple users and events in parallel.
- **Configurable Events**: Customize start times and intervals for events.
- **Kafka Integration**: Send events to Kafka brokers for real-world testing.
- **Console Output**: Display events in the console for easy inspection.
- **Custome Event Types**: Simulate various scenarios.

## Installation

To install Kafaker, clone this repository and install the required Python packages:

```bash
git https://github.com/dinyad-prog00/kafaker--kafka-events-faker.git
cd kafaker--kafka-events-faker
pip install -r requirements.txt
```

## Usage

You can start using Kafaker. Example (main.py, run: python main.py):

```python
from kafaker.events import KafkaOrderEvents,KafkaUserAuthEvents

kafkaf = KafkaUserAuthEvents(console=True)
#kafkaf = KafkaOrderEvents(console=False,polulate_id=True)
kafkaf.start()
```

## Configuration

Kafaker can be configured with various parameters:

- `topic_name`: The name of the Kafka topic or console category to which events will be sent.
- `bootstrap_servers`: A string representing the Kafka server(s) to connect to.
- `nb_threads`: The number of threads to use for parallel event generation.
- `start_times`: A list of start times for each thread.
- `intervals`: A list of intervals (in seconds) or functions returning intervals for event generation (ex: random).
- `console`: If `True`, events are displayed in the console; if `False`, they are sent to Kafka.
- `populate_id`: If `True`, each event is given a unique identifier.
- ...

## Example Output

Here is an example of the output you might see in the console when running Kafaker with the `console` option enabled:

```
Kafka events faker is started....

user_auth-1 ======================================

{
  "user": "YUGLzUkDkZsRMA5tDGwpZD",
  "user_agent": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS X) AppleWebKit/535.0 (KHTML, like Gecko) CriOS/18.0.805.0 Mobile/32S412 Safari/535.0",
  "device": "mobile_web",
  "host": "laptop-54.valentin.net",
  "ip": "142.219.241.136",
  "date": "2024-08-08T15:49:25.762",
  "auth_type": "apple",
  "type": "account_linked",
  "event_time": "2024-08-08T15:49:25.762"
}

user_auth-2 ======================================

{
  "user": "N3WbzmKxxmcSoe95B36ryw",
  "user_agent": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_5 like Mac OS X) AppleWebKit/535.2 (KHTML, like Gecko) FxiOS/16.4d1744.0 Mobile/54N033 Safari/535.2",
  "device": "web",
  "host": "db-18.pruvost.fr",
  "ip": "201.220.2.113",
  "date": "2024-08-08T15:49:27.763",
  "auth_type": "facebook",
  "type": "2fa_disabled",
  "event_time": "2024-08-08T15:49:27.763"
}

user_auth-1 ======================================

{
  "user": "mC3eMP5srU6VFEHHMQGCUw",
  "user_agent": "Mozilla/5.0 (Linux; Android 3.2.6) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/38.0.807.0 Safari/536.2",
  "device": "web",
  "host": "laptop-01.baron.com",
  "ip": "77.208.187.227",
  "date": "2024-08-08T15:49:30.762",
  "auth_type": "password",
  "type": "push_notification_disabled",
  "event_time": "2024-08-08T15:49:30.762"
}
```
