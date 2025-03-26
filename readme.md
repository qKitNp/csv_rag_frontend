# CSV RAG Interface

A Streamlit-based web interface for uploading and querying CSV files using RAG (Retrieval Augmented Generation) capabilities.

## Features

- **File Upload**: Upload CSV files through an intuitive interface
- **File Management**: View and select from previously uploaded files
- **Content Preview**: See a preview of the CSV file contents
- **Natural Language Queries**: Ask questions about your data in plain English
- **Real-time Responses**: Get AI-powered responses based on your CSV data

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd csv_rag_frontend
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your backend URL:

```
BACKEND_URL=<your-backend-url>
```

### Running the Application

```bash
streamlit run app_ui.py
```

The application will be available at `http://localhost:8501`

## Usage

1. **Upload a CSV File**:

   - Click the "Choose a CSV file" button in the sidebar
   - Select your CSV file from your local system

2. **Select a File**:

   - Choose from previously uploaded files using the dropdown in the sidebar

3. **View Content**:

   - Once a file is selected, you'll see a preview of its contents

4. **Query Your Data**:
   - Enter your question in the text area
   - Click "Submit Query" to get AI-generated insights

## Environment Variables

- `BACKEND_URL`: URL of the FastAPI backend server

## Deployment

The application is configured for deployment on Heroku using:

- `Procfile`: Defines the web process
- `setup.sh`: Configures Streamlit for production

## Technical Details

Built with:

- Streamlit for the frontend interface
- Requests for API communication
- Python-dotenv for environment management
- Pandas for data handling
