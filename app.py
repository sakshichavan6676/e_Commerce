{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdb91741-1178-4679-b415-a77084e635d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import streamlit as st\n",
    "import pickle\n",
    "\n",
    "\n",
    "# Load the saved model\n",
    "with open('model.pkl', 'rb') as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "\n",
    "\n",
    "# UI inputs\n",
    "avg_session = st.number_input(\"Avg. Session Length\")\n",
    "time_app = st.number_input(\"Time on App\")\n",
    "time_web = st.number_input(\"Time on Website\")\n",
    "membership = st.number_input(\"Length of Membership\")\n",
    "\n",
    "# Predict\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(\n",
    "        [[avg_session, time_app, time_web, membership]]\n",
    "    )\n",
    "    st.success(f\"Predicted Yearly Amount Spent: ${prediction[0]:.2f}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
