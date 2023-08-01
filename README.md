#UnrealEditorPythonScripts#
---------------------------------------------------


Some of my personal scripts i made to use for my own projects, but free of charge to be used for any project and any purpose as long as it is not violating the Unreal Engine EULA.

In order to be able to sue those helper scripts, you must be sure this plugins are enabled first:

1. Scripting/Python Editor Script Plugin
2. Scripting/Editor Scripting Utilities


## Aimation ##

- **[CleanNotifiesFromAnimations.py](https://github.com/ang8myt/UnrealEditorPythonScripts/Animation/CleanNotifiesFromAnimations.py)** Run on a selected single or multiple animation file(s) in order to clean up the selected file(s) from any animation notifies.
- **[SetAllAnimNotifyProperty.py]** Run on a selected single or multiple animation file(s) in order set some values for all the animation notifies exists in the selected animations (notify name, notify color, notify trigger settings,...etc.). NOTE that the later part of the scrip (color fetch & change) won't work with the custom notifies (the ones that call a function/Event), as those notifies are meant to have fixed color by design.

## Assets ##

- **[ReportUnusedAssets.py]** Running this script will look through all the project folders, and add to the log the assets that were found not in a use, or in another word, the assets that have no dependency with any other project files.
- **[DeleteUnusedAssets.py]** Running this script will look through all the project folders, and delete the assets that were found not in a use, or in another word, the assets that have no dependency with any other project files. Note that, running this script won't show a confirmation message or accepting dialogue box, it will force delete the assets right a way, so make sure to evaluate the change before submitting to your repo.
- **[ArchiveUnusedAssets.py]** Running this script will look through all the project folders, and grab all the assets that were found not in a use, or in another word, the assets that have no dependency with any other project files. And finally put them all together in a *"_ARCHIVE"* directory at the content root directory. It works similarly as the ***DeleteUnusedAssets.py*** script, except this won't delete any, and keeping them in archive for final & closer evaluation.
- **[UnifyAssetDuplicates.py]** Run on a selected single asset in order to look through the project for similar assets with the same name, and will remove all of them, and replace all their references with the selected one. This is a very common case if for example have added several packs or assets to the project and you will end up with several files (textures, materials or such) that have the same exact name and parameters *(add Paragon characters for example to a single project could result that)*, but a unique version coming from each imported pack; and there it come the usage of that script in unifying them.
- **[UnifyAllAssetsDuplicates.py]** It working the same as the previous script (UnifyAssetDuplicated) except this time, you don't have to select any asset. The script will run through the entire project seeking any asset duplicated (same type & same name) and will unify them into one version only.
- **[OrganizeAssetsPerType.py]** When you start new project, you don't have to worry about organizing the assets per family in folders. Just go ahead and focus on building the prototype or content, and then execute that script at any moment will make sure to move all the assets from the same type (*UClass*) to their own folder.
- **[PrefixAllAssets.py]** Running this script will apply prefix to majority of the files. While those prefixes I used are more subjective to my own pipeline, but you can modify them simply by opening the script and set the prefix of your choice per file type at the top of the script. You can also add more cases if not exist!

## Components ##

- **[AccessAndModifyComponentsOld.py]** Running this script will go through all the selected actors, and modify a given attribute of the given component type to a given value. In the example we search for StaticMeshComponents (as type) and reset their relative location (as attribute) to 0,0,0 (as value).
Worth mention that, this version of the script, works great with none-inherited components (the ones with gray icons, not blue icons). For better version, that uses different logic, check the script below.
- **[AccessAndModifyComponentsNew.py]** Running this script will go through all the selected actors, and modify a given attribute of the given component type to a given value. In the example we search for StaticMeshComponents (as type) and reset their relative location (as attribute) to 0,0,0 (as value).

## Level ##
- **[CreateSingleLevelStreaming.py]** An example on how to create a level streaming via python script. You can create as many streaming levels and control them right away with a for loop, however in this example we create only singe level of "*LevelStreamingDynamic*" at a desired location.

## Materials ##
- **[CreateInstancesOfSelectedMaterial.py]** Run on a selected single or multiple Material file(s) in order to generate material instances of it/them. The number of the final generated instances count can be set within the script before running, by changing the value of the variable *totalRequiredInstances*
- **[AssignMaterialToAllSimilarNamedMeshes.py]** Select a static mesh and then a material *(Yup, has to be in that order)* and run the script in order to run through the project looking for similar static meshes, and then assign the selected material to all of found clones of that mesh. The script can be extended easily to add more materials in case of the mesh is not using a single material slot.
- **[ReportTwoSidedMaterials.py]** When run this script, it will go through the entire project searching for materials and material instances, and eventually report fully to the log if there are ones that is using Two-Sided shading.

## Sequencer ##
- **[CreateAndEditCineCameraActor.py]** An example on how you can create cinematic camera in the current world/map, and start modifying some of it's focus settings (Keep in mind you **MUST enable the Scripting python sequencer plugin** for that, **python plugin only is not enough**).
*This nice example was built while supporting a user of the python course, so the credits goes to them*.
- **[CreateCineCameraForEverySkeletalMesh.py]** An example on auto-create cameras for every skeletal mesh actor in the world, and align the camera to the skeletal characters, set the cameras to always look at those characters actors.


