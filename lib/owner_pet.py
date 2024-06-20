class Pet:
     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
     all = []
     def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        Pet.all.append(self)
        # GETTER / READER
        @property
        def pet_type(self):
            print("GETTING _pet_type")
            return self._pet_type
        #setter/writer
        @pet_type.setter
        def pet_type(self, pet_type):
            if pet_type in Pet.PET_TYPES:
                self._pet_type = pet_type
            else:
                raise ValueError(f"{pet_type} is not a valid pet type")


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [ pet for pet in Pet.all if pet.owner == self ]
    
    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception("NO")
        def get_sorted_pets(self):
            #get pets
            my_pets = self.pets()
            #sort pets
            sorted_pets = sorted(my_pets, key=lambda pet: pet.name)
            return sorted_pets