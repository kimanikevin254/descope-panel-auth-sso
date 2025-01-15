from dotenv import load_dotenv
import os
import panel as pn

load_dotenv()

# Enable Panel extension
pn.extension(sizing_mode="stretch_width")

# Admin dashboard content
admin_content = f"""
# You're an admin. You have access to more data and functionality.
"""

# Create and configure the Material template
template = pn.template.MaterialTemplate(
    site="Panel",
    title="Admin Dashboard",
    main=[admin_content]
)

# Serve the admin dashboard
template.servable()