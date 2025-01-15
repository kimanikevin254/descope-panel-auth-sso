import numpy as np
import pandas as pd
import panel as pn
import hvplot.pandas

PRIMARY_COLOR = "#0072B5"
SECONDARY_COLOR = "#B54300"
CSV_FILE = "https://raw.githubusercontent.com/holoviz/panel/main/examples/assets/occupancy.csv"

# Enable the Panel extension
pn.extension(sizing_mode="stretch_width")

# Function to load the data
@pn.cache
def get_data():
    return pd.read_csv(CSV_FILE, parse_dates=["date"], index_col="date")

data = get_data()

# Function to transform the data (rolling average and outliers)
def transform_data(variable, window, sigma):
    """Calculates the rolling average and identifies outliers"""
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = np.abs(residual) > std * sigma
    return avg, avg[outliers]

# Function to get the plot
def get_plot(variable="Temperature", window=30, sigma=10):
    """Plots the rolling average and the outliers"""
    avg, highlight = transform_data(variable, window, sigma)
    return avg.hvplot(
        height=300, legend=False, color=PRIMARY_COLOR
    ) * highlight.hvplot.scatter(color=SECONDARY_COLOR, padding=0.1, legend=False)

# Create widgets
variable_widget = pn.widgets.Select(name="Variable", value="Temperature", options=list(data.columns))
window_widget = pn.widgets.IntSlider(name="Window", value=30, start=1, end=60)
sigma_widget = pn.widgets.IntSlider(name="Sigma", value=10, start=0, end=20)

# Bind widgets to plotting function
bound_plot = pn.bind(
    get_plot, variable=variable_widget, window=window_widget, sigma=sigma_widget
)

# Create the layout
widgets = pn.Column(variable_widget, window_widget, sigma_widget, sizing_mode="fixed", width=300)

# Configure the template with the logout button in the header
template = pn.template.MaterialTemplate(
    site="Panel",
    title="User Dashboard",
    header=[pn.Row(pn.layout.Spacer(), logout_widget)],
    sidebar=[variable_widget, window_widget, sigma_widget],
    main=[bound_plot]
)

# Serve the app (run with `panel serve <filename>.py`)
template.servable()