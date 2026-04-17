# Weather App using Flask

This project is a simple web application that provides weather information using the OpenWeather API. It was developed as part of the CS50x course.

## Screenshots

![Weather Info](https://user-images.githubusercontent.com/98171563/228758731-dc106c1e-fe19-4544-81c5-26fe992be801.png)
*Figure 1: Home Page of the Weather App*

## Features

- User can enter a city name to get current weather information.
- Displays temperature, weather description.

## Installation and Setup

To run this project locally, follow these steps:

### Prerequisites

- Python 3.x installed on your system
- pip (Python package installer)
- An API key from [OpenWeather](https://openweathermap.org/api)

### Instructions

1. **Clone the repository**

   ```sh
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```

2. **Install required packages**

   Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

   Install the necessary packages:

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory of the project and add your OpenWeather API key:

   ```env
   OPENWEATHER_API_KEY=your_openweather_api_key
   ```

4. **Run the application**

   Start the Flask server:

   ```sh
   flask run
   ```

   By default, Flask will run the app on `http://127.0.0.1:5000/`.

5. **Usage**

   Open your web browser and go to `http://127.0.0.1:5000/`. Enter a city name in the search bar to get the current weather information for that city.


## Built With

- [Flask](https://flask.palletsprojects.com/)
- [OpenWeather API](https://openweathermap.org/api)
- HTML/CSS for frontend

## Contributing

Contributions are welcome. Please fork this repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.


