#ifndef LOW_LEVEL_API
#define LOW_LEVEL_API

class LowLevelApi {
    public:
	void setPumpOnOff(bool);
	void setHeatOnOff(bool);
	void setPower(float percent);
	float getPower();
        float getTemperature();
        
        float power;
};

extern "C" {
	LowLevelApi* low_level_new() { return new LowLevelApi(); }
	void low_level_set_pump_on_off(LowLevelApi* lowLevelApi, bool on) { lowLevelApi->setPumpOnOff(on); }
	void low_level_set_heat_on_off(LowLevelApi* lowLevelApi, bool on) { lowLevelApi->setHeatOnOff(on); }
	void low_level_set_power(LowLevelApi* lowLevelApi, float percent) { lowLevelApi->setPower(percent); }
	float low_level_get_power(LowLevelApi* lowLevelApi) { return lowLevelApi->getPower(); }
	float low_level_get_temperature(LowLevelApi* lowLevelApi) { return lowLevelApi->getTemperature(); }
}

#endif //LOW_LEVEL_API
