import os
import logging
import logging.config

logger = logging.getLogger(__name__)
logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'logging.conf'))
