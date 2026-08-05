import os
import streamlit as st
import numpy as np
from joblib import load
import pandas as pd

# Initialize the session state with an empty prediction
if "pred" not in st.session_state:
    st.session_state["pred"] = None
    # st.session_state stores value across user interactions

# Function to load the model (use caching)
@st.cache_resource(show_spinner="Loading Model...")
def load_model():
    model_path = "model/model.joblib"
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}. Make sure the file exists and was uploaded.")
        st.stop()

    try:
        return load(model_path)
    except ModuleNotFoundError as e:
        st.error(
            "Failed to load the model: missing module required by the trained pipeline.\n\n"
            f"Missing: `{getattr(e, 'name', str(e))}`\n\n"
            "Fix: install the scikit-learn version used for training, or re-export the model with a compatible serializer."
        )
        st.stop()
    except Exception as e:
        st.error(f"Failed to load the model:\n\n{e}")
        st.stop()

# Callback function to make a prediction
def make_prediction(pipe):
    X_pred = pd.DataFrame([{
        "miles": st.session_state["miles"],
        "year": st.session_state["year"],
        "make": st.session_state["make"],
        "model": st.session_state["model"],
        "body_type": st.session_state["body_type"],
        "vehicle_type": st.session_state["vehicle_type"],
        "drivetrain": st.session_state["drivetrain"],
        "transmission": st.session_state["transmission"],
        "fuel_type": st.session_state["fuel_type"],
        "engine_size": st.session_state["engine_size"],
        "engine_block": st.session_state["engine_block"],
        "state": st.session_state["province"]
    }])

    # Normalize string/categorical inputs to a consistent format (trim + lower)
    for col in [
        "make", "model", "body_type", "vehicle_type", "drivetrain",
        "transmission", "fuel_type", "engine_block", "state"
    ]:
        if col in X_pred.columns:
            val = X_pred.at[0, col]
            if isinstance(val, str):
                val_norm = val.strip().lower()
                # small compatibility mapping
                if col == "fuel_type" and val_norm == "hyrid":
                    val_norm = "hybrid"
                X_pred.at[0, col] = val_norm

    # Attempt prediction and handle pipeline errors
    try:
        pred = pipe.predict(X_pred)
        st.session_state["pred"] = round(float(pred[0]), 2)
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        # keep previous prediction in session_state (if any)

if __name__ == "__main__":
    st.title("Prediction Car Price")

    # Load model
    pipe = load_model()

    with st.form(key="form"):
        col1, col2, col3 = st.columns(3)

        # Column 1 inputs
        with col1:
            st.number_input("Miles", value=86132.0, min_value=0.0, step=0.1, key="miles")
            st.selectbox("Model", index=0, key="model", options=[
                'prius', 'highlander', 'civic', 'accord', 'corolla', 'ridgeline',
                'odyssey', 'cr-v', 'pilot', 'camry solara', 'matrix', 'rav4',
                'hr-v', 'fit', 'yaris', 'yaris ia', 'tacoma', 'camry',
                'avalon', 'venza', 'sienna', 'passport', 'accrod crosstour',
                'element', 'tundra', 'sequoia', 'corolla hatchback', '4runner',
                'echo', 'tercel', 'mr2 spyder', 'fj cruiser', 'corolla im',
                'c-hr', 'civic hatchback', '86', 's2000', 'supra', 'insight',
                'clarity', 'cr-z', 'prius prime', 'prius plug-in', 'prius c', 'prius v'
            ])
            st.selectbox("Body Type", key="body_type", options=[
                "suv", "sedan", "pickup", "hatchback", "minivan", "coupe", "wagon",
                "convertible", "cargo_van", "mini_mpv", "passenger_van", "cutaway",
                "targa", "micro_car", "car_van", "chassis_cab", "crossover",
                "combi", "roadster", "commercial_wagon"
            ])
            st.selectbox("Vehicle Type", key="vehicle_type", options=["car", "truck"])

        # Column 2 inputs
        with col2:
            st.number_input("Year", value=2001, min_value=1886, step=1, key="year")
            st.number_input("Engine size (L)", value=1.5, key="engine_size", min_value=0.9, step=0.1)
            st.selectbox("Drivetrain", ["fwd", "rwd", "4wd"], key="drivetrain")
            st.selectbox("Transmission", ["automatic", "manual"], key="transmission")

        # Column 3 inputs
        with col3:
            st.selectbox("Make", key="make", index=0, options=['toyota', 'honda'])
            st.selectbox("Province", index=0, key="province", options=[
                'nb', 'qc', 'bc', 'on', 'ab', 'mb', 'sk', 'ns',
                'pe', 'nl', 'yt', 'nc', 'oh', 'sc'
            ])
            st.selectbox("Fuel Type", ["gasoline", "hybrid", "diesel", "electric"], key="fuel_type")
            st.selectbox("Engine Block", ["i", "v", "h"], key="engine_block")

        # Submit button
        st.form_submit_button("Calculate", type="primary", on_click=make_prediction, kwargs=dict(pipe=pipe))

    # Display the prediction
    if st.session_state["pred"] is not None:
        st.subheader(f"Predicted Price of Reused Car: ${st.session_state['pred']}")
    else:
        st.write("Calculate to get predicted price")

    # Optional debug: show all state values
    if st.checkbox("Show session state / debug"):
        st.write(st.session_state)
