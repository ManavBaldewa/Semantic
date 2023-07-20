import spacy
import streamlit as st
import spacy.cli 

spacy.cli.download("en_core_web_lg")

# Load the English language model from SpaCy
nlp = spacy.load("en_core_web_lg")

# Define a function to calculate the semantic similarity between two texts
def calculate_similarity(text1, text2) :
  """
  Calculates the semantic similarity between two texts.

  Args:
    text1 (str): The first text.
    text2 (str): The second text.

  Returns:
    float: The semantic similarity between the two texts.
  """
# Create Doc objects from the two texts
  sent1 = nlp(text1)
  sent2 = nlp(text2)

# Calculate the similarity between the two Docs
  value = sent1.similarity(sent2)

# Round the similarity to four decimal places
  return round(value, 4)

# Define the main function
def main() :
# Set the title of the app
    st.title("Semantic Similarity Tester")
  
# Add a markdown text with a background color
    html_temp = """
    <div style = "backgroud-color : tomato ; padding : 10px">
    <h2 style = "color : white ; text-align : center ;>Streamlit Semantic Textual Similarity App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

# Get the two texts from the user
    text1 = st.text_input("Text1")
    text2 = st.text_input("Text2")
  
# Calculate the similarity between the two texts
    similarity = ""
    if st.button("Calculate similarity") :
        similarity = calculate_similarity(text1, text2)
      
# Display the similarity
    st.success("Similarity score : {}".format(similarity))

# Run the main function
if __name__ == "__main__" :
    main()
