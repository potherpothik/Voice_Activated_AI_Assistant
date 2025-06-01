class WashingMachineService:
    def __init__(self):
        self.name = "Washing Machine Repair"
        self.description = "Repair services for washing machines addressing problems with spinning, draining, leaking, and unusual noises."
        self.common_issues = ["not spinning", "not draining", "leaking water", "making loud noises", "stuck on spin cycle"]
        self.price_range = "$85-$310"

    def get_info(self):
        return {
            "name": self.name,
            "description": self.description,
            "common_issues": self.common_issues,
            "price_range": self.price_range
        } 