#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
# create a new 'Legacy VTK Reader'

sarimagevtk = paraview.simple.LegacyVTKReader(FileNames=['C:\\Users\\User\\Desktop\\Appdesigner\\sarimage.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [662, 240]

# get layout
layout1 = GetLayout()

# show data in view
sarimagevtkDisplay = Show(sarimagevtk, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
sarimagevtkDisplay.Representation = 'Outline'
sarimagevtkDisplay.ColorArrayName = ['POINTS', '']
sarimagevtkDisplay.LookupTable = None
sarimagevtkDisplay.MapScalars = 1
sarimagevtkDisplay.MultiComponentsMapping = 0
sarimagevtkDisplay.InterpolateScalarsBeforeMapping = 1
sarimagevtkDisplay.Opacity = 1.0
sarimagevtkDisplay.PointSize = 2.0
sarimagevtkDisplay.LineWidth = 1.0
sarimagevtkDisplay.RenderLinesAsTubes = 0
sarimagevtkDisplay.RenderPointsAsSpheres = 0
sarimagevtkDisplay.Interpolation = 'Gouraud'
sarimagevtkDisplay.Specular = 0.0
sarimagevtkDisplay.SpecularColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.SpecularPower = 100.0
sarimagevtkDisplay.Luminosity = 0.0
sarimagevtkDisplay.Ambient = 0.0
sarimagevtkDisplay.Diffuse = 1.0
sarimagevtkDisplay.Roughness = 0.3
sarimagevtkDisplay.Metallic = 0.0
sarimagevtkDisplay.Texture = None
sarimagevtkDisplay.RepeatTextures = 1
sarimagevtkDisplay.InterpolateTextures = 0
sarimagevtkDisplay.SeamlessU = 0
sarimagevtkDisplay.SeamlessV = 0
sarimagevtkDisplay.UseMipmapTextures = 0
sarimagevtkDisplay.BaseColorTexture = None
sarimagevtkDisplay.NormalTexture = None
sarimagevtkDisplay.NormalScale = 1.0
sarimagevtkDisplay.MaterialTexture = None
sarimagevtkDisplay.OcclusionStrength = 1.0
sarimagevtkDisplay.EmissiveTexture = None
sarimagevtkDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.FlipTextures = 0
sarimagevtkDisplay.BackfaceRepresentation = 'Follow Frontface'
sarimagevtkDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.BackfaceOpacity = 1.0
sarimagevtkDisplay.Position = [0.0, 0.0, 0.0]
sarimagevtkDisplay.Scale = [1.0, 1.0, 1.0]
sarimagevtkDisplay.Orientation = [0.0, 0.0, 0.0]
sarimagevtkDisplay.Origin = [0.0, 0.0, 0.0]
sarimagevtkDisplay.Pickable = 1
sarimagevtkDisplay.Triangulate = 0
sarimagevtkDisplay.UseShaderReplacements = 0
sarimagevtkDisplay.ShaderReplacements = ''
sarimagevtkDisplay.NonlinearSubdivisionLevel = 1
sarimagevtkDisplay.UseDataPartitions = 0
sarimagevtkDisplay.OSPRayUseScaleArray = 0
sarimagevtkDisplay.OSPRayScaleArray = 'metalplate'
sarimagevtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sarimagevtkDisplay.OSPRayMaterial = 'None'
sarimagevtkDisplay.Orient = 0
sarimagevtkDisplay.OrientationMode = 'Direction'
sarimagevtkDisplay.SelectOrientationVectors = 'None'
sarimagevtkDisplay.Scaling = 0
sarimagevtkDisplay.ScaleMode = 'No Data Scaling Off'
sarimagevtkDisplay.ScaleFactor = 59.900000000000006
sarimagevtkDisplay.SelectScaleArray = 'metalplate'
sarimagevtkDisplay.GlyphType = 'Arrow'
sarimagevtkDisplay.UseGlyphTable = 0
sarimagevtkDisplay.GlyphTableIndexArray = 'metalplate'
sarimagevtkDisplay.UseCompositeGlyphTable = 0
sarimagevtkDisplay.UseGlyphCullingAndLOD = 0
sarimagevtkDisplay.LODValues = []
sarimagevtkDisplay.ColorByLODIndex = 0
sarimagevtkDisplay.GaussianRadius = 2.995
sarimagevtkDisplay.ShaderPreset = 'Sphere'
sarimagevtkDisplay.CustomTriangleScale = 3
sarimagevtkDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
sarimagevtkDisplay.Emissive = 0
sarimagevtkDisplay.ScaleByArray = 0
sarimagevtkDisplay.SetScaleArray = ['POINTS', 'metalplate']
sarimagevtkDisplay.ScaleArrayComponent = ''
sarimagevtkDisplay.UseScaleFunction = 1
sarimagevtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sarimagevtkDisplay.OpacityByArray = 0
sarimagevtkDisplay.OpacityArray = ['POINTS', 'metalplate']
sarimagevtkDisplay.OpacityArrayComponent = ''
sarimagevtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sarimagevtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
sarimagevtkDisplay.SelectionCellLabelBold = 0
sarimagevtkDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
sarimagevtkDisplay.SelectionCellLabelFontFamily = 'Arial'
sarimagevtkDisplay.SelectionCellLabelFontFile = ''
sarimagevtkDisplay.SelectionCellLabelFontSize = 18
sarimagevtkDisplay.SelectionCellLabelItalic = 0
sarimagevtkDisplay.SelectionCellLabelJustification = 'Left'
sarimagevtkDisplay.SelectionCellLabelOpacity = 1.0
sarimagevtkDisplay.SelectionCellLabelShadow = 0
sarimagevtkDisplay.SelectionPointLabelBold = 0
sarimagevtkDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
sarimagevtkDisplay.SelectionPointLabelFontFamily = 'Arial'
sarimagevtkDisplay.SelectionPointLabelFontFile = ''
sarimagevtkDisplay.SelectionPointLabelFontSize = 18
sarimagevtkDisplay.SelectionPointLabelItalic = 0
sarimagevtkDisplay.SelectionPointLabelJustification = 'Left'
sarimagevtkDisplay.SelectionPointLabelOpacity = 1.0
sarimagevtkDisplay.SelectionPointLabelShadow = 0
sarimagevtkDisplay.PolarAxes = 'PolarAxesRepresentation'
sarimagevtkDisplay.ScalarOpacityFunction = None
sarimagevtkDisplay.ScalarOpacityUnitDistance = 6.368468376732937
sarimagevtkDisplay.SelectMapper = 'Projected tetra'
sarimagevtkDisplay.SamplingDimensions = [128, 128, 128]

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
sarimagevtkDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
sarimagevtkDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
sarimagevtkDisplay.GlyphType.TipResolution = 6
sarimagevtkDisplay.GlyphType.TipRadius = 0.1
sarimagevtkDisplay.GlyphType.TipLength = 0.35
sarimagevtkDisplay.GlyphType.ShaftResolution = 6
sarimagevtkDisplay.GlyphType.ShaftRadius = 0.03
sarimagevtkDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sarimagevtkDisplay.ScaleTransferFunction.Points = [1.090000033378601, 0.0, 0.5, 0.0, 1786873344.0, 1.0, 0.5, 0.0]
sarimagevtkDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sarimagevtkDisplay.OpacityTransferFunction.Points = [1.090000033378601, 0.0, 0.5, 0.0, 1786873344.0, 1.0, 0.5, 0.0]
sarimagevtkDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
sarimagevtkDisplay.DataAxesGrid.XTitle = 'X Axis'
sarimagevtkDisplay.DataAxesGrid.YTitle = 'Y Axis'
sarimagevtkDisplay.DataAxesGrid.ZTitle = 'Z Axis'
sarimagevtkDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
sarimagevtkDisplay.DataAxesGrid.XTitleFontFile = ''
sarimagevtkDisplay.DataAxesGrid.XTitleBold = 0
sarimagevtkDisplay.DataAxesGrid.XTitleItalic = 0
sarimagevtkDisplay.DataAxesGrid.XTitleFontSize = 12
sarimagevtkDisplay.DataAxesGrid.XTitleShadow = 0
sarimagevtkDisplay.DataAxesGrid.XTitleOpacity = 1.0
sarimagevtkDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
sarimagevtkDisplay.DataAxesGrid.YTitleFontFile = ''
sarimagevtkDisplay.DataAxesGrid.YTitleBold = 0
sarimagevtkDisplay.DataAxesGrid.YTitleItalic = 0
sarimagevtkDisplay.DataAxesGrid.YTitleFontSize = 12
sarimagevtkDisplay.DataAxesGrid.YTitleShadow = 0
sarimagevtkDisplay.DataAxesGrid.YTitleOpacity = 1.0
sarimagevtkDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
sarimagevtkDisplay.DataAxesGrid.ZTitleFontFile = ''
sarimagevtkDisplay.DataAxesGrid.ZTitleBold = 0
sarimagevtkDisplay.DataAxesGrid.ZTitleItalic = 0
sarimagevtkDisplay.DataAxesGrid.ZTitleFontSize = 12
sarimagevtkDisplay.DataAxesGrid.ZTitleShadow = 0
sarimagevtkDisplay.DataAxesGrid.ZTitleOpacity = 1.0
sarimagevtkDisplay.DataAxesGrid.FacesToRender = 63
sarimagevtkDisplay.DataAxesGrid.CullBackface = 0
sarimagevtkDisplay.DataAxesGrid.CullFrontface = 1
sarimagevtkDisplay.DataAxesGrid.ShowGrid = 0
sarimagevtkDisplay.DataAxesGrid.ShowEdges = 1
sarimagevtkDisplay.DataAxesGrid.ShowTicks = 1
sarimagevtkDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
sarimagevtkDisplay.DataAxesGrid.AxesToLabel = 63
sarimagevtkDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
sarimagevtkDisplay.DataAxesGrid.XLabelFontFile = ''
sarimagevtkDisplay.DataAxesGrid.XLabelBold = 0
sarimagevtkDisplay.DataAxesGrid.XLabelItalic = 0
sarimagevtkDisplay.DataAxesGrid.XLabelFontSize = 12
sarimagevtkDisplay.DataAxesGrid.XLabelShadow = 0
sarimagevtkDisplay.DataAxesGrid.XLabelOpacity = 1.0
sarimagevtkDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
sarimagevtkDisplay.DataAxesGrid.YLabelFontFile = ''
sarimagevtkDisplay.DataAxesGrid.YLabelBold = 0
sarimagevtkDisplay.DataAxesGrid.YLabelItalic = 0
sarimagevtkDisplay.DataAxesGrid.YLabelFontSize = 12
sarimagevtkDisplay.DataAxesGrid.YLabelShadow = 0
sarimagevtkDisplay.DataAxesGrid.YLabelOpacity = 1.0
sarimagevtkDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
sarimagevtkDisplay.DataAxesGrid.ZLabelFontFile = ''
sarimagevtkDisplay.DataAxesGrid.ZLabelBold = 0
sarimagevtkDisplay.DataAxesGrid.ZLabelItalic = 0
sarimagevtkDisplay.DataAxesGrid.ZLabelFontSize = 12
sarimagevtkDisplay.DataAxesGrid.ZLabelShadow = 0
sarimagevtkDisplay.DataAxesGrid.ZLabelOpacity = 1.0
sarimagevtkDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
sarimagevtkDisplay.DataAxesGrid.XAxisPrecision = 2
sarimagevtkDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
sarimagevtkDisplay.DataAxesGrid.XAxisLabels = []
sarimagevtkDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
sarimagevtkDisplay.DataAxesGrid.YAxisPrecision = 2
sarimagevtkDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
sarimagevtkDisplay.DataAxesGrid.YAxisLabels = []
sarimagevtkDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
sarimagevtkDisplay.DataAxesGrid.ZAxisPrecision = 2
sarimagevtkDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
sarimagevtkDisplay.DataAxesGrid.ZAxisLabels = []
sarimagevtkDisplay.DataAxesGrid.UseCustomBounds = 0
sarimagevtkDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
sarimagevtkDisplay.PolarAxes.Visibility = 0
sarimagevtkDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
sarimagevtkDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
sarimagevtkDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
sarimagevtkDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
sarimagevtkDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
sarimagevtkDisplay.PolarAxes.EnableCustomRange = 0
sarimagevtkDisplay.PolarAxes.CustomRange = [0.0, 1.0]
sarimagevtkDisplay.PolarAxes.PolarAxisVisibility = 1
sarimagevtkDisplay.PolarAxes.RadialAxesVisibility = 1
sarimagevtkDisplay.PolarAxes.DrawRadialGridlines = 1
sarimagevtkDisplay.PolarAxes.PolarArcsVisibility = 1
sarimagevtkDisplay.PolarAxes.DrawPolarArcsGridlines = 1
sarimagevtkDisplay.PolarAxes.NumberOfRadialAxes = 0
sarimagevtkDisplay.PolarAxes.AutoSubdividePolarAxis = 1
sarimagevtkDisplay.PolarAxes.NumberOfPolarAxis = 0
sarimagevtkDisplay.PolarAxes.MinimumRadius = 0.0
sarimagevtkDisplay.PolarAxes.MinimumAngle = 0.0
sarimagevtkDisplay.PolarAxes.MaximumAngle = 90.0
sarimagevtkDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
sarimagevtkDisplay.PolarAxes.Ratio = 1.0
sarimagevtkDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
sarimagevtkDisplay.PolarAxes.PolarAxisTitleVisibility = 1
sarimagevtkDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
sarimagevtkDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
sarimagevtkDisplay.PolarAxes.PolarLabelVisibility = 1
sarimagevtkDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
sarimagevtkDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
sarimagevtkDisplay.PolarAxes.RadialLabelVisibility = 1
sarimagevtkDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
sarimagevtkDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
sarimagevtkDisplay.PolarAxes.RadialUnitsVisibility = 1
sarimagevtkDisplay.PolarAxes.ScreenSize = 10.0
sarimagevtkDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
sarimagevtkDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
sarimagevtkDisplay.PolarAxes.PolarAxisTitleFontFile = ''
sarimagevtkDisplay.PolarAxes.PolarAxisTitleBold = 0
sarimagevtkDisplay.PolarAxes.PolarAxisTitleItalic = 0
sarimagevtkDisplay.PolarAxes.PolarAxisTitleShadow = 0
sarimagevtkDisplay.PolarAxes.PolarAxisTitleFontSize = 12
sarimagevtkDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
sarimagevtkDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
sarimagevtkDisplay.PolarAxes.PolarAxisLabelFontFile = ''
sarimagevtkDisplay.PolarAxes.PolarAxisLabelBold = 0
sarimagevtkDisplay.PolarAxes.PolarAxisLabelItalic = 0
sarimagevtkDisplay.PolarAxes.PolarAxisLabelShadow = 0
sarimagevtkDisplay.PolarAxes.PolarAxisLabelFontSize = 12
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextBold = 0
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextItalic = 0
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextShadow = 0
sarimagevtkDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
sarimagevtkDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
sarimagevtkDisplay.PolarAxes.EnableDistanceLOD = 1
sarimagevtkDisplay.PolarAxes.DistanceLODThreshold = 0.7
sarimagevtkDisplay.PolarAxes.EnableViewAngleLOD = 1
sarimagevtkDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
sarimagevtkDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
sarimagevtkDisplay.PolarAxes.PolarTicksVisibility = 1
sarimagevtkDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
sarimagevtkDisplay.PolarAxes.TickLocation = 'Both'
sarimagevtkDisplay.PolarAxes.AxisTickVisibility = 1
sarimagevtkDisplay.PolarAxes.AxisMinorTickVisibility = 0
sarimagevtkDisplay.PolarAxes.ArcTickVisibility = 1
sarimagevtkDisplay.PolarAxes.ArcMinorTickVisibility = 0
sarimagevtkDisplay.PolarAxes.DeltaAngleMajor = 10.0
sarimagevtkDisplay.PolarAxes.DeltaAngleMinor = 5.0
sarimagevtkDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
sarimagevtkDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
sarimagevtkDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
sarimagevtkDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
sarimagevtkDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
sarimagevtkDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
sarimagevtkDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
sarimagevtkDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
sarimagevtkDisplay.PolarAxes.ArcMajorTickSize = 0.0
sarimagevtkDisplay.PolarAxes.ArcTickRatioSize = 0.3
sarimagevtkDisplay.PolarAxes.ArcMajorTickThickness = 1.0
sarimagevtkDisplay.PolarAxes.ArcTickRatioThickness = 0.5
sarimagevtkDisplay.PolarAxes.Use2DMode = 0
sarimagevtkDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(sarimagevtkDisplay, ('POINTS', 'metalplate'))

# rescale color and/or opacity maps used to include current data range
sarimagevtkDisplay.RescaleTransferFunctionToDataRange(True, True)

# change representation type
sarimagevtkDisplay.SetRepresentationType('Volume')

# get color transfer function/color map for 'metalplate'
metalplateLUT = GetColorTransferFunction('metalplate')
metalplateLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
metalplateLUT.InterpretValuesAsCategories = 0
metalplateLUT.AnnotationsInitialized = 0
metalplateLUT.ShowCategoricalColorsinDataRangeOnly = 0
metalplateLUT.RescaleOnVisibilityChange = 0
metalplateLUT.EnableOpacityMapping = 0
metalplateLUT.RGBPoints = [1.090000033378601, 0.231373, 0.298039, 0.752941, 893436672.545, 0.865003, 0.865003, 0.865003, 1786873344.0, 0.705882, 0.0156863, 0.14902]
metalplateLUT.UseLogScale = 0
metalplateLUT.ShowDataHistogram = 0
metalplateLUT.AutomaticDataHistogramComputation = 0
metalplateLUT.DataHistogramNumberOfBins = 10
metalplateLUT.ColorSpace = 'Diverging'
metalplateLUT.UseBelowRangeColor = 0
metalplateLUT.BelowRangeColor = [0.0, 0.0, 0.0]
metalplateLUT.UseAboveRangeColor = 0
metalplateLUT.AboveRangeColor = [0.5, 0.5, 0.5]
metalplateLUT.NanColor = [1.0, 1.0, 0.0]
metalplateLUT.NanOpacity = 1.0
metalplateLUT.Discretize = 1
metalplateLUT.NumberOfTableValues = 256
metalplateLUT.ScalarRangeInitialized = 1.0
metalplateLUT.HSVWrap = 0
metalplateLUT.VectorComponent = 0
metalplateLUT.VectorMode = 'Magnitude'
metalplateLUT.AllowDuplicateScalars = 1
metalplateLUT.Annotations = []
metalplateLUT.ActiveAnnotatedValues = []
metalplateLUT.IndexedColors = []
metalplateLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'metalplate'
metalplatePWF = GetOpacityTransferFunction('metalplate')
metalplatePWF.Points = [1.090000033378601, 0.0, 0.5, 0.0, 1786873344.0, 1.0, 0.5, 0.0]
metalplatePWF.AllowDuplicateScalars = 1
metalplatePWF.UseLogScale = 0
metalplatePWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
metalplateLUT.ApplyPreset('jet', True)


#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).