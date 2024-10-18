# Thermia API Server

Thermia API Server is a Python-based server that provides an interface for monitoring and controlling a Thermia heat pump. It exposes data via a Prometheus-compatible metrics endpoint and allows for setting the temperature through a simple API.

## Features
- Exposes various Thermia heat pump metrics in Prometheus format for easy monitoring.
- Provides an API to set the desired temperature of the heat pump.
- Built on top of the [python-thermia-online-api](https://github.com/klejejs/python-thermia-online-api), allowing seamless interaction with the Thermia Online API.

## Getting Started

### Prerequisites
- Docker installed on your system.
- Access to the Thermia Online account (username and password).

### Running the Server

You can run the server using Docker. An example `.env` file is provided below to set up the required environment variables.

#### 1. Create an `.env` file
Create a `.env` file based on the example below:

```env
# .env
USERNAME=your_thermia_username
PASSWORD=your_thermia_password
```

#### 2. Pull the Docker Image
Pull the latest Docker image from Docker Hub:

```bash
docker pull gjorret/thermia-api-server:latest
```

#### 3. Run the Docker Container
Run the Docker container, passing in the `.env` file:

```bash
docker run -d --env-file .env -p 8000:8000 gjorret/thermia-api-server:latest
```
Or just add the environment variables directly in the docker run command:
```bash
docker run -d --env USERNAME='your_username' --env PASSWORD='your_password' -p 8000:8000 gjorret/thermia-api-server
```

The server will start and be accessible at `http://localhost:8000`.

### API Endpoints

#### GET `/metrics`

- **Description:** This endpoint exposes the Prometheus-formatted metrics of the Thermia heat pump.

- **Response:** A plain text response in Prometheus metrics format containing various heat pump statistics, including temperatures, operational times, and heating effect.

- **Example Response:**

    ```
    # HELP outdoor_temperature Outdoor Temperature of the heat pump
    # TYPE outdoor_temperature gauge
    outdoor_temperature{heat_pump_name="Jordvarme"} 10.0
    # HELP hot_water_temperature Hot Water Temperature of the heat pump
    # TYPE hot_water_temperature gauge
    hot_water_temperature{heat_pump_name="Jordvarme"} 49.0
    # HELP heating_effect Heating Effect of the heat pump
    # TYPE heating_effect gauge
    heating_effect{heat_pump_name="Jordvarme"} 22.0
    ```

#### POST `/api/temperature/set/<temperature>`

- **Description:** This endpoint allows you to set the desired temperature of the Thermia heat pump.

- **Parameters:**

    - `temperature`: Integer value specifying the desired temperature in degrees Celsius.

- **Example Request:**

    ```bash
    curl -X POST http://localhost:8000/api/temperature/set/22
    ```

- **Response:**

   - **200 OK:** The temperature was set successfully.

      ```json
      {
         "message": "Temperature set to 22 degrees."
      }
      ```

### Development

#### Prerequisites
- Python 3.12 or higher
- Pip

#### Setup
1. **Clone the repository**:

   ```bash
   git clone https://github.com/gjorret/thermia-api-server.git
   cd thermia-api-server
   ```

2. **Create a virtual environment and install dependencies**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the server locally**:

   ```bash
   export USERNAME=your_thermia_username
   export PASSWORD=your_thermia_password
   gunicorn -b 0.0.0.0:8000 src.app:app
   ```

### Configuration

#### Environment Variables
- `USERNAME`: Thermia Online account username.
- `PASSWORD`: Thermia Online account password.

#### Docker Configuration
- To change the port or environment variables, modify the `.env` file or the Docker run command.

### Reference to Original Project
This project is built on top of the [python-thermia-online-api](https://github.com/klejejs/python-thermia-online-api). Special thanks to the original author for providing the Thermia Online API Python interface.

### Docker Hub
The Docker image is available on Docker Hub at [gjorret/thermia-api-server](https://hub.docker.com/r/gjorret/thermia-api-server).

### License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Contact
For any questions or issues, feel free to reach out through the GitHub repository's issues section.