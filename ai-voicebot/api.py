import enum
from typing import Annotated

from livekit.agents import llm
import logging

logger =  logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

class Zone(enum.Enum):
    LIVING_ROOM = 'living_room'
    BEDROOM = 'bedroom'
    KITCHEN = 'kitchen'
    BATHROOM = 'bathroom'
    OFFICE = 'office'

class AssistantFnc(llm.FunctionContext):

    def __init__(self) -> None:
        super().__init__()

        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21
        }

    @llm.ai_callable(description="get the temperature in a specific room")
    def get_temperature(self, zone: Annotated[Zone, llm.TypeInfo(description= "The specific Zone")]):
        logger.info("get temp - zone %s", zone)
        temp =  self._temperature[Zone(zone)]
        return f"the temprature in the {zone} is {temp}C"

    @llm.ai_callable(description ="set the temprature in a specific room")
    def set_temperature(
        self, 
        zone: Annotated[Zone, llm.TypeInfo(description= "The specific Zone")], 
        temp: Annotated[int, llm.TypeInfo(description = " The temprature to set")]
        ):
        logger.info("set temp - zone %s", zone, temp)
        self._temperature[Zone(zone)] = temp
        return f"the temprature in the {zone} is now {temp}C"

    