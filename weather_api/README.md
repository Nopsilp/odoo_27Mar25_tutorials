CLASS WeatherData:
    ATTRIBUTES:
        - location: string
        - temperature: float
        - condition: string = "Clear"

    METHOD fetch_and_store_weather_data():
        data = _fetch_weather_data()
        IF data is not None:
            LOG "Weather data fetched:", data
            CREATE new record in DB with data
        ELSE:
            LOG "Weather data not stored due to fetch failure"

    METHOD _fetch_weather_data():
        SET credentials: username, password
        SET query parameters:
            - coordinates
            - weather_params = ["t_2m:C"] (temperature at 2 meters)
            - model = "mix"
            - interval = "PT1H"
            - start & end time = current UTC time

        TRY:
            result = meteomatics.query_time_series(...)
            IF result is empty:
                LOG "Empty response from API"
                RETURN None
            
            IF "t_2m:C" not in result:
                LOG "Expected temperature data not found"
                RETURN None

            temperature = extract from result["t_2m:C"]
            RETURN {
                "temperature": temperature,
                "location": defined location,
                "condition": inferred or default value
            }

        EXCEPT ConnectionError:
            LOG "API connection failed"
        EXCEPT KeyError:
            LOG "Missing expected data field"
        EXCEPT Exception:
            LOG "Unexpected error occurred"

        RETURN None
