# Green Lungs
### Tree Recommendations and Pollution Impact Estimation

Green Lungs is a web application that helps users identify suitable tree species for urban planting and estimate how those planting choices could affect pollution levels over time.

The application combines available environmental data, site conditions, and tree-species information to support planting decisions. Along with recommending which trees may be suitable for a location, it aims to estimate the potential environmental impact of those choices, helping users compare planting options and plan urban green spaces more effectively.

## Live Application

- **Website:** [Green Lungs](http://greenlungs-env.eba-npiprwiw.ap-southeast-2.elasticbeanstalk.com/)
- **API Documentation:** [Swagger UI](http://greenlungs-env.eba-npiprwiw.ap-southeast-2.elasticbeanstalk.com/docs)
- **Health Check:** [API Status](http://greenlungs-env.eba-npiprwiw.ap-southeast-2.elasticbeanstalk.com/api/health)

## Problem Statement

Urban areas face high pollution levels and limited green spaces. Tree plantation can help improve urban environments, but the results depend on choosing suitable species and planting them in appropriate locations.

Different tree species have different growth characteristics, water requirements, and abilities to capture certain air pollutants. The environmental impact also depends on the number of trees planted, local conditions, and how well the trees survive.

Green Lungs addresses two connected questions:

- **Which trees should be planted, and where?**
- **How might planting those trees affect pollution levels over time?**

The aim is to connect tree-planting recommendations with estimates of their potential environmental impact.

## Features

- **Tree-species recommendations:** Explore suitable species using available environmental and site information.
- **Location-based planning:** Work with supported study locations and their available data.
- **Planting constraints:** Consider factors such as available space and water availability where supported by the application.
- **Pollution impact estimation:** Estimate potential changes in pollution associated with planting choices, where supported by the implemented model.
- **Environmental projections:** Explore possible future outcomes using the application's projection functionality.
- **Web interface and API:** View results through the website or access supported functionality through API endpoints.
- **Cloud deployment:** Access the application online through AWS Elastic Beanstalk.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python |
| API framework | FastAPI |
| Application server | Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Containerization | Docker |
| Cloud deployment | AWS Elastic Beanstalk |
| Compute infrastructure | Amazon EC2, managed by Elastic Beanstalk |
| Geocoding | OpenStreetMap Nominatim, where configured |
| Data | Local datasets packaged with the application |

## How It Works

The application follows a workflow that connects environmental data, tree recommendations, and potential pollution impacts.

1. **Location and environmental data:** The application uses the available information for a supported study site.
2. **Species evaluation:** Candidate tree species are evaluated using the recommendation logic and available site conditions.
3. **Planting recommendations:** The system identifies suitable planting options while considering applicable constraints.
4. **Pollution impact estimation:** The application estimates how the selected planting options could influence pollution levels, where supported by the implemented calculations.
5. **Projections and comparison:** Users can explore estimated outcomes to help compare planting choices and support planning decisions.

The purpose is not simply to identify suitable trees, but also to understand the potential environmental benefit of planting them.

## Project Architecture

```text
Environmental and Site Data
            |
            v
     FastAPI Application
            |
            v
   Tree Recommendation Logic
            |
            v
 Species Selection and Allocation
            |
            v
 Estimated Pollution Impact
            |
            v
 Environmental Projections
            |
            v
       Web Interface
```

## AWS Deployment

Green Lungs is deployed on **AWS Elastic Beanstalk using Docker**. The application ZIP was uploaded through the AWS Management Console.

The deployment flow is:

```text
User's Browser
      |
      v
AWS Elastic Beanstalk
      |
      v
Amazon EC2 Instance
      |
      v
Docker Container
      |
      v
FastAPI Application
      |
      +-- Tree Recommendation Logic
      +-- Pollution Impact and Projection Logic
      +-- Packaged Application Data
```

Elastic Beanstalk manages the application environment, while Docker packages and runs the application. Deployment was performed through the AWS web console; the EB CLI was not required.

The application uses its packaged local datasets and any external services configured in the code. Services such as Amazon S3 or Amazon Location Service should not be described as active integrations unless they are actually being used.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/api/health` | Checks application status |
| `GET` | `/api/overview` | Retrieves overview information |
| `POST` | `/api/recommend` | Requests tree recommendations |

The endpoints can be explored and tested through the [interactive API documentation](http://greenlungs-env.eba-npiprwiw.ap-southeast-2.elasticbeanstalk.com/docs).

To check the application's status:

```bash
curl http://greenlungs-env.eba-npiprwiw.ap-southeast-2.elasticbeanstalk.com/api/health
```

## Running the Project Locally

### Requirements

- Python 3.12 or a compatible version
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Vansh-Vaibhav/Green-Lungs.git
cd Green-Lungs
```

Confirm the repository URL and default branch before using these commands.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

Open these addresses in your browser:

- Website: `http://127.0.0.1:8000/`
- API documentation: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/health`

## Running with Docker

Build the image from the project root:

```bash
docker build -t green-lungs .
```

Run the container:

```bash
docker run --rm -p 8000:8000 green-lungs
```

Open `http://127.0.0.1:8000/` to access the application.

Ensure the Docker build includes all required source files, frontend assets, and datasets. Check `.dockerignore` so that required runtime files are not excluded.

## Project Structure

```text
Green-Lungs/
├── data/                 # Application datasets
├── static/               # Frontend files
├── Dockerfile             # Docker image configuration
├── .dockerignore          # Docker build exclusions
├── .gitignore
├── aws_io.py              # Data and integration utilities
├── projections.py         # Projection-related logic
├── requirements.txt       # Python dependencies
├── server.py              # FastAPI application
├── tree_recommender.py    # Tree recommendation logic
└── README.md
```

This structure should match the actual files in the repository.

## Data and Limitations

The application depends on the quality, coverage, and completeness of its environmental and tree-species datasets. Some locations may have more information available than others.

Pollution impact estimates and future projections should be treated as estimates rather than guaranteed outcomes. Actual pollution levels are affected by many factors, including traffic, industrial activity, weather, wind, other emission sources, tree survival, and maintenance.

Tree planting can contribute to environmental improvement, but the magnitude of any pollution reduction depends on the species, number of trees, planting location, and local conditions. Synthetic or estimated data should be clearly distinguished from verified observations.

## Future Improvements

- Add more verified environmental and tree-species data.
- Support additional study locations.
- Improve the estimation of pollution impacts from planting choices.
- Compare estimated results with real measurements collected after plantation.
- Improve missing-data handling and recommendation explanations.
- Add monitoring features to evaluate environmental changes over time.

## Contributors

- [Pranay Bhardwaj](https://github.com/PranayBhardwaj29)
- [Navya Gupta](https://github.com/navyagupta480)
- [Vanshika V](https://github.com/vanshikav660)
- [Vansh Vaibhav](https://github.com/Vansh-Vaibhav)

## Acknowledgements

The project may use environmental data or services from OpenAQ, Open-Meteo, Copernicus CAMS, and OpenStreetMap, depending on the sources included in the current data pipeline. Relevant licences and attribution requirements should be followed.

## Disclaimer

Green Lungs is an environmental planning and decision-support project. Its recommendations and pollution impact estimates depend on the available data and implemented calculations. They do not guarantee a specific reduction in pollution and should be evaluated against real-world measurements and local ecological guidance.
