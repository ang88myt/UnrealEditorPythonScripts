import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedActors = MyEditorUtility().get_selection_set()

for actor in selectedActors:
    unreal.log(actor.get_name())
    unreal.log("****************************************************")

    SMCompts = actor.get_components_by_class(unreal.StaticMeshComponent)
    for SMCompt in SMCompts:
        SMComptT = SMCompt.get_editor_property("relative_location")
        print(SMComptT)
        SMCompt.set_editor_property("relative_location", unreal.Vector(0.0, 0.0, 0.0))
        print(SMComptT)
