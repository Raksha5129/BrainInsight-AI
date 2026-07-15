import plotly.graph_objects as go

def confidence_gauge(confidence):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        number={"suffix": "%"},
        title={"text": "Model Confidence"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2563EB"},
            "steps": [
                {"range": [0, 50], "color": "#FECACA"},
                {"range": [50, 80], "color": "#FDE68A"},
                {"range": [80, 100], "color": "#BBF7D0"}
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "value": confidence
            }
        }
    ))

    fig.update_layout(height=350)

    return fig