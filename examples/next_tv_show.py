import quizduell
import datetime

# Change to valid user id:
user_id = '...'

# Instantiate Quizduell TV API without TV auth token since we don't vote:
tv_api = quizduell.QuizduellTvApi(user_id)
state = tv_api.get_state()
print 'Next show:', datetime.datetime.fromtimestamp(state['Meta']['NextShowDate'])
