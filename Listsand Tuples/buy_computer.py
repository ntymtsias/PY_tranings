current_choice = "999"
computer_parts = []

available_parts = ["computer","monitor","keyboard","mouse","mouse mat","hdmi"]
while current_choice != "0":
    current_choice = 99 if current_choice == '' else current_choice
    if int(current_choice) <= len(available_parts)+1:
        idx = int(current_choice) - 1
        part_to_add = available_parts[idx]
        print(f"Adding {current_choice}: {part_to_add}")
        if part_to_add not in computer_parts:
            computer_parts.append(part_to_add)
    else:
        print("Please select a value from the lsit:")
        values = [print(f"{idx}: {name}") for idx,name in enumerate(available_parts,start=1)]
        print("0: to finish")

    current_choice = input()
print(computer_parts)

