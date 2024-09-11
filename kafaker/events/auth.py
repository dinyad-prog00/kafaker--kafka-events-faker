from datetime import datetime
import random
from faker import Faker
from kafaker.template import customer
from kafaker.model import EventModel, FromRepo,IdRepo
from kafaker.topic import TopicConfig
from kafaker.faker import KafkaEventsFaker
from kafaker.data import DataRepo
fake = Faker("fr_FR")
{

    'user',
    'user_agent',
    'device'  # mobile_web, desktop
    'type'  # user_unsuspended, password_reset_requested, user_unsuspended,login, signup_invalid_email_format, user_created,user_deleted,user_updated,signup,login_not_matching_password,password_changed,signup_not_compliant_password,user_suspended,user_updated, login_unknown_identifier, profile_lockout, login_matching_password, email_verified, login_successful_suspended_account, password_reset, authorization_refused, email_verified
    'auth_type'  # password, google, facebook, apple
    'host',
    'ip',
    'date'
    'id'
}

types = [
    'user_suspended',
    'user_unsuspended',
    'password_reset_requested',
    'password_reset',
    'password_changed',
    'login', 
    'signup', 
    'signup_invalid_email_format', 
    'user_created',
    'user_deleted',
    'user_updated',
    'login_not_matching_password', 
    'email_verified',
    'account_locked',
    'account_unlocked',
    'user_role_updated',
    'user_permissions_updated',
    'session_created',
    'session_expired',
    'session_terminated',
    'session_login_attempt',
    'session_login_success',
    'session_login_failure',
    'session_logout',
    'account_activated',
    'account_deactivated',
    'account_deleted',
    'account_updated',
    'account_linked',
    'account_unlinked',
    'password_policy_updated',
    '2fa_enabled',
    '2fa_disabled',
    'device_linked',
    'device_unlinked',
    'device_updated',
    'user_invited',
    'invitation_accepted',
    'invitation_rejected',
    'payment_processed',
    'payment_failed',
    'subscription_started',
    'subscription_canceled',
    'subscription_renewed',
    'invoice_generated',
    'invoice_paid',
    'credit_card_added',
    'credit_card_removed',
    'credit_card_updated',
    'profile_picture_changed',
    'profile_updated',
    'language_preference_updated',
    'timezone_preference_updated',
    'notification_settings_updated',
    'email_notification_enabled',
    'email_notification_disabled',
    'sms_notification_enabled',
    'sms_notification_disabled',
    'push_notification_enabled',
    'push_notification_disabled',
    'billing_information_updated',
    'billing_address_updated',
    'shipping_address_updated'
]

[
                'user_suspended',
                'user_unsuspended',
                'password_reset_requested',
                'password_reset',
                'password_changed',
                'login', 
                'signup', 
                'signup_invalid_email_format', 
                'user_created',
                'user_deleted',
                'user_updated',
                'login_not_matching_password', 
                'email_verified'
                ]





class KafkaUserAuthEvents(KafkaEventsFaker):
    def __init__(self, topic_name="user_auth",  bootstrap_servers='localhost:9092', nb_threads=3, start_times=[0, 2, 21], intervals=[5, 7, lambda: random.randint(1, 20)], console=True, polulate_id=False):

        auth = self.build_model()
        super().__init__(
            topics=[
                TopicConfig(topic_name, auth,
                            nb_threads=3,
                            start_times=[0, 2, 21],
                            intervals=[5, 7, lambda: random.randint(1, 20)])
            ],
            repositoies=[
                DataRepo("users", customer, 3000),
            ],
            bootstrap_servers=bootstrap_servers,
            console=console,
            polulate_id=polulate_id
        )

    def build_model(self):
        return EventModel({
            'user' : IdRepo("users"),
            'user_agent' : fake.user_agent,
            'device' : lambda: fake.random_element(elements=['mobile_web', 'mobile', 'web', 'desktop']),
            'host' : fake.hostname,
            'ip': fake.ipv4,
            'date' : lambda:  datetime.now().isoformat(timespec='milliseconds'),
            'auth_type' : lambda: fake.random_element(elements=['password', 'google', 'facebook', 'apple']),
            'type' : lambda: fake.random_element(elements=types),
        })
