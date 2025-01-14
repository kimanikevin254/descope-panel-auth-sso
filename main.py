from dotenv import load_dotenv
import os
import panel as pn

# Load env variables
load_dotenv()

# Enable Panel extension
pn.extension(sizing_mode="stretch_width")

# Define the authorization callback
def authorize(user_info):
    """
    Authorization callback to redirect users based on roles.
    """
    # Extract user roles from the user_info dict
    roles = user_info.get('tenants').get(os.getenv('DESCOPE_TENANT_ID'), {}).get('roles')

    if "Tenant Admin" in roles:
        return "/admin"
    else:
        return "/user"

# Assign the authorization callback
pn.config.authorize_callback = authorize