import arcpy

import re


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "ercitoolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [ClipRasterTool,ClipRasterTool1]


class ClipRasterTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "polygon_clip"
        self.description = ""
        self.canRunInBackground = False
        

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = [            
            arcpy.Parameter(
                displayName="dwg",
                name="clip_layer",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Input"),
                
            arcpy.Parameter(
                displayName="output",
                name="output_path",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Output")
        ]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # 获取当前ArcMap文档引用
        mxd = arcpy.mapping.MapDocument("CURRENT")
        # 获取活动数据框（ArcMap对应ArcGIS Pro的activeMap）
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        # 获取目标数据框
        #df = mxd.activeDataFrame
        #if target_frame:
        #    for frame in arcpy.mapping.ListDataFrames(mxd):
        #        if frame.name == target_frame:
        #            df = frame
        #            break
        

        clip_layer = parameters[0].valueAsText
        output_path = parameters[1].valueAsText
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4547)
        #arcpy.env.workspace = r"C:\Users\duany\Documents\ArcGIS\Default.gdb"
        polygon_layer = clip_layer
        where_clause = "layer = 'clip'"
        arcpy.SelectLayerByAttribute_management(polygon_layer, "NEW_SELECTION", where_clause)
        arcpy.AddMessage(parameters[0].valueAsText)
        #matches =re.findall(r'\S+\.dwg', clip_layer)
        #try:
        #    output_path = matches[0].replace(".dwg", "_clip.shp")  
        #except:
        #    matches =re.findall(r'\S+\.DWG', clip_layer)    
        #    output_path = matches[0].replace(".DWG", "_clip.shp")  
        arcpy.AddMessage(output_path)
        arcpy.CopyFeatures_management(polygon_layer, output_path)

        # 统一使用正斜杠并验证路径存在性
        #in_raster = r"C:\Users\duany\Documents\ArcGIS\luohe2021img\luohe_4111.img"
        #if not arcpy.Exists(in_raster):
        #    raise ValueError("输入栅格文件不存在")

        # sr=None
        # Python 2兼容的字符串格式化
        #sr = arcpy.Describe(output_path).spatialReference
        #if not sr:
        #    # 若无空间参考则手动定义（示例使用WGS84）
        #    arcpy.DefineProjection_management(output_path, arcpy.SpatialReference(4547))
        #    sr = arcpy.Describe( output_path).spatialReference
        #sr = arcpy.Describe(in_raster).spatialReference
        #if not sr:
        #    # 若无空间参考则手动定义（示例使用WGS84）
        #    arcpy.DefineProjection_management(in_raster, arcpy.SpatialReference(4547))
        #    sr = arcpy.Describe( in_raster).spatialReference
        # 创建临时栅格图层
        #temp_layer = "temp_raster_layer"
        #arcpy.MakeRasterLayer_management(r"C:\Users\duany\Documents\ArcGIS\luohe2021img\luohe_4111.img", temp_layer)
#
        ## 保存为图层文件
        ## arcpy.SaveToLayerFile_management(temp_layer, output_lyr)
#
        #
        #addLayer = arcpy.mapping.Layer(temp_layer)
        #arcpy.mapping.AddLayer(arcpy.mapping.ListDataFrames(mxd)[0], addLayer, "BOTTOM")
        #addLayer = arcpy.mapping.Layer(output_path)
        #arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
        #arcpy.AddMessage(in_raster)
        #arcpy.AddMessage(output_path)
        #arcpy.Clip_management (in_raster,"#",out_raster, output_path, 256, "NONE", "NO_MAINTAIN_EXTENT")
        #arcpy.AddMessage(out_raster)

        return
class ClipRasterTool1(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "raster_clip"
        self.description = ""
        self.canRunInBackground = False
        

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = [            
            arcpy.Parameter(
                displayName="shp",
                name="clip_layer",
                datatype="GPFeatureLayer",
                parameterType="Required",
                direction="Input"),
            arcpy.Parameter(
                displayName="raster",
                name="in_raster",
                datatype="GPRasterLayer",
                parameterType="Required",
                direction="Input"),    
            arcpy.Parameter(
                displayName="output",
                name="out_raster",
                datatype="DERasterDataset",
                parameterType="Required",
                direction="Output")
        ]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # 获取当前ArcMap文档引用
        mxd = arcpy.mapping.MapDocument("CURRENT")
        # 获取活动数据框（ArcMap对应ArcGIS Pro的activeMap）
        df = arcpy.mapping.ListDataFrames(mxd)[0]
       

        output_path = parameters[0].valueAsText
        in_raster = parameters[1].valueAsText
        out_raster = parameters[2].valueAsText
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4547)
        #arcpy.env.workspace = r"C:\Users\duany\Documents\ArcGIS\Default.gdb"
        

        # 统一使用正斜杠并验证路径存在性
        #in_raster = r"C:\Users\duany\Documents\ArcGIS\luohe2021img\luohe_4111.img"
        #if not arcpy.Exists(in_raster):
        #    raise ValueError("输入栅格文件不存在")

        # sr=None
        # Python 2兼容的字符串格式化
        #sr = arcpy.Describe(output_path).spatialReference
        #if not sr:
        #    # 若无空间参考则手动定义（示例使用WGS84）
        #    arcpy.DefineProjection_management(output_path, arcpy.SpatialReference(4547))
        #    sr = arcpy.Describe( output_path).spatialReference
        #sr = arcpy.Describe(in_raster).spatialReference
        #if not sr:
        #    # 若无空间参考则手动定义（示例使用WGS84）
        #    arcpy.DefineProjection_management(in_raster, arcpy.SpatialReference(4547))
        #    sr = arcpy.Describe( in_raster).spatialReference
        # 创建临时栅格图层
        #temp_layer = "temp_raster_layer"
        #arcpy.MakeRasterLayer_management(r"C:\Users\duany\Documents\ArcGIS\luohe2021img\luohe_4111.img", temp_layer)
#
        ## 保存为图层文件
        ## arcpy.SaveToLayerFile_management(temp_layer, output_lyr)
#
        #
        #addLayer = arcpy.mapping.Layer(temp_layer)
        #arcpy.mapping.AddLayer(arcpy.mapping.ListDataFrames(mxd)[0], addLayer, "BOTTOM")
        #addLayer = arcpy.mapping.Layer(output_path)
        #arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
        #arcpy.AddMessage(in_raster)
        #arcpy.AddMessage(output_path)
        arcpy.Clip_management (in_raster,"#",out_raster, output_path, 256, "NONE", "NO_MAINTAIN_EXTENT")
        arcpy.AddMessage(out_raster)

        return
