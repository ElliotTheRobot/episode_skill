from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'heinzdonnellyschmidt'

LOGGER = getLogger(__name__)


class EpisodesSkill(MycroftSkill):
    def __init__(self):
        super(EpisodesSkill, self).__init__(name="EpisodesSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        episode_intent = IntentBuilder("EpisodesIntent").\
             require("PlayKeyword"). \
             require("EpisodeKeyword").\
             require("EpisodeNumber").build()

        self.register_intent(episode_intent, self.handle_episode_intent)

    def handle_episode_intent(self, message):
        word = message.data.get("EpisodeNumber")
        self.speak("Playing episode " + word)

    def stop(self):
        pass


def create_skill():
    return EpisodesSkill()