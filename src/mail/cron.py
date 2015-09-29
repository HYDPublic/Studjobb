import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.database.engine import database
from src.database.schedueled_entry_repository import SchedueledEntryRepository 
from src.mail.schedueler import Schedueler

# Load the repository
schedueled_entry_repository = SchedueledEntryRepository(database)

# Load schedueler with schedueled entries from database
schedueled_entries = schedueled_entry_repository.findAll()
schedueler = Schedueler(schedueled_entries)

# Connect to the mail server
schedueler.connect()

# Run the schedueler
schedueler.run()

# Retrieve the schedueled entries that that were sent
schedueled_entries_that_were_sent = schedueler.schedueled_entries_that_were_sent

# Mark the sent mails as 'sent' in the database 
for schedueled_entry_that_were_sent in schedueled_entries_that_were_sent:
    schedueled_entry_repository.update(schedueled_entry_that_were_sent) 

# Finally disconnect from the mail server
schedueler.disconnect()
