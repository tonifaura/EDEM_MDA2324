# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSensorController(BaseTestCase):
    """SensorController integration test stubs"""

    def test_get_temperature(self):
        """Test case for get_temperature

        Get the temperature of the robot
        """
        response = self.client.open(
            '/getLastMeassureBySensor/{sensorID}'.format(sensor_id='sensor_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
