import unreal
import sys

# blueprintName = "AStreamingBlueprint"
blueprintPath = "/Game/Blueprintsxxx"

createAssetCount = int(sys.argv[1])
createAssetName = str(sys.argv[2])
createAssetName += '%d'

factory = unreal.BlueprintFactory()

factory.set_editor_property("ParentClass", unreal.Character)
assetTools = unreal.AssetToolsHelpers.get_asset_tools()

for x in range(createAssetCount):
    myfile = assetTools.create_asset(createAssetName %(x), blueprintPath, None, factory)

myfile = assetTools.create_asset(createAssetName, blueprintPath, None, factory)
