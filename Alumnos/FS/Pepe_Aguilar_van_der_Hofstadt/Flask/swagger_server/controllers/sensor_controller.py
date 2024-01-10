import connexion
import six

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server import util


def get_temperature(sensor_id):  # noqa: E501
    """Get the temperature of the robot

     # noqa: E501

    :param sensor_id: sensor ID
    :type sensor_id: str

    :rtype: Measure
    """
    return 'do some magic!'
