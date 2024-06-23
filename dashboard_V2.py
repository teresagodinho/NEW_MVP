server = app.server
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "72ca73fc-56a0-41b2-8ad5-341ce49edd16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: dash in /opt/anaconda3/lib/python3.11/site-packages (2.17.0)\n",
      "Requirement already satisfied: dash-bootstrap-components in /opt/anaconda3/lib/python3.11/site-packages (1.6.0)\n",
      "Requirement already satisfied: pandas in /opt/anaconda3/lib/python3.11/site-packages (2.1.4)\n",
      "Requirement already satisfied: scikit-learn in /opt/anaconda3/lib/python3.11/site-packages (1.2.2)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (2.2.5)\n",
      "Requirement already satisfied: Werkzeug<3.1 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (2.2.3)\n",
      "Requirement already satisfied: plotly>=5.0.0 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (5.9.0)\n",
      "Requirement already satisfied: dash-html-components==2.0.0 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: dash-core-components==2.0.0 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: dash-table==5.0.0 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (5.0.0)\n",
      "Requirement already satisfied: importlib-metadata in /opt/anaconda3/lib/python3.11/site-packages (from dash) (7.0.1)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in /opt/anaconda3/lib/python3.11/site-packages (from dash) (4.9.0)\n",
      "Requirement already satisfied: requests in /opt/anaconda3/lib/python3.11/site-packages (from dash) (2.31.0)\n",
      "Requirement already satisfied: retrying in /opt/anaconda3/lib/python3.11/site-packages (from dash) (1.3.4)\n",
      "Requirement already satisfied: nest-asyncio in /opt/anaconda3/lib/python3.11/site-packages (from dash) (1.6.0)\n",
      "Requirement already satisfied: setuptools in /opt/anaconda3/lib/python3.11/site-packages (from dash) (68.2.2)\n",
      "Requirement already satisfied: numpy<2,>=1.23.2 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in /opt/anaconda3/lib/python3.11/site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: scipy>=1.3.2 in /opt/anaconda3/lib/python3.11/site-packages (from scikit-learn) (1.11.4)\n",
      "Requirement already satisfied: joblib>=1.1.1 in /opt/anaconda3/lib/python3.11/site-packages (from scikit-learn) (1.2.0)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/anaconda3/lib/python3.11/site-packages (from scikit-learn) (2.2.0)\n",
      "Requirement already satisfied: Jinja2>=3.0 in /opt/anaconda3/lib/python3.11/site-packages (from Flask<3.1,>=1.0.4->dash) (3.1.3)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in /opt/anaconda3/lib/python3.11/site-packages (from Flask<3.1,>=1.0.4->dash) (2.0.1)\n",
      "Requirement already satisfied: click>=8.0 in /opt/anaconda3/lib/python3.11/site-packages (from Flask<3.1,>=1.0.4->dash) (8.1.7)\n",
      "Requirement already satisfied: tenacity>=6.2.0 in /opt/anaconda3/lib/python3.11/site-packages (from plotly>=5.0.0->dash) (8.2.2)\n",
      "Requirement already satisfied: six>=1.5 in /opt/anaconda3/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in /opt/anaconda3/lib/python3.11/site-packages (from Werkzeug<3.1->dash) (2.1.3)\n",
      "Requirement already satisfied: zipp>=0.5 in /opt/anaconda3/lib/python3.11/site-packages (from importlib-metadata->dash) (3.17.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/anaconda3/lib/python3.11/site-packages (from requests->dash) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.11/site-packages (from requests->dash) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/anaconda3/lib/python3.11/site-packages (from requests->dash) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.11/site-packages (from requests->dash) (2024.6.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install dash dash-bootstrap-components pandas scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dfa8c5e2-89d4-4308-8f64-032c01431b21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: imbalanced-learn in /opt/anaconda3/lib/python3.11/site-packages (0.11.0)\n",
      "Requirement already satisfied: numpy>=1.17.3 in /opt/anaconda3/lib/python3.11/site-packages (from imbalanced-learn) (1.26.4)\n",
      "Requirement already satisfied: scipy>=1.5.0 in /opt/anaconda3/lib/python3.11/site-packages (from imbalanced-learn) (1.11.4)\n",
      "Requirement already satisfied: scikit-learn>=1.0.2 in /opt/anaconda3/lib/python3.11/site-packages (from imbalanced-learn) (1.2.2)\n",
      "Requirement already satisfied: joblib>=1.1.1 in /opt/anaconda3/lib/python3.11/site-packages (from imbalanced-learn) (1.2.0)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/anaconda3/lib/python3.11/site-packages (from imbalanced-learn) (2.2.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install imbalanced-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7323174f-7765-4557-a38c-baa6412ccd86",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://0.0.0.0:8204/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x168a34690>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import dash\n",
    "import numpy as np\n",
    "from dash import dcc, html\n",
    "from dash.dependencies import Input, Output, State\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split, GridSearchCV\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from imblearn.over_sampling import SMOTE\n",
    "import dash_bootstrap_components as dbc\n",
    "from dash import dash_table\n",
    "import plotly.express as px\n",
    "import plotly.figure_factory as ff\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.cluster import KMeans\n",
    "\n",
    "# Load the dataset\n",
    "data = pd.read_csv('/Users/teresagodinho/Desktop/loan/loan_balanced_6040.csv')\n",
    "\n",
    "# Data preprocessing\n",
    "X = data[['annual_inc', 'term', 'loan_amnt', 'home_ownership_OWN']]\n",
    "y = data['loan_status']\n",
    "\n",
    "# Apply SMOTE to balance the dataset\n",
    "smote = SMOTE(random_state=42)\n",
    "X_resampled, y_resampled = smote.fit_resample(X, y)\n",
    "\n",
    "# Split the dataset into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)\n",
    "\n",
    "# Define the Random Forest Classifier with GridSearchCV\n",
    "param_grid = {\n",
    "    'n_estimators': [50, 100, 200],\n",
    "    'max_features': ['sqrt', 'log2'],\n",
    "    'max_depth': [4, 6, 8, 10],\n",
    "    'criterion': ['gini', 'entropy']\n",
    "}\n",
    "\n",
    "grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)\n",
    "grid_search.fit(X_train, y_train)\n",
    "\n",
    "# Best model from GridSearchCV\n",
    "model = grid_search.best_estimator_\n",
    "\n",
    "# Prepare data for linear regression to predict interest rates\n",
    "X_interest = data[['loan_amnt', 'open_acc', 'delinq_2yrs', 'term']]\n",
    "y_interest = data['int_rate']\n",
    "\n",
    "# Train a Linear Regression model for predicting interest rates\n",
    "lin_reg_model = LinearRegression()\n",
    "lin_reg_model.fit(X_interest, y_interest)\n",
    "\n",
    "# Standardize data for clustering\n",
    "scaler = StandardScaler()\n",
    "data_scaled = scaler.fit_transform(data[['annual_inc', 'loan_amnt']])\n",
    "\n",
    "# Apply KMeans clustering\n",
    "kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)\n",
    "data['cluster'] = kmeans.fit_predict(data_scaled)\n",
    "\n",
    "# Compute default probabilities for each client using the Random Forest Classifier\n",
    "data['probability_of_default'] = model.predict_proba(data[['annual_inc', 'term', 'loan_amnt', 'home_ownership_OWN']])[:, 1]\n",
    "data.sort_values(by='probability_of_default', ascending=False, inplace=True)\n",
    "\n",
    "# Initialize the Dash app with Bootstrap theme\n",
    "app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])\n",
    "\n",
    "# Define the layout of the app\n",
    "app.layout = dbc.Container(\n",
    "    fluid=True,\n",
    "    children=[\n",
    "        dbc.Row(\n",
    "            dbc.Col(html.Img(src=\"/assets/LendSmart_logo.png\", height=\"100px\", style={\"display\": \"block\", \"margin-left\": \"auto\", \"margin-right\": \"auto\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "        ),\n",
    "        dbc.Row(\n",
    "            dbc.Col(\n",
    "                dcc.Tabs(id=\"tabs-example\", value='tab-1', children=[\n",
    "                    dcc.Tab(label='Main Page', value='tab-1'),\n",
    "                    dcc.Tab(label='Background Information', value='tab-2'),\n",
    "                    dcc.Tab(label='New Client Default Prediction', value='tab-3'),\n",
    "                    dcc.Tab(label='Client Risk Segmentation', value='tab-4'),\n",
    "                ])\n",
    "            )\n",
    "        ),\n",
    "        html.Div(id='tabs-content-example')\n",
    "    ],\n",
    "    style={\"background-color\": \"#ffffff\"}\n",
    ")\n",
    "\n",
    "# Define callback to render content based on selected tab\n",
    "@app.callback(\n",
    "    Output('tabs-content-example', 'children'),\n",
    "    Input('tabs-example', 'value')\n",
    ")\n",
    "def render_content(tab):\n",
    "    if tab == 'tab-1':\n",
    "        return html.Div([\n",
    "            html.Div(\n",
    "                \"This dashboard helps a US loan mortgage company identify and manage at-risk clients. Using machine learning models and statistical analysis, it predicts loan defaults and provides actionable insights. Amid rising US mortgage delinquency rates due to economic uncertainty (Financial Times), this tool enables early identification of potential defaults and better management of at-risk clients, ensuring financial stability and improved loan portfolio management.\", \n",
    "                style={\"text-align\": \"center\", \"color\": \"white\", \"padding\": \"20px\", \"border-radius\": \"10px\", \"font-size\": \"20px\", \"margin-bottom\": \"20px\", \"margin-top\": \"20px\", \"background-color\": \"#1B49A4\"}\n",
    "            ),\n",
    "        ])\n",
    "    elif tab == 'tab-2':\n",
    "        return html.Div([\n",
    "            html.Div(\n",
    "                \"Explore various graphs that describe our dataset, which underpins the predictive tools used in the following tabs. Gain insights into loan distributions, income levels, interest rates, and more.\", \n",
    "                style={\"text-align\": \"center\", \"color\": \"white\", \"padding\": \"20px\", \"border-radius\": \"10px\", \"font-size\": \"20px\", \"margin-bottom\": \"20px\", \"margin-top\": \"20px\", \"background-color\": \"#1B49A4\"}\n",
    "            ),\n",
    "    \n",
    "            dcc.Dropdown(\n",
    "                id='dropdown-selection',\n",
    "                options=[\n",
    "                    {'label': 'Correlation Heatmap', 'value': 'heatmap'},\n",
    "                    {'label': 'Distribution of Loan Status', 'value': 'loan_status'},\n",
    "                    {'label': 'Distribution of Loan Amounts', 'value': 'loan_amounts'},\n",
    "                    {'label': 'Distribution of Annual Incomes', 'value': 'annual_incomes'},\n",
    "                    {'label': 'Distribution of Interest Rates', 'value': 'interest_rates'}\n",
    "                ],\n",
    "                value='heatmap'\n",
    "            ),\n",
    "            html.Div(id='display-selected-value', style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'margin-top': '20px'})\n",
    "        ])\n",
    "    elif tab == 'tab-3':\n",
    "        return dbc.Container(\n",
    "            fluid=True,\n",
    "            children=[\n",
    "                dbc.Row(\n",
    "                    dbc.Col(\n",
    "                        html.P(\"Enter your information to receive a personalized loan recommendation in seconds. Our tool quickly evaluates your eligibility, helping you save time and determine the feasibility of your loan application. If your loan is denied, you will receive a recommendation. If your loan is approved, we will suggest an interest rate.\", \n",
    "                               style={\"text-align\": \"center\", \"color\": \"white\", \"padding\": \"20px\", \"margin-top\": \"20px\", \"border-radius\": \"10px\", \"font-size\": \"20px\", \"margin-bottom\": \"20px\",\"background-color\": \"#1B49A4\"}),\n",
    "                        width=12\n",
    "                    )\n",
    "                ),\n",
    "                dbc.Row([\n",
    "                    dbc.Col(html.Label('Annual Income', style={\"color\": \"#2c3e50\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "                    dbc.Col(dcc.Input(id='annual-income', type='number', value=120000, min=0, max=1000000, style={\"width\": \"100%\", \"padding\": \"10px\"}), width={\"size\": 6, \"offset\": 3})\n",
    "                ]),\n",
    "                dbc.Row([\n",
    "                    dbc.Col(html.Label('Loan Term (months)', style={\"color\": \"#2c3e50\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "                    dbc.Col(dcc.Input(id='loan-term', type='number', value=36, min=1, max=360, style={\"width\": \"100%\", \"padding\": \"10px\"}), width={\"size\": 6, \"offset\": 3})\n",
    "                ]),\n",
    "                dbc.Row([\n",
    "                    dbc.Col(html.Label('Loan Amount', style={\"color\": \"#2c3e50\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "                    dbc.Col(dcc.Input(id='loan-amount', type='number', value=300000, min=0, max=1000000, style={\"width\": \"100%\", \"padding\": \"10px\"}), width={\"size\": 6, \"offset\": 3})\n",
    "                ]),\n",
    "                dbc.Row([\n",
    "                    dbc.Col(html.Label('Home Ownership (OWN=1, RENT=0)', style={\"color\": \"#2c3e50\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "                    dbc.Col(dcc.Input(id='home-ownership', type='number', value=1, min=0, max=1, style={\"width\": \"100%\", \"padding\": \"10px\"}), width={\"size\": 6, \"offset\": 3})\n",
    "                ]),\n",
    "                dbc.Row([\n",
    "                    dbc.Col(html.Label('Number of Open Accounts', style={\"color\": \"#2c3e50\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "                    dbc.Col(dcc.Input(id='class-open-acc', type='number', value=5, min=0, max=50, style={\"width\": \"100%\", \"padding\": \"10px\"}), width={\"size\": 6, \"offset\": 3})\n",
    "                ]),\n",
    "                dbc.Row([\n",
    "                    dbc.Col(html.Label('Delinquencies in Last 2 Years 1=YES 0=NO', style={\"color\": \"#2c3e50\"}), width={\"size\": 6, \"offset\": 3}),\n",
    "                    dbc.Col(dcc.Input(id='class-delinq-2yrs', type='number', value=0, min=0, max=50, style={\"width\": \"100%\", \"padding\": \"10px\"}), width={\"size\": 6, \"offset\": 3})\n",
    "                ]),\n",
    "                dbc.Row(\n",
    "                    dbc.Col(\n",
    "                        html.Button('Predict', id='predict-button', n_clicks=0, style={\"background-color\": \"#1B49A4\", \"color\": \"white\", \"padding\": \"20px 25px\", \"border-radius\": \"20px\", \"font-size\": \"20px\"}),\n",
    "                        width={\"size\": 6, \"offset\": 3},\n",
    "                        style={\"padding-top\": \"20px\",\"display\": \"flex\"}\n",
    "                    ),\n",
    "                    justify=\"start\"\n",
    "                ),\n",
    "                dbc.Row(\n",
    "                    dbc.Col(\n",
    "                        html.Div(\n",
    "                            [\n",
    "                                html.H3('Prediction', style={\"color\": \"white\"}),\n",
    "                                html.Div(id='prediction-result', style={\"color\": \"white\"}),\n",
    "                                html.H3('Prediction Probability', style={\"color\": \"white\"}),\n",
    "                                html.Div(id='prediction-probability', style={\"color\": \"white\"}),\n",
    "                                html.H3(id='recommendations-title', style={\"color\": \"white\"}),\n",
    "                                html.Div(id='recommendations', style={\"color\": \"white\"})\n",
    "                            ],\n",
    "                            style={\"padding\": \"20px\", \"backgroundColor\": \"#1B49A4\", \"borderRadius\": \"10px\", \"margin-top\": \"20px\"}  # Adding top margin to space out results}\n",
    "                        ),\n",
    "                        width=6, style={\"padding\": \"10px\"}\n",
    "                    ),\n",
    "                    justify=\"center\"\n",
    "                )\n",
    "            ]\n",
    "        )\n",
    "    elif tab == 'tab-4':\n",
    "        risk_levels = data.pivot_table(values='loan_status', \n",
    "                                       index=pd.cut(data['loan_amnt'], bins=range(0, 105000, 5000)), \n",
    "                                       columns=pd.cut(data['annual_inc'], bins=range(0, 1050000, 50000)), \n",
    "                                       aggfunc='mean')\n",
    "        risk_levels = risk_levels.fillna(0)  # fill NaNs with zeros\n",
    "\n",
    "        x_labels = [f\"${i*5000}\" for i in range(21)]  # generate loan amount bins labels\n",
    "        y_labels = [f\"${i*50000}\" for i in range(21)]  # generate annual income bins labels\n",
    "\n",
    "        heatmap = px.imshow(\n",
    "            risk_levels.values,\n",
    "            labels=dict(x=\"Loan Amount\", y=\"Annual Income\", color=\"Default Probability\"),\n",
    "            x=x_labels[:risk_levels.shape[1]],\n",
    "            y=y_labels[:risk_levels.shape[0]],\n",
    "            color_continuous_scale='RdYlGn_r',\n",
    "        )\n",
    "\n",
    "        heatmap.update_layout(\n",
    "            title='Client Risk Segmentation Heatmap',\n",
    "            xaxis_title='Loan Amount',\n",
    "            yaxis_title='Annual Income',\n",
    "            autosize=False,\n",
    "            width=800,\n",
    "            height=800\n",
    "        )\n",
    "        \n",
    "        datatable = dash_table.DataTable(\n",
    "            id='client-table',\n",
    "            columns=[\n",
    "                {\"name\": \"Client\", \"id\": \"client\"},\n",
    "                {\"name\": \"Annual Income\", \"id\": \"annual_inc\"},\n",
    "                {\"name\": \"Loan Term\", \"id\": \"term\"},\n",
    "                {\"name\": \"Loan Amount\", \"id\": \"loan_amnt\"},\n",
    "                {\"name\": \"Home Ownership\", \"id\": \"home_ownership\"},\n",
    "                {\"name\": \"Delinquencies in Last 2 Years\", \"id\": \"delinq_2yrs\"},\n",
    "                {\"name\": \"Probability of Default\", \"id\": \"probability_of_default\"},\n",
    "                {\"name\": \"Current Interest Rate\", \"id\": \"int_rate\"},\n",
    "                {\"name\": \"Suggested Interest Rate\", \"id\": \"suggested_interest_rate\"}\n",
    "            ],\n",
    "            data=data[data['probability_of_default'] < 1].assign(\n",
    "                client=lambda x: x.index + 1,\n",
    "                home_ownership=lambda x: x['home_ownership_OWN'].map({1: 'OWN', 0: 'RENT'}),\n",
    "                suggested_interest_rate=lambda x: lin_reg_model.predict(\n",
    "                    x[['loan_amnt', 'open_acc', 'delinq_2yrs', 'term']]\n",
    "                ).round(2)\n",
    "            ).to_dict('records'),\n",
    "            sort_action=\"native\",\n",
    "            sort_mode=\"single\",\n",
    "            style_table={'overflowX': 'auto'},\n",
    "            style_cell={\n",
    "                'height': 'auto',\n",
    "                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',\n",
    "                'whiteSpace': 'normal'\n",
    "            }\n",
    "        )\n",
    "\n",
    "        return html.Div([\n",
    "            html.H4(\"Client Risk Segmentation Analysis\", style={'textAlign': 'center', 'margin-top': '20px'}),\n",
    "            html.P(\n",
    "                \"This heatmap visualizes the risk segmentation of clients based on their loan amounts and annual incomes. \"\n",
    "                \"Each cell represents the default probability for a specific segment, with colors ranging from green (low risk) to red (high risk). \"\n",
    "                \"By analyzing this heatmap, we can identify which client segments are more likely to default on their loans, allowing for better risk management and targeted strategies.\",\n",
    "                style={\"text-align\": \"center\", \"color\": \"white\", \"backgroundColor\": \"#1B49A4\", \"padding\": \"10px\", \"border-radius\": \"5px\", \"font-size\": \"20px\", \"margin-top\": \"20px\", \"margin-bottom\": \"15px\"}\n",
    "            ),\n",
    "        \n",
    "            dcc.Graph(figure=heatmap, style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'margin-top': '20px'}),\n",
    "            html.Div([\n",
    "                html.H4(\"Client Risk Evaluation and Interest Rate Recommendations\", style={'textAlign': 'center', 'margin-top': '20px'}),\n",
    "                html.Div(\"We're using our random forest model to calculate a new probability of default for all existing clients. Based on these probabilities, we've also calculated suggested interest rates. The goal is to improve the management of the company's at-risk clients.\",\n",
    "                         style={\"text-align\": \"center\", \"color\": \"white\", \"backgroundColor\": \"#1B49A4\", \"padding\": \"10px\", \"border-radius\": \"5px\", \"font-size\": \"20px\", \"margin-top\": \"30px\", \"margin-bottom\": \"20px\"}),\n",
    "                datatable\n",
    "            ], style={'padding-top': '20px'})\n",
    "        ])\n",
    "\n",
    "# Define the callback to update the displayed graph based on dropdown selection\n",
    "@app.callback(\n",
    "    Output('display-selected-value', 'children'),\n",
    "    [Input('dropdown-selection', 'value')]\n",
    ")\n",
    "def update_output(value):\n",
    "    if value == 'heatmap':\n",
    "        correlation_matrix = data[['loan_amnt', 'term', 'int_rate', 'installment', 'annual_inc', \n",
    "                                   'delinq_2yrs', 'home_ownership_OWN', 'home_ownership_RENT', 'open_acc', 'loan_status']].corr()\n",
    "        fig = px.imshow(correlation_matrix, \n",
    "                        labels={'color':'Correlation'},\n",
    "                        x=['Loan Amount', 'Loan Term', 'Interest Rate', 'Installment', 'Annual Income', \n",
    "                           'Delinquency in the Last 2 Years', 'Home Owner', 'Home Renter', 'Number of Open Accounts', 'Loan Status'],\n",
    "                        y=['Loan Amount', 'Loan Term', 'Interest Rate', 'Installment', 'Annual Income', \n",
    "                           'Delinquency in the Last 2 Years', 'Home Owner', 'Home Renter', 'Number of Open Accounts', 'Loan Status'],\n",
    "                        color_continuous_scale='RdBu_r')\n",
    "        fig.update_layout(title='Correlation Heatmap')\n",
    "        return dcc.Graph(figure=fig, style={'textAlign': 'center', 'margin-top': '20px'})\n",
    "    elif value == 'loan_status':\n",
    "        loan_status_counts = data['loan_status'].value_counts().reset_index()\n",
    "        loan_status_counts.columns = ['Loan Status', 'Count']\n",
    "        fig = px.bar(loan_status_counts, \n",
    "                     x='Loan Status', \n",
    "                     y='Count',\n",
    "                     labels={'Loan Status': 'Loan Status', 'Count': 'Number of Loans'},\n",
    "                     title='Distribution of Loan Status')\n",
    "        return dcc.Graph(figure=fig)\n",
    "    elif value == 'loan_amounts':\n",
    "        fig = px.histogram(data, x='loan_amnt', nbins=50, title='Distribution of Loan Amounts')\n",
    "        fig.update_layout(xaxis_title='Loan Amount ($)', yaxis_title='Count')\n",
    "        return dcc.Graph(figure=fig)\n",
    "    elif value == 'annual_incomes':\n",
    "        fig = px.histogram(data, x='annual_inc', nbins=50, title='Distribution of Annual Incomes')\n",
    "        fig.update_layout(xaxis_title='Annual Income ($)', yaxis_title='Count')\n",
    "        return dcc.Graph(figure=fig)\n",
    "    elif value == 'interest_rates':\n",
    "        fig = px.histogram(data, x='int_rate', nbins=50, title='Distribution of Interest Rates')\n",
    "        fig.update_layout(xaxis_title='Interest Rate (%)', yaxis_title='Count')\n",
    "        return dcc.Graph(figure=fig)\n",
    "\n",
    "# Define the callback to update the predictions\n",
    "@app.callback(\n",
    "    [Output('prediction-result', 'children'),\n",
    "     Output('prediction-probability', 'children'),\n",
    "     Output('recommendations-title', 'children'),\n",
    "     Output('recommendations', 'children')],\n",
    "    [Input('predict-button', 'n_clicks')],\n",
    "    [State('annual-income', 'value'),\n",
    "     State('loan-term', 'value'),\n",
    "     State('loan-amount', 'value'),\n",
    "     State('home-ownership', 'value'),\n",
    "     State('class-open-acc', 'value'),\n",
    "     State('class-delinq-2yrs', 'value')]\n",
    ")\n",
    "def update_prediction(n_clicks, annual_income, loan_term, loan_amount, home_ownership, open_acc, delinq_2yrs):\n",
    "    if n_clicks > 0:\n",
    "        input_data = pd.DataFrame({\n",
    "            'annual_inc': [annual_income],\n",
    "            'term': [loan_term],\n",
    "            'loan_amnt': [loan_amount],\n",
    "            'home_ownership_OWN': [home_ownership]\n",
    "        })\n",
    "\n",
    "        prediction = model.predict(input_data)\n",
    "        prediction_proba = model.predict_proba(input_data)\n",
    "\n",
    "        if prediction[0] == 1:\n",
    "            result = 'Loan Denied'\n",
    "            probability = f\"{prediction_proba[0][1]*100:.2f}% probability of default\"\n",
    "            recommendations_title = 'Recommendations'\n",
    "            recommendations = \"\"\"\n",
    "            - Reduce Loan Amount: A lower loan amount reduces the repayment burden, which can decrease the risk of default.\n",
    "            - Extend Loan Term: Smaller monthly payments can be easier to manage, reducing the risk of default.\n",
    "            \"\"\"\n",
    "            return result, probability, recommendations_title, recommendations\n",
    "        else:\n",
    "            result = 'Loan Accepted'\n",
    "            probability = f\"{prediction_proba[0][1]*100:.2f}% probability of default\"\n",
    "\n",
    "            # Predict the interest rate using the linear regression model\n",
    "            input_data_for_rate = pd.DataFrame({\n",
    "                'loan_amnt': [loan_amount],\n",
    "                'open_acc': [open_acc],\n",
    "                'delinq_2yrs': [delinq_2yrs],\n",
    "                'term': [loan_term]\n",
    "            })\n",
    "\n",
    "            predicted_rate = lin_reg_model.predict(input_data_for_rate)\n",
    "            recommended_rate = f\"The suggested interest rate is {predicted_rate[0]:.2f}%.\"\n",
    "\n",
    "            recommendations_title = 'Suggested Interest Rate'\n",
    "            return result, probability, recommendations_title, recommended_rate\n",
    "    return '', '', '', ''\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True, host='0.0.0.0', port=8204)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "375832c7-ff45-49f9-bf65-8d40dc6bb551",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
