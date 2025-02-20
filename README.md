# Add Authentication and SSO to Your Panel App

This repository is part of an article that aims to guide readers through the process of integrating Descope authentication and OIDC SSO into a Panel application. 
It is tailored to assist developers who are either building new data apps with Panel's visualization framework or looking to add authentication to existing Panel apps. 
It demonstrate how to efficiently implement authentication features using Descope alongside Panel's built-in OAuth capabilities, making it a valuable resource for developers seeking to enhance their data visualization applications with secure user authentication and access control.

## Getting Started

To run this code on your local machine:
1. Follow along with the article to set up Descope, Okta, and obtain the necessary credentials.
  
2. Clone the repo:
  
  ```bash
  git clone https://github.com/kimanikevin254/descope-panel-auth-sso.git
  ```
3. Create and activate a virtual environment:

  ```bash
  cd descope-panel-auth-sso
  
  python -m venv venv
  
  source venv/bin/activate
  ```

3. Install all the dependencies using the command below:

  ```bash
  pip install -r requirements.txt
  ```

4. Rename `.env.example` to `.env` and fill out the values for each variable.

5. Run the app using the command:

  ```bash
  panel serve main.py admin.py user.py --oauth-provider=generic --index index.html --dev
  ```

6. Navigate to "http://localhost:5006" on your browser.
