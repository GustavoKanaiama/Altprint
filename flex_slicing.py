from Altprint.core.flex_continuous import FlexProcess, FlexPrint


process = FlexProcess(settings_file="config/parameters/dev_flex_parameters.yml")
part = FlexPrint(process)


part.slice()
part.make_layers()
part.export_gcode("out/gcode/sliced_geometry.gcode")
