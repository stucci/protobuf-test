import addressbook_pb2

addressbook = addressbook_pb2.AddressBook()

person = addressbook.people.add()
person.id = 999
person.name = 'Jhon Doe'
person.email = 'jhon.doe@sample.co.jp'

serialized = addressbook.SerializeToString()
print(serialized)

addressbook_deserialized = addressbook_pb2.AddressBook()
addressbook_deserialized.ParseFromString(serialized)
print(addressbook_deserialized)
