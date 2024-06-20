## Computer vision bot for videogames
Watches specified area on your monitor during playing a videogame (hp bar, mana, stamina etc) and triggers if bar value falls down under specified value. 
The only action is autopressing specified keycap on keyboard. For example, if hp becomes lower than 70%, bot will programmatically press keycap, which is used for healing.

There are some settings which can be used to configure bot. All of them are in `appsettings.json` file:

- `isDebugMode` (bool. Values: `true` of `false`) If debug mode is enabled, keyboard caps won't be pressed. Bot makes short sound to show that event is triggered.
- `monitoringThresholdMs` (int) Time interval in milliseconds between taking a monitor screenshot. The lower value, the more accurate monitoring is. May affect game perfomance.
- `isCvPreviewEnabled` (bool. Values: `true` of `false`)  If preview is enabled, a new window with selected area for monitoring will be shown. It is usefull just for visualization of bot work.
- `monitoringAreaCoordinates` (json object with int values) This object has 4 fields with X and Y coordinates of area on your monitor which you want to put under bot monitoring. It takes coordinates of top left point (x; y) and bottom right point (x; y) of a rectangular area.
- `monitoringAreaColorRgb` (json object with int values) This object takes low and high values for r (red), g (green) and b (blue) values of area under monitoring.
In this way an interval of color tones is created. For example, if bot watches a red hp bar, you should get RGB of that red color and add them to that config. If RGB is (120, 35, 40), you should enter rLow lower than 120, rHigh higher than 120 and the same for green and blue.
This interval mode is created for areas with opacity, which can change color a little.
- `targetKeyCap` (string) Keycap on your keyboard to press when event is triggered. For example, to press Q button, add "q" to this parameter.
- `triggerValueLow` (int) and `triggerValueHigh` (int) Low and high values of interval, where event is triggered and bot will press specified button. For example, if low value is 2 and high is 70 - keyboard button will be pressed if hp is between 2% and 70%.
Low value is used to prevent useless event trigering on loading screens, for example, where prefered area for monitoring is not shown.
- `triggerInterval` (int) Time interval in milliseconds between bot actions. For example, if first aid kit in your videogame takes 5 seconds for usage, there is no need for bot triggering in 5 seconds after last trigger even if event triggering conditions are suitable.
