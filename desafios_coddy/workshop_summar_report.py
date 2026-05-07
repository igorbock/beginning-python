# Write a function summarize_workshop that takes a total score, number of participants, 
# four session ratings, and a list of material names. Return a dictionary with 
# three keys: "overall_average" (total divided by count), "session_average" (average of the four ratings), 
# and "unique_materials" (count of distinct material names in the list).

def summarize_workshop(total_score, num_participants, rating1, rating2, rating3, rating4, materials):
    # Write code here 
    overall_average = total_score / num_participants
    session_average = (rating1 + rating2 + rating3 + rating4) / 4
    unique_materials = len(set(materials))
    return {
        "overall_average": overall_average,
        "session_average": session_average,
        "unique_materials": unique_materials
    }