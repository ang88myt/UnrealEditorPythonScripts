import unreal

@unreal.uclass()
class MyEditorLevelUtility(unreal.EditorLevelUtils):
    pass

streamingLvl = MyEditorLevelUtility().create_new_streaming_level(unreal.LevelStreamingDynamic, "/Game/Streaming/lvl_TestStreaming", False)

