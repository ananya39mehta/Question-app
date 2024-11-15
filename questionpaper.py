import streamlit as st

# Function to display multiple-choice questions and answers
def mcq_questions():
    st.header("Multiple Choice Questions (MCQs)")

    # Initialize score variable
    score = 0

    # Question 1
    st.subheader("1. What are the issues usually faced in relationships?")
    options = ["Difference of opinion", "Lack of trust", "Generation gap", "All of the above"]
    answer = "All of the above"
    user_answer = st.radio("Choose an option", options, key="q1")
    if user_answer == answer:
        score += 1

    # Question 2
    st.subheader("2. Is it necessary to have a difference of opinion in a relationship?")
    options = ["Yes", "No", "It depends", "Not at all"]
    answer = "Yes"
    user_answer = st.radio("Choose an option", options, key="q2")
    if user_answer == answer:
        score += 1

    # Question 3
    st.subheader("3. Why do we say someone doesn't understand us?")
    options = ["They can't hear us", "They can't understand us", "They don't want to follow our advice", "None of the above"]
    answer = "They don't want to follow our advice"
    user_answer = st.radio("Choose an option", options, key="q3")
    if user_answer == answer:
        score += 1

    # Question 4
    st.subheader("4. Why do people not follow advice even when it's for their own good?")
    options = ["Because they don't care", "They don't trust the person", "Because they don't want to", "None of the above"]
    answer = "Because they don't want to"
    user_answer = st.radio("Choose an option", options, key="q4")
    if user_answer == answer:
        score += 1

    # Question 5
    st.subheader("5. Why is it important to accept that 'everyone is right from their perspective'?")
    options = ["To avoid conflict", "To understand different viewpoints", "To accept people", "All of the above"]
    answer = "All of the above"
    user_answer = st.radio("Choose an option", options, key="q5")
    if user_answer == answer:
        score += 1

    # Question 6
    st.subheader("6. What is the main factor causing people to reject advice?")
    options = ["Ego", "Pride", "Stubbornness", "Lack of interest"]
    answer = "Ego"
    user_answer = st.radio("Choose an option", options, key="q6")
    if user_answer == answer:
        score += 1

    # Question 7
    st.subheader("7. Why do children often feel misunderstood by their parents?")
    options = ["Parents are too busy", "Generational gap", "Parents don't care", "Lack of communication"]
    answer = "Generational gap"
    user_answer = st.radio("Choose an option", options, key="q7")
    if user_answer == answer:
        score += 1

    # Question 8
    st.subheader("8. What is an effective way to resolve arguments in relationships?")
    options = ["Ignoring the issue", "Talking openly and honestly", "Avoiding confrontation", "Blaming each other"]
    answer = "Talking openly and honestly"
    user_answer = st.radio("Choose an option", options, key="q8")
    if user_answer == answer:
        score += 1

    # Question 9
    st.subheader("9. How does maintaining mutual respect in relationships affect their longevity?")
    options = ["It strengthens the bond", "It creates distance", "It leads to frequent arguments", "It doesn't matter"]
    answer = "It strengthens the bond"
    user_answer = st.radio("Choose an option", options, key="q9")
    if user_answer == answer:
        score += 1

    # Question 10
    st.subheader("10. How can one handle rejection from parents effectively?")
    options = ["By arguing with them", "By understanding their perspective", "By ignoring their advice", "By withdrawing from them"]
    answer = "By understanding their perspective"
    user_answer = st.radio("Choose an option", options, key="q10")
    if user_answer == answer:
        score += 1

    return score

# Function to display subjective questions
def subjective_questions():
    st.header("Subjective Questions")

    st.subheader("11. Discuss the role of difference of opinion in relationships. Why is it considered natural, and what makes arguments an 'unnecessary creation'?")
    st.text_area("Your answer here", key="q11")

    st.subheader("12. How does the energy and intention behind advice affect its acceptance, according to the speaker? Provide examples from the text to support your answer.")
    st.text_area("Your answer here", key="q12")

    st.subheader("13. What is the significance of accepting that 'everyone is right from their perspective'? How can this understanding influence interpersonal relationships?")
    st.text_area("Your answer here", key="q13")

    st.subheader("14. Analyze how rejection from parents can impact the communication and relationship with their children. Why is acceptance crucial in maintaining a strong parent-child relationship?")
    st.text_area("Your answer here", key="q14")

    st.subheader("15. Why do children often stop sharing their experiences with their parents as they grow up? How can parents maintain an open and trusting communication channel with their children?")
    st.text_area("Your answer here", key="q15")

# Main function to display the app
def main():
    st.title("Relationship Issues and Understanding Quiz")

    # Display multiple-choice questions
    score = mcq_questions()

    # Display subjective questions
    subjective_questions()

    # Create a Submit button
    if st.button('Submit'):
        # Display final score
        st.subheader("Your Final Score:")
        st.write(f"You scored {score} out of 10 for the multiple-choice questions.")

        st.write("Note: The subjective questions are not graded automatically.")

if __name__ == "__main__":
    main()
