from pydantic import BaseModel, field_serializer

# Film model
# Only return relevant data pieces, not all are interesting or will be used
class Starship(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    films: list[str]
    url: str

    def serialize_to_int(self, value):
        try:
            v: int = int(float(value))
            return v
        except:
            return None

    def serialize_to_float(self, value):
        try:
            v: float = float(value)
            return v
        except:
            return None

    # Make number values consistent for re-usable frontend pieces
    # If data return types are consistent it'll make frontend development easier
    @field_serializer('cost_in_credits')
    def serialize_cost_in_credits(self, value: str, _info):
        return self.serialize_to_int(value)

    @field_serializer('length')
    def serialize_length(self, value: str, _info):
        return self.serialize_to_float(value)

    @field_serializer('max_atmosphering_speed')
    def serialize_max_atmosphering_speed(self, value: str, _info):
        return self.serialize_to_int(value)

    @field_serializer('passengers')
    def serialize_passengers(self, value: str, _info):
        return self.serialize_to_int(value)

    @field_serializer('cargo_capacity')
    def serialize_cargo_capacity(self, value: str, _info):
        return self.serialize_to_int(value)
    
    @field_serializer('hyperdrive_rating')
    def serialize_hyperdrive_rating(self, value: str, _info):
        return self.serialize_to_float(value)
    
    @field_serializer('MGLT')
    def serialize_MGLT(self, value: str, _info):
        return self.serialize_to_float(value)

# Film model
# Only return relevant data pieces, not all are interesting or will be used
class Film(BaseModel):
    title: str
    episode_id: int
    starships: list[Starship]