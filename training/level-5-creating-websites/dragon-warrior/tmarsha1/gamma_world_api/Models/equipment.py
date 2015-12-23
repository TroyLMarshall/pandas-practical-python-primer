class Equipment:


    required_elements = {"name", "complexity", "tech_level", "price",
                         "weight", "value"}


    def __init__(self, name: str, complexity: str, tech_level: str,
                 price: float, weight: float, value: float):
        self.name = name
        self.complexity = complexity
        self.tech_level = tech_level
        self.price = price
        self.weight = weight
        self.value = value


