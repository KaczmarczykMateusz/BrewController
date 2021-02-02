#include <iostream>
#include <ctime>
#include "LowLevelApi.hpp"

void LowLevelApi::setPumpOnOff(bool on) {
	;  //TODO: set proper parameter
}

void LowLevelApi::setHeatOnOff(bool on) {
	;  //TODO: set proper parameter
}

void LowLevelApi::setPower(float percent) {
	power = percent;  //TODO: set proper parameter
} 

float LowLevelApi::getPower() {
	return power;  //TODO: replace with actual value
}

float LowLevelApi::getTemperature() {
	return 36.6;  //TODO: replace with actual value
}
