from .ac_repair import ACRepairService
from .fridge_repair import FridgeRepairService
from .oven_repair import OvenRepairService
from .washing_machine import WashingMachineService


# Service factory function
def get_service(service_type):
    services = {
        "ac_repair": ACRepairService(),
        "fridge_repair": FridgeRepairService(),
        "oven_repair": OvenRepairService(),
        "washing_machine": WashingMachineService()
    }
    
    return services.get(service_type, None)
