# This file includes overrides to build the `development` environment for the LMS starting from the
# settings of the `production` environment

from docker_run_production import *
from .utils import Configuration

# Load custom configuration parameters from yaml files
config = Configuration(os.path.dirname(__file__))

DEBUG = True
REQUIRE_DEBUG = True

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

PIPELINE_ENABLED = False
STATICFILES_STORAGE = "openedx.core.storage.DevelopmentStorage"

ALLOWED_HOSTS = ["*"]

WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

# configurable-lti-consumer sample configuration
CONFIGURABLE_XBLOCKS_SETTINGS = {
    "components": [{
        "module": "lti_consumer",
        "base_class": "ConfigurableLtiConsumerXBlock",
        "subclasses": [{
            "name": "Video",
            "display": "Video LTI xblock",
            "lti": {
                "key": "jisc.ac.uk",
                "secret": "secret",
            },
            "default_values": {
                "description": "Video",
                "lti_id": "",
                "launch_target": "iframe",
                "launch_url": "http://ltiapps.net/test/tp.php",
                "custom_parameters": [],
                "button_text": "button",
                "inline_height": 800,
                "modal_height": 800,
                "modal_width": 80,
                "has_score": False,
                "weight": 0,
                "hide_launch": False,
                "accept_grades_past_due": False,
                "ask_to_send_username": True,
                "ask_to_send_email": True

            }
        },{
            "name": "Generic",
            "display": "Generic LTI xblock",
            "default_values": {
                "description": "Generic",
                "ask_to_send_username": True,
                "ask_to_send_email": True
            }
        }]
    }]
}
