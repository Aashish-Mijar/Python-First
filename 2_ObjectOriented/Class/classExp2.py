class Computer:
    deviceName=""
    processor=""
    ram=""
    systemType=""
    edition=""

user1=Computer()
user2=Computer()
user3=Computer()

# ----- USER 1
user1.deviceName="Desktop-6R5F0UT"
user1.processor="12th Gen"
user1.ram=8
user1.systemType="64-bit operating system"
user1.edition="Windows 10 Pro"

#  ----- USER 2
user2.deviceName="Desktop-65T0T"
user2.processor="13th Gen"
user2.ram=16
user2.systemType="64-bit operating system"
user2.edition="Windows 11"

# ------ USER 3
user3.deviceName="Desktop-2Y04H"
user3.processor="14th Gen"
user3.ram=32
user3.systemType="64-bit operating system"
user3.edition="Windows 11"

print(f"\nDevice name: {user1.deviceName}\nProcessor: {user1.processor}\nRAM: {user1.ram}\nSystem Type: {user1.systemType}\nEdition: {user1.edition}\n")
print(f"Device name: {user2.deviceName}\nProcessor: {user2.processor}\nRAM: {user2.ram}\nSystem Type: {user2.systemType}\nEdition: {user2.edition}\n")
print(f"Device name: {user3.deviceName}\nProcessor: {user3.processor}\nRAM: {user3.ram}\nSystem Type: {user3.systemType}\nEdition: {user3.edition}\n")