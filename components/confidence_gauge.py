import plotly.graph_objects as go

def confidence_gauge(confidence):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        number={
            "suffix": "%",
            "font": {"size": 42, "color": "#1E293B"}
        },
        title={
            "text": "<b>Model Confidence</b>",
            "font": {"size": 22, "color": "#1E293B"}
        },
        gauge={
            "axis": {
                "range": [0, 100],
                "tickcolor": "#64748B"
            },
            "bar": {
                "color": "#2563EB"
            },
            "steps": [
                {"range": [0, 50], "color": "#FECACA"},
                {"range": [50, 80], "color": "#FDE68A"},
                {"range": [80, 100], "color": "#BBF7D0"}
            ],
            "threshold": {
                "line": {
                    "color": "#DC2626",
                    "width": 5
                },
                "value": confidence
            }
        }
    ))

    fig.update_layout(
        height=350,
        paper_bgcolor="white",
        font=dict(
            family="Poppins",
            color="#1E293B"
        ),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig