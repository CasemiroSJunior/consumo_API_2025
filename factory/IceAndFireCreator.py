from ApiConsumeCreator import ApiCreator
from IceAndFire import IceAndFire

class IceAndFireCreator(ApiCreator):
    def create_api_consumer(self) -> IceAndFire:
        return IceAndFire()