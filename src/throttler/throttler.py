class Throttler(object):

    def __init__(self):
        self._login_attempts = {}

    def add_login_attempt(self, login_attempt):
        if not self.previous_entry_exists_for(login_attempt):
            self.set_initial_empty_list_for(login_attempt)
        self.remember(login_attempt)

    def remember(self, login_attempt):
        self._login_attempts[login_attempt.identifier].append(login_attempt)

    def set_initial_empty_list_for(self, login_attempt):
        self._login_attempts[login_attempt.identifier] = []

    def add_login_attempts(self, login_attempts):
        for login_attempt in login_attempts:
            self.add_login_attempt(login_attempt)

    def get_total_number_of_login_attempts(self):
        return sum(map(len, self._login_attempts.values()))

    def previous_entry_exists_for(self, login_attempt):
        return self._login_attempts.has_key(login_attempt.identifier)

    def previous_entries_for(self, login_attempt):
        if self.previous_entry_exists_for(login_attempt):
            return self._login_attempts[login_attempt.identifier]
        return []

    def get_number_of_similar_attempts_for(self, login_attempt):
        return len(self.previous_entries_for(login_attempt))
