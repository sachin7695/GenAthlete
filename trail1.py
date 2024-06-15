import streamlit as st 
import time

st.set_page_config(page_title='GenAthlete', layout="wide")

name = "GenAthlete"
tag = "Unlocking Athlete-Inspired Style for Customers."
st.markdown(f"<h1 style='text-align: center;'>{name}</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'><em>{tag}<em></h3>", unsafe_allow_html=True)

st.sidebar.title("Login Here")
option = st.sidebar.selectbox("Users", ("John", "Virat"))

if option == "John":
    tab1, tab2 , tab3, tab4, tab5 = st.tabs(['Request', 'Brands Extracted', 'Product Recommendations', "Couldn't found any? Click here to Generate.", "Product Encrichment"])
    with tab1:
        st.title("Request Memo")
        st.subheader("_You'll find what are you looking for or you can Generate_")
        name = st.text_input("Please enter your prompt here.")
        #upload image
        st.write("_OR_")
        upload = st.file_uploader("Choose an image...", type=["jpg", "png"])
        if st.button("Submit"):
            st.success("Thank you for your request!. Please redirect to next tab to choose the extracted brands.")
            
    with tab2:
        with st.spinner("Please Wait..."):
            time.sleep(5)
            st.title("Brands Extracted")
            st.subheader("_Brands that were extracted from the image._")
            # Display the extracted brands
            st.write("From the image you provided, the brands associated with the jersey are:")
            st.write("1. Adidas - The Adidas logo is visible on the right side of the chest. ")
            st.write("2. FIFA - The FIFA World Cup winners badge is on the left side of the chest, above the national emblem of the Argentina Football Association (AFA).")
            st.write("These are the primary brands/logos visible on the jersey.")
            st.selectbox("Choose the brands",("None","Adidas", "FIFA"))
            if st.button("Next"):
                st.success("You'll get your product recommendations on next Page")
                st.balloons()
        
    with tab3:
        with st.spinner("Loading..."):
            time.sleep(5)
        
            st.title("Product Recommendations")
            st.subheader("_Based on your preferences, these are the products we recommend._")
            # Display the recommended products
            st.write("Here are some products that might be relevant based on your preferences:")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image("https://www.bing.com/th?id=OIP.kWGQwNmbqsmuGmmNTS6HcwHaHa&w=146&h=150&c=8&rs=1&qlt=90&o=6&dpr=1.1&pid=3.1&rm=2")
                st.write("__Name:__ Adidas Jersey")
                st.write("Price: $29.99")
                st.write("Rating: 4.5/5")
                
            with col2:
                st.image("data:image/jpeg;base64,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")
                st.write("__Name:__ Adidas Shorts")
                st.write("Price = $29.75")
                st.write("Rating = 4/5")
                
            with col3:
                st.image("https://th.bing.com/th?id=OPHS.UHzSDQUP4edWAg474C474&w=128&h=168&c=17&pcl=f5f5f5&o=5&dpr=1.1&pid=21.1")
                st.write("__Name:__ Adidas Spikeless Running Shoes")
                st.write("Price = $69.99")
                st.write("Rating = 4.7/5")
                
            with col4:
                st.image("data:image/jpeg;base64,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")
                st.write("__Name:__ Adidas Cap")
                st.write("Price = $19.50")
                st.write("Rating = 4.8/5")
        
        st.write("These are the products that match your preferences and are recommended based on your choices.")
        
    with tab4:
        st.header("Generate your own customize apparel")
        user_input = st.text_input("Enter your prompt: ")
        if st.button("Generate"):
            with st.spinner("Loading..."):
                time.sleep(5)
        
                col1, col2 = st.columns(2)
                with col1:
                    st.image("sleeveless.png")
                    button = st.button("View Product")
                with col2:
                    st.image("sleeve.png")
        
    with tab5:
        with st.spinner("Loading..."):
            time.sleep(5)
        
            st.subheader("Generated Product Name: _Adidas AirFlex Sleeveless Jersey_")
            col1, col2 = st.columns(2)
            
            with col1:
                st.image("sleeveless.png")
                
            with col2:
                st.subheader("Generated Product Description:")
                st.write("This sleek, comfortable jersey is designed for everyday use. It features a round neckline and soft, breathable fabric for a great fit. The adidas AirFlex sleeveless jersey is a versatile choice for any outfit.")
                st.subheader(":blue[$19.99]")
                st.subheader("Generated Product Attribute:")
                st.write("The product arrived in good condition and exceeded my expectations. It's well-made and has a great fit. I highly recommend this product!")
                st.write("Generated Product Badges")
                st.write("1. Genz Look")
                st.write("2. Good Fabric")

elif option == "Virat":
    tab1, tab2 , tab3, tab4 = st.tabs(['Request', 'Brands Extracted', 'Product Recommendations', "Couldn't found any? Click here to Generate."])
    with tab1:
        st.title("Request Memo")
        st.subheader("_You'll find what are you looking for or you can Generate_")
        name = st.text_input("Please enter your prompt here.")
        #upload image
        st.write("_OR_")
        upload = st.file_uploader("Choose an image...", type=["jpg", "png"])
        if st.button("Submit"):
            st.success("Thank you for your request!. Please redirect to next tab to choose the extracted brands.")
            
    with tab2:
        st.title("Brands Extracted")
        st.subheader("_Brands that were extracted from the image._")
        # Display the extracted brands
        st.write("From the image you provided, the brands associated with the jersey are:")
        st.write("1. Nike - Main sportswear brand on the jersey. ")
        st.write("Only Nike is primary brands/logo visible on the jersey.")
        st.selectbox("Choose the brands",("None","Nike"))
        if st.button("Next"):
            st.success("You'll get your product recommendations on next Page")
            st.balloons()