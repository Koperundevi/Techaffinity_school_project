from tastypie.api import Api
from api import MarkResource

v1_api = Api(api_name='v1')
v1_api.register(MarkResource())