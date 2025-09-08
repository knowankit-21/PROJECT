class Army:
    def __init__(self):
        self.name='Ankit sharma'
        self.age=25
        self.gender='Male'
        self.relationship='unmarried'
        self.location='Kashmir'
        self.From='Bihar,patna'
        self.gn=self.Gun()
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Relationship:",self.relationship)
        print("Location:",self.location)
        print("From",self.From)

    class Gun:
        def __init__(self):
            self.name='AK47'
            self.capacity='75 Rounds'
            self.lenght='34.4 inch'
        def disp(self):
            print("Gun Name:",self.name)
            print("Capacity:",self.capacity)
            print("Length:",self.lenght)

a=Army()
a.show()
p=a.gn
p.disp()