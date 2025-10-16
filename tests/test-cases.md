# Test Cases - Online Judicial System (Chatbot + Forms)

| Test Case ID | Description | Input Data | Preconditions | Expected Result | Actual Result |
|--------------:|------------|------------|---------------|-----------------|----------------|
| TC01 | Chatbot opens via floating button | Click open | Chatbot accessible | Chat widget opens | |
| TC02 | Chatbot response to valid query | "How to file a complaint?" | Chat opened | Returns guidance text | |
| TC03 | Chatbot rejects empty query | "" | Chat opened | Shows "Please enter a query" or similar | |
| TC04 | File Complaint form - valid input | Name, Email, Complaint | Form page loaded (local) | "Submitted successfully" | |
| TC05 | File Complaint form - empty required | Missing fields | Form page loaded | Shows validation error | |
| TC06 | Contact Us form - valid input | Email, Message | Contact page loaded | "Message sent" | |
