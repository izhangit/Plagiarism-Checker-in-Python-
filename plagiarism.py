# Plagiarism Checker in Python!❌🚫

# import NLTK
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load stop words
stop_words = set(stopwords.words('english'))

# Define a function to Calculate the Jaccard Similarity coefficient
def jaccard_similarity(set1,set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection/union

# Define a Function to check for Plagiarism
def check_plagiarism(text1,text2):
    # Tokenize the text
    tokens1 = set(word_tokenize(text1.lower()))-stop_words
    tokens2 = set(word_tokenize(text2.lower()))-stop_words

# Calculate the Jaccard Similarity Coefficient
    similarity = jaccard_similarity(tokens1,tokens2)

# Print the Similarity score 
    print("Similarity Score : {:.2f}".format(similarity))

# Example usage 
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."

    check_plagiarism(text1,text2)




