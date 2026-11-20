import contextlib
import io
import unittest
from unittest.mock import patch

import main


class WeatherCliTests(unittest.TestCase):
    def test_city_at_zero_latitude_or_longitude_can_be_looked_up(self):
        for latitude, longitude in ((0.0, 30.0), (15.0, 0.0)):
            with self.subTest(latitude=latitude, longitude=longitude):
                with patch.object(main.sys, "argv", ["main.py", "example"]), patch.object(main, "WeatherService") as provider:
                    service = provider.return_value
                    service.get_coordinates.return_value = (latitude, longitude, "Example")
                    service.get_weather.return_value = {"temperature": 25.0, "windspeed": 8}
                    out = io.StringIO()
                    with contextlib.redirect_stdout(out):
                        main.main()
                    service.get_weather.assert_called_once_with(latitude, longitude)
                    self.assertIn("25.0°C", out.getvalue())

    def test_missing_coordinates_do_not_request_weather(self):
        with patch.object(main.sys, "argv", ["main.py", "missing"]), patch.object(main, "WeatherService") as provider:
            service = provider.return_value
            service.get_coordinates.return_value = (None, None, None)
            with contextlib.redirect_stdout(io.StringIO()):
                main.main()
            service.get_weather.assert_not_called()
