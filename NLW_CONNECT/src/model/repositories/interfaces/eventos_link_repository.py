from abc import ABC, abstractmethod
from src.model.entities.eventos_link import EventosLink

class EventosLinkRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, event_id: int, subscriber_id: int) -> None:
       pass
    
    @abstractmethod
    def select_event_link(self, event_id: int, subscriber_id: int) -> EventosLink:
        pass