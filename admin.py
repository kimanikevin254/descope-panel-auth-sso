from dotenv import load_dotenv
import os
import panel as pn

load_dotenv()

# Enable Panel extension
pn.extension(sizing_mode="stretch_width")

# Extract roles and permissions
tenant_data = pn.state.user_info.get('tenants', {}).get(os.getenv('DESCOPE_TENANT_ID'), {})
roles = tenant_data.get('roles', [])
permissions = tenant_data.get('permissions', [])

# Admin dashboard content
admin_content = f"""
# You're an admin. You have access to more data and functionality.

#### Your Roles:
<ul>
    {"".join(f"<li>{role}</li>" for role in roles) if roles else "<li>No roles assigned</li>"}
</ul>

#### Your Permissions:
<ul>
    {"".join(f"<li>{permission}</li>" for permission in permissions) if permissions else "<li>No permissions assigned</li>"}
</ul>
"""

# Logout button
logout_widget = pn.widgets.Button(name="Logout", button_type="danger", width=100, align="end")

# Configure logout functionality
logout_widget.js_on_click(code="""window.location.href = '/logout'""")

# Authorization callback for the admin dashboard
def authorize_admin(user_info):
    if "Tenant Admin" in roles:
        return True
    return "/user"

# Assign the authorization callback
pn.config.authorize_callback = authorize_admin

# Create and configure the Material template
template = pn.template.MaterialTemplate(
    site="Panel",
    title="Admin Dashboard",
    header=[pn.Row(pn.layout.Spacer(), logout_widget)],
    main=[admin_content]
)

# Serve the admin dashboard
template.servable()
