import streamlit as st
from code_review import review_code

st.title("GenAI Code Reviewer")
st.write("Submit your Code below for analysis!")

# Input section
user_code = st.text_area("Enter your Code here:")

if st.button("Analyze Code"):
    if user_code.strip():

        try:
            # Call the AI review function
            feedback = review_code(user_code)

            # Parsing feedback
            feedback_text = feedback

            # Display feedback paragraphs
            st.markdown("### Feedback:")
            st.markdown(feedback_text)

        except Exception as e:
            st.error(f"Error during processing: {e}")
    else:
        st.error("Please input valid Code.")
