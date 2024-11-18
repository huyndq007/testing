'''Huy testing app1.py'''
import _thread

from usr.modules.battery import Battery
from usr.modules.history import History
from usr.modules.logging import getLogger
from usr.modules.net_manage import NetManager
from usr.modules.thingsboard import TBDeviceMQTTClient
from usr.modules.power_manage import PowerManage
from usr.modules.aliIot import AliIot, AliIotOTA
from usr.modules.location import GNSS, CellLocator, WiFiLocator, CoordinateSystemConvert

from usr.settings_user import UserConfig
from usr.tracker_tb import Tracker as TBTracker
from usr.tracker_ali import Tracker as AliTracker
from usr.settings import Settings, PROJECT_NAME, FIRMWARE_NAME

log = getLogger(__name__)

log.debug("444")

