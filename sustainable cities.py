class UrbanArea:
    def __init__(self, name, housing_density, public_transport_score, green_area_ratio, waste_recycling_rate):
        self.name = name
        self.housing_density = housing_density
        self.public_transport_score = public_transport_score
        self.green_area_ratio = green_area_ratio
        self.waste_recycling_rate = waste_recycling_rate
        self.sustainability_score = 0

    def evaluate(self):
        self.sustainability_score = (
            (100 - abs(self.housing_density - 300)) * 0.25 +
            self.public_transport_score * 0.25 +
            self.green_area_ratio * 0.25 +
            self.waste_recycling_rate * 0.25
        )

    def decision(self):
        if self.sustainability_score > 85:
            return "Highly Sustainable"
        elif self.sustainability_score > 65:
            return "Sustainable with Improvements"
        else:
            return "Not Sustainable"

    def __str__(self):
        return (
            f"Area: {self.name}\n"
            f" Housing Density: {self.housing_density}\n"
            f" Public Transport Score: {self.public_transport_score}\n"
            f" Green Area Ratio: {self.green_area_ratio}%\n"
            f" Recycling Rate: {self.waste_recycling_rate}%\n"
            f" Sustainability Score: {self.sustainability_score:.2f}\n"
            f" Verdict: {self.decision()}\n"
        )


areas = [
    UrbanArea("Metro Core", 320, 90, 25, 70),
    UrbanArea("Eco Suburb", 250, 60, 40, 80),
    UrbanArea("Old Town", 400, 50, 10, 30),
    UrbanArea("Smart Village", 180, 70, 50, 85),
]

print("Smart Urban Planning and Design for Sustainable Cities\n")
for area in areas:
    area.evaluate()
    print(area)