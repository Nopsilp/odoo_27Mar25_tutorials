from odoo import models, fields, api, _
import meteomatics.api as meteomatics_api
import logging
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)


class WeatherData(models.Model):
    _name = 'weather.data'
    _description = 'Weather Data through meteomatics.api'
    
    location = fields.Char(string='Location')
    temperature = fields.Float(string='Temperature')
    condition = fields.Char(string='Condition', default='Clear')

    def store_weather_data(self):
        data = self._fetch_weather_data()
        if data:
            _logger.info(f'Weather data fetched: {data}')
            self.env['weather.data'].create(data)
        else:
            _logger.warning('Weather data not stored due to fetch failure')


    def _fetch_weather_data(self):
    # fetch weather data from meteomatics.api
        username = 'test_test_odoo'
        password = '5x2iUkP6iG'

        coordinates = [(13.736717, 100.523186)]
        weather_params = ["t_2m:C"]
        model = 'mix'

        #set the time
        interval = timedelta(hours=1)
        starttime = datetime.now().replace(minute=0, second=0, microsecond=0)
        endtime = starttime + timedelta(days=1)

        try:
            result = meteomatics_api.query_time_series(
                coordinates, starttime, endtime, interval,
                weather_params, username, password, model
            )
            if result.empty:
                _logger.warning('Empty response from API')
                return None
            
            if not result["t_2m:C"].any():
                _logger.warning('Expected temperature data not found')
                return None

            temperature = result["t_2m:C"].iloc[0]

            return {
                'location': 'Bangkok',
                'temperature': temperature,
                'condition': 'Clear'
            }

        except ConnectionError:
            _logger.warning('API connection failed')
            return None
        
        except KeyError as keyerror:
            _logger.warning(f'Missing expected data field: {keyerror}')
            return None

        except Exception as e:
            _logger.warning(f'Unexpected error occurred: {e}')
            return None
        
        finally:
            _logger.info(f'Execution is completed.')