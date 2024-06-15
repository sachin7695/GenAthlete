import streamlit as st
from openai import OpenAI
import time
import pandas as pd
import json

st.set_page_config(page_title='GenAthlete', layout="wide")

st.image("genaii.png")
st.sidebar.title("Login Here")
option = st.sidebar.selectbox("Users", ("John", "Virat"))

client = OpenAI(api_key='sk-proj-')

def extract_brands(image_url):
    response = client.chat.completions.create(
                    model = "gpt-4o",
                    messages = [
                        {
                            "role": "system",
                            "content": "You are a expert in extracting the brands associated on Jersey."
                        },
                        {
                            "role": "user",
                            "content" :[
                                {"type": "text", "text": "Extract the Brands on Jersey."},
                                {"type":"image_url","image_url":{
                                    "url":f"{image_url}"
                                }}
                            ]
                        }
                    ],
                    temperature = 0.4,
                    max_tokens= 500
                )
    final_response = response.choices[0].message.content
    return final_response

def recommend_products(final_response):
    data =  pd.read_csv("product.csv")
    df = pd.DataFrame(data)
    
    final_response_rec = final_response
    guidlines = """1. Do Not Hallucinate.
    2. Retrive only [Name: , Price:, Rating: (assume product rating between 1 to 5 and display as: 4.2(Choose randomly Range from 3.5-5)), ProductImage:(Replace link after https://dks.scene7.com/is/image/)].
    Be friendly and retrive the answer in JSON format only.
    3. recommend atleast 4 products with all the parameters filled from given data.
    4. Be Concise. Replace the complete data for parameters mentioned.
    """
    
    prompt =f"""you are a helpful assistant who is expert in recommending products only in JSON format from the given data.
    You should only recommend products from {final_response_rec} brand.
    Here's the data: {df}.
    Based on the data, recommend me a product that would be suitable for the customer based on their preferences.
    Follow {guidlines}.
    """
    
    product_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who is expert in recommending products."
            },
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
        temperature=0.6,
        max_tokens=800
    )
    
    response = product_response.choices[0].message.content
    return response
  
  
def generate_image(user_input):
    response = client.images.generate(
        model="dall-e-3",
        prompt=user_input,
        n=1,
        size="1024x1024",
        quality="standard",
    )
    image_url = response.data[0].url
    return image_url  

def generate_des(image1):
    guidlines = """1. Do Not Hallucinate.
    2. Generate [ProductName: , ProductDes:, Price:, ProductAtt:(single line), ProductBadges:(one)]
    Be friendly and give answer JSON format only.
    4. Be Concise.
    """
    prompt= f""" You are a helpful assistant who is expert in generating description for the product.
    Follow {guidlines}.
    """
    
    response_des = client.chat.completions.create(
        model = "gpt-4o",
        messages=[
        {
            "role": "system",
                "content": "You are a helpful assistant who is expert in product descriptions." },
        {
            "role": "user",
            "content" :[
                {"type": "text", "text": f"{prompt}"},
                {"type":"image_url","image_url":{
                    "url":f"{image1}"
                }}
            ]
        }
    ],
        temperature = 0.4,
        max_tokens=1000
    )
    response_dis = response_des.choices[0].message.content
    return response_dis
    

if option == "John":
    tab1, tab2 , tab3, tab4 = st.tabs(['Request & Brands Extracted', 'Product Recommendations', "Couldn't found any? Click here to Generate.", "Product Encrichment"])
    with tab1:
        st.title("Request Memo ")
        st.subheader("_You'll find what are you looking for or you can Generate_")
        
        image_url = st.text_input("Please Enter the Photo URL.")
        if st.button("Submit"):
            final_response = extract_brands(image_url)
            st.success(final_response)
            st.write("Please go to next tab for the Product recommendations.")
            
            
    with tab2:
        st.title("Product Recommendations")
        st.subheader("_Here's Your Product Recommendations_")
        if 'final_response' in locals():
            response = recommend_products(final_response)
            st.write(response)
            
            start_index = response.index("[")
            end_index = response.rindex("]")

            # Extract the JSON array
            json_array = response[start_index:end_index+1]
        
            file = "response_json.json"
            with open(file, "w") as f:
                f.write(json_array)
                
            with open('response_json.json', 'r') as file:
                    response = json.load(file)

                # Create Streamlit columns
            col1, col2, col3, col4 = st.columns(4)

            # Display products in each column
            columns = [col1, col2, col3, col4]
            for idx, product in enumerate(response):
                with columns[idx]:
                    st.image(product["ProductImage"])
                    name = product["Name"]
                    st.write(f"__Name:__ {name}")  
                    price = (product["Price"])
                    st.write(f"__Price:__ {price}")
                    ratings= (product["Rating"])
                    st.write(f"__Rating:__ {ratings}/5")
                    
    with tab3:
        st.header("Generate your own customize apparel")
        user_input = st.text_input("Enter your prompt: ")
        if st.button("Generate"):
            with st.spinner("Loading..."):
                time.sleep(5)
                col1, col2 = st.columns(2)
                with col1:
                    image1 = generate_image(user_input)
                    st.image(image1)
                    button = st.button("View Product")
                with col2:
                    image = generate_image(user_input)
                    st.image(image)
                    
    with tab4:
        if 'image1' in locals():
            st.header("Product Encrichments:")
            col1, col2 = st.columns(2)
            details_str = generate_des(image1)
            
            start_index = details_str.find('{')

            # Find the index of the closing curly brace and include it in the substring
            end_index = details_str.rfind('}') + 1

            # Extract the JSON content
            details_json_str = details_str[start_index:end_index]

            # Write the extracted JSON content to a new file
            with open("details.json", "w") as f:
                f.write(details_json_str)

            with open("details.json", "r") as file:
                try:
                    details = json.load(file)
                except json.decoder.JSONDecodeError as e:
                    # Handle JSON decode error
                    st.error(f"Error decoding JSON: {e}")
                    details = None
                
            if details is not None:
                # Display the details in Streamlit columns
                col1, col2 = st.columns(2)
                with col1:
                    st.image(image1)

                with col2:
                    # Display each key-value pair separately with custom labels
                    st.subheader("__Gen Product Name:__")
                    st.write(details.get("ProductName"))

                    st.subheader("__Gen Product Description:__")
                    st.write(details.get("ProductDes"))

                    st.subheader("__Price:__")
                    st.write(details.get("Price"))

                    st.subheader("__Gen Product Attributes:__")
                    st.write(details.get("ProductAtt"))

                    st.subheader("__Gen Product Badges:__")
                    st.write(details.get("ProductBadges"))