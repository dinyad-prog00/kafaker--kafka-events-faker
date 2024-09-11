from kafaker.events import KafkaOrderEvents,KafkaUserAuthEvents

#kafkaf = KafkaUserAuthEvents(console=True)
kafkaf = KafkaOrderEvents(console=False,polulate_id=True)
kafkaf.start()
