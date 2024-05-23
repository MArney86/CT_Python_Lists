#Given:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#Task 1:
did_both = []
for attendee in attended: #iterate the list
    if attendee in submitted: #test if value is in both
        did_both.append(attendee) #add to the did_both list if it is in both
    else: 
        pass # do nothing if value is not in both lists
print(did_both)
#Task 2:
set_sub = set(submitted)
set_att = set(attended)

if set_sub == set_att:
    print("The 2 lists are equal") #let the user know that both lists are the same
else:
    print("The 2 lists are not equal") #let the user know both list are not the sam

#Task 3:
for attendee in attended: #iterate the list
    if attendee not in submitted: #test if value is not in both lists
        att_index = attended.remove(attendee) #if not in both lists remove from the attended list
    else:
        pass
print(attended) #print the modified list to show that it was successful    