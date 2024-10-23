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

if "Alice" in did_both:
    print("Alice both attended the last class and submitted their assignments")

else:
    print("Alice did not both attend the last class and submit their assignments")