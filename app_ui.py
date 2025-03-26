import streamlit as st
import requests
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os

load_dotenv()

# Configure the base URL for your FastAPI server
BASE_URL = os.getenv("BACKEND_URL")

def upload_file():
    """Handle file upload"""
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        files = {"file": uploaded_file}
        response = requests.post(f"{BASE_URL}/upload", files=files)
        if response.status_code == 200:
            st.success("File uploaded successfully!")
            st.session_state.files = get_files()  # Refresh file list
        else:
            st.error(f"Error uploading file: {response.json()['detail']}")

def get_files():
    """Fetch list of files from server"""
    try:
        response = requests.get(f"{BASE_URL}/files")
        if response.status_code == 200:
            return response.json()
        return []
    except:
        st.error("Cannot connect to server")
        return []

def query_file(file_id, query):
    """Send query to server"""
    try:
        response = requests.post(
            f"{BASE_URL}/query",
            json={"file_id": file_id, "query": query}
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error querying file: {str(e)}"

def main():
    st.title("CSV RAG Interface")

    # Initialize session state for files
    if 'files' not in st.session_state:
        st.session_state.files = get_files()

    # Sidebar
    with st.sidebar:
        st.header("Files")
        
        # Upload section
        st.subheader("Upload New File")
        upload_file()
        
        # File list
        st.subheader("Available Files")
        files = st.session_state.files
        selected_file = None
        
        if files:
            file_names = {f["file_name"]: f["file_id"] for f in files}
            selected_name = st.selectbox("Select a file", list(file_names.keys()))
            if selected_name:
                selected_file = {
                    "id": file_names[selected_name],
                    "name": selected_name
                }
        else:
            st.info("No files available")

    # Main content area
    if selected_file:
        st.header(f"Selected File: {selected_file['name']}")
        
        # Show file content
        try:
            content_response = requests.get(f"{BASE_URL}/content/{selected_file['id']}")
            if content_response.status_code == 200:
                content = content_response.json()["response"]
                st.subheader("File Content Preview")
                st.text(content[:1000] + "..." if len(content) > 1000 else content)
        except:
            st.error("Error loading file content")

        # Query section
        st.subheader("Query the Data")
        query = st.text_area("Enter your query about the data")
        if st.button("Submit Query"):
            if query:
                with st.spinner("Generating response..."):
                    response = query_file(selected_file['id'], query)
                    st.write("### Response")
                    st.write(response)
            else:
                st.warning("Please enter a query")
    else:
        st.info("Please select a file from the sidebar to begin")

if __name__ == "__main__":
    main()