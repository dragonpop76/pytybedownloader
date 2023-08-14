import csv

# creating a config list (the objects for Difficulty class will live here)
config = []
attributes_listed = []


class Difficulty:

    all = []

    def __init__(
            self,
            name: str,
            low_set=None,
            high_set=None,
            low_rep=None,
            high_rep=None
                 ):
        self._name = name
        self._low_set = low_set
        self._high_set = high_set
        self._low_rep = low_rep
        self._high_rep = high_rep

        Difficulty.all.append(self)

    def __repr__(self):
        return f"('{self.name}', {self.low_set} , {self.high_set} , {self.low_rep}, {self.high_rep})"

    def __str__(self):
        return f"'{self.name}', low set = {self.low_set}, high set = {self.high_set}, low rep = {self.low_rep}, " \
               f"high rep = {self.high_rep} \n"

    def change_set(self, name):
        print(f"Your current sets for {Difficulty.get_difficulty_by_name(self, name)} "
              f"difficulty are {Difficulty.get_low_set_by_name(self, name)} (x)-"
              f"{Difficulty.get_high_set_by_name(self, name)} (y)")
        self.low_set = int(input("change x"))
        self.high_set = int(input("change y"))

    def change_rep(self, name):
        print(f"Your current sets for {Difficulty.get_difficulty_by_name(self, name)} "
              f"difficulty are {Difficulty.get_low_rep_by_name(self, name)} (x)-"
              f"{Difficulty.get_high_rep_by_name(self, name)} (y)")
        self.low_rep = int(input("change x"))
        self.high_rep = int(input("change y"))

    @classmethod
    def instantiate_from_csv(cls):
        # opening up the csv file
        with open("exercise_config.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=' ')
            difficulty = list(reader)
            # putting our data into the format of a dictionary, so we can call on each object by name

            for setting in difficulty:
                Difficulty(
                    name=setting.get('name'),
                    low_set=setting.get('low_set'),
                    high_set=setting.get('high_set'),
                    low_rep=setting.get('low_rep'),
                    high_rep=setting.get('high_rep'),
                )

# getter
    def get_difficulty_by_name(self, name):
        # Search for a Difficulty object by its name and return it
        for difficulty_obj in self.all:
            if difficulty_obj.name == name:
                name = difficulty_obj.name
                return name

# getter
    def get_low_set_by_name(self, name):
        for difficulty_obj in self.all:
            if difficulty_obj.name == name:
                low_set = difficulty_obj.low_set
                return low_set

# getter
    def get_high_set_by_name(self, name):
        for difficulty_obj in self.all:
            if difficulty_obj.name == name:
                high_set = difficulty_obj.high_set
                return high_set

# getter
    def get_low_rep_by_name(self, name):
        for difficulty_obj in self.all:
            if difficulty_obj.name == name:
                low_rep = difficulty_obj.low_rep
                return low_rep

# getter
    def get_high_rep_by_name(self, name):
        for difficulty_obj in self.all:
            if difficulty_obj.name == name:
                high_rep = difficulty_obj.high_rep
                return high_rep

    @classmethod
    def get_attributes_by_name(cls, name):
        for difficulty_obj in cls.all:
            if difficulty_obj.name == name:
                name = f"{difficulty_obj.name} "
                low_set = f" {difficulty_obj.low_set} "
                high_set = f" {difficulty_obj.high_set} "
                low_rep = f" {difficulty_obj.low_rep} "
                high_rep = f" {difficulty_obj.high_rep} "
                attributes_listed.clear()
                attributes_listed.append(name)
                attributes_listed.append(low_set)
                attributes_listed.append(high_set)
                attributes_listed.append(low_rep)
                attributes_listed.append(high_rep)
                return attributes_listed

    @classmethod
    def print_to_csv(cls):
        with open("exercise_config.csv", 'w', newline='') as csvfile:
            fieldnames = ['name ', ' low_set ', ' high_set ', ' low_rep ', ' high_rep ']
            writer = csv.writer(csvfile, dialect='excel', delimiter=",")
            easy = Difficulty.get_attributes_by_name('easy')
            writer.writerow(fieldnames)
            writer.writerow(easy)
            medium = Difficulty.get_attributes_by_name('medium')
            writer.writerow(medium)
            hard = Difficulty.get_attributes_by_name('hard')
            writer.writerow(hard)
            csvfile.close()

    @property
    def name(self):
        if self._name:
            return self._name

    @property
    def low_set(self):
        if self._low_set:
            return self._low_set
        self._low_set = Difficulty.get_low_set_by_name(self, self.name)
        return self._low_set

    @low_set.setter
    def low_set(self, new_low_set):
        if new_low_set > 0 and isinstance(new_low_set, int):
            self._low_set = new_low_set
        else:
            print("invalid amount of sets")

    @property
    def high_set(self):
        if self._high_set:
            return self._high_set
        self._high_set = Difficulty.get_high_set_by_name(self, self.name)
        return self._high_set

    @high_set.setter
    def high_set(self, new_high_set):
        if new_high_set > 0 and isinstance(new_high_set, int):
            self._high_set = new_high_set
        else:
            print("invalid amount of sets")

    @property
    def low_rep(self):
        if self._low_rep:
            return self._low_rep
        self._low_rep = Difficulty.get_low_rep_by_name(self, self.name)
        return self._low_rep

    @low_rep.setter
    def low_rep(self, new_low_rep):
        if new_low_rep > 0 and isinstance(new_low_rep, int):
            self._low_rep = new_low_rep
        else:
            print("invalid amount of sets")

    @property
    def high_rep(self):
        if self._high_rep:
            return self._high_rep
        self._high_rep = Difficulty.get_high_rep_by_name(self, self.name)
        return self._high_rep

    @high_rep.setter
    def high_rep(self, new_high_rep):
        if new_high_rep > 0 and isinstance(new_high_rep, int):
            self._high_rep = new_high_rep
        else:
            print("invalid amount of sets")


Difficulty.instantiate_from_csv()
print(Difficulty.all[0].low_set)
