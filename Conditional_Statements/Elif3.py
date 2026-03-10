light = input("Enter the traffic light color:").lower()

if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow down")
elif light == "red":
    print("Stop")
else:
    print(" proceed carefully")