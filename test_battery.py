import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

@pytest.fixture
def monitored_battery(mocker):
    return Battery(100, external_monitor=Mock())


def describe_Battery():

    def describe_init():
        def describe_battery_initializes_without_monitor():
            def capacity_initialized(charged_battery):
                assert charged_battery.mCapacity == 100

            def charge_initialized_to_capacity(charged_battery):
                assert charged_battery.mCharge == 100
            
            def monitor_initialized_to_none(charged_battery):
                assert charged_battery.external_monitor == None

        def describe_battery_initializes_with_monitor():
            def capacity_initialized(monitored_battery):
                assert monitored_battery.mCapacity == 100

            def charge_initialized_to_capacity(monitored_battery):
                assert monitored_battery.mCharge == 100
            
            def monitor_initialized(monitored_battery):
                assert isinstance(monitored_battery.external_monitor, Mock)

    def describe_get_capacity():
        def battery_returns_capacity_when_fully_charged(charged_battery):
            assert charged_battery.getCapacity() == charged_battery.mCapacity == 100
        
        def battery_returns_capacity_when_partially_charged(partially_charged_battery):
            assert partially_charged_battery.getCapacity() == partially_charged_battery.mCapacity == 100

    def describe_get_charge():
        def battery_returns_charge_when_fully_charged(charged_battery):
            assert charged_battery.getCharge() == charged_battery.mCharge == 100
        
        def battery_returns_charge_when_partially_charged(partially_charged_battery):
            assert partially_charged_battery.getCharge() == partially_charged_battery.mCharge == 70

    def describe_recharge():
        def battery_recharges_succesfully(partially_charged_battery):
            assert partially_charged_battery.recharge(20) is True
            assert partially_charged_battery.getCharge() == 90
        
        def battery_does_not_recharge_past_capacity(charged_battery, partially_charged_battery):
            assert charged_battery.recharge(10) is False
            assert charged_battery.getCharge() == 100

            assert partially_charged_battery.recharge(40) is True
            assert partially_charged_battery.getCharge() == 100
        
        def battery_notifies_recharge_to_monitor(monitored_battery):
            monitored_battery.mCharge = 70
            monitored_battery.recharge(20)
            monitored_battery.external_monitor.notify_recharge.assert_called_once_with(90)

    def describe_drain():
        def battery_drains_succesfully(charged_battery):
            assert charged_battery.drain(30) is True
            assert charged_battery.getCharge() == 70
        
        def battery_does_not_drain_past_capacity(charged_battery):
            assert charged_battery.drain(150) is True
            assert charged_battery.getCharge() == 0

            assert charged_battery.drain(10) is False
            assert charged_battery.getCharge() == 0
        
        def battery_notifies_drain_to_monitor(monitored_battery):
            monitored_battery.drain(30)
            monitored_battery.external_monitor.notify_drain.assert_called_once_with(70)

