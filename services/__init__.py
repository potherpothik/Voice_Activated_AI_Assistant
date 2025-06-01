from .fridge_repair import FridgeRepairService
from .oven_repair import OvenRepairService
from .washing_machine import WashingMachineService

def get_service(service_name: str):
    """
    Get the appropriate service instance based on the service name.
    
    Args:
        service_name (str): Name of the service to get
        
    Returns:
        Service instance or None if service not found
    """
    services = {
        "fridge_repair": FridgeRepairService,
        "oven_repair": OvenRepairService,
        "washing_machine": WashingMachineService
    }
    
    service_class = services.get(service_name.lower())
    if service_class:
        return service_class()
    return None 