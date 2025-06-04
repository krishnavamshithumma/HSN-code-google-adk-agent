# HSN Code Agent

This project implements an HSN (Harmonized System of Nomenclature) code agent using the Google ADK (Agent Development Kit). The agent can validate HSN codes for format and hierarchy, and suggest HSN codes based on a product description.

---

## 📁 Project Structure

```text
.
├── data
│   └── HSN_Master_Data.csv
├── __pycache__
│   └── utils.cpython-312.pyc
├── README.md
├── requirements.txt
└── src
    ├── agent.py
    ├── data_utils.py
    ├── __init__.py
    └── validation.py

*   agent.py: Contains the core logic for the HSN code agent, defining tools for validation and suggestion. It uses the google.adk.agents.Agent class.
    
*   data\_utils.py: Provides a utility function to load the HSN master data from a CSV file into a pandas DataFrame.
    
*   validation.py: Includes functions for validating HSN code format, checking existence in the master data, and validating the hierarchical structure of the HSN code.
    
*   requirements.txt: Lists all the necessary Python packages to run the project.
    

**Features**
------------

*   **HSN Code Validation:** Checks if an HSN code is in a valid format (numeric, specific lengths) and if it exists in the provided master data. It also validates the hierarchical structure of the code.
    
*   **HSN Code Suggestion:** Suggests relevant HSN codes based on a given product description by performing a keyword match against the master data.
    

**Setup and Installation**
--------------------------

Follow these steps to set up and run the project locally:

### **1\. Clone the Project**

First, clone the repository to your local machine:

git clone https://github.com/krishnavamshithumma/HSN-code-google-adk-agent.gitcd HSN-code-google-adk-agent

### **2\. Add Your Data**

Place your HSN master data CSV file (e.g., HSN\_Master\_Data.csv) inside the data folder. Ensure the CSV has columns named HSNCode and Description.

### **3\. Configure Google API Key**

Create a .env file inside the src folder and add your Google API key as follows:

GOOGLE\_GENAI\_USE\_VERTEXAI=FALSEGOOGLE\_API\_KEY="paste\_your\_api\_key\_here"

Replace "paste\_your\_api\_key\_here" with your actual Google API key.

### **4\. Install Requirements**

Install all the necessary Python packages using pip:

pip install -r requirements.txt

**How to Run the Agent**
------------------------

You can run the HSN code agent either through the terminal or via a web interface.

### **Running via Terminal**

adk run src

### **Running via Web Interface**

adk web

When prompted on the web interface, make sure to select src as the agent directory.

**Interacting with the Agent**
------------------------------

Once the agent is running (either in terminal or web mode), you can interact with it by providing HSN codes or product descriptions.

### **Examples:**

*   **Validate HSN Code:**01011010_(Expected output will include validation status, format validity, existence, hierarchy validation, and description if it exists.)_
    
*   **Suggest HSN Codes from Description:**LIVE HORSES_(Expected output will include suggestions for matching HSN codes and their descriptions.)_
    

**Screenshots**
---------------

_(You would insert your screenshots here, showing examples of the agent's output for both validation and suggestion queries.)_