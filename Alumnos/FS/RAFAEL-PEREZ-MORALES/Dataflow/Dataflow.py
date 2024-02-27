import apache_beam as beam
from apache_beam.runners import DataflowRunner
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.transforms.window as window
from apache_beam.metrics import Metrics

from apache_beam.ml.inference.base import ModelHandler
from apache_beam.ml.inference.base import RunInference

from google.cloud.vision_v1.types import Feature
from google.cloud import vision

import argparse
import requests
import logging
import json
import re
import io