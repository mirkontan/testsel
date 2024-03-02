import streamlit as st
from selenium import webdriver

def scrape_url(url):
    # Initialize Selenium WebDriver (you may need to adjust the path to your WebDriver)
    driver = webdriver.Chrome()
    
    # Open the URL
    driver.get(url)
    
    # Scrape content
    content = driver.page_source
    
    # Close the WebDriver
    driver.quit()
    
    return content

# Streamlit UI
st.title("Web Content Scraper")

# Input URL
url = st.text_input("Enter URL")

if st.button("Scrape"):
    if url:
        try:
            content = scrape_url(url)
            st.success("Scraping successful!")
            st.write(content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid URL")
