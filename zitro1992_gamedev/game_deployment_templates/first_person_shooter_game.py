import unreal
from unreal import AnimToTextureBPLibrary
from zitro1992_gamedev.common import Common

# Load config file
config_data = Common.load_config_file("/Users/kevinortiz/Documents/Unreal Projects/Python/first_person_shooter_game/config.yml")

# Perform necessary steps on Guns based on values from config.yml
guns = config_data["Guns"]
for gun in guns:
    for gun_type in guns[gun]:
        asset_path = guns[gun][gun_type]["AssetPath"]
        static_mesh_name = guns[gun][gun_type]["StaticMeshName"]

        if not unreal.EditorAssetLibrary.does_asset_exist(static_mesh_name):
            Common.create_static_mesh_from_skeletal_mesh(asset_path, static_mesh_name)
        else:
            print(f"Static mesh {static_mesh_name} already exists")

        # Set collision for static mesh
        static_mesh = unreal.EditorAssetLibrary.load_asset(static_mesh_name)
        unreal.EditorStaticMeshLibrary.add_simple_collisions(static_mesh=static_mesh, shape_type=unreal.ScriptingCollisionShapeType.BOX)

        unreal.EditorAssetLibrary.save_asset(static_mesh_name)

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

mapping_context_data = config_data["InputMappingContext"]
for mapping_context in mapping_context_data:
    mapping_context_name = mapping_context_data[mapping_context]["Name"]
    mapping_context_path = mapping_context_data[mapping_context]["Path"]
    mapping_context_input_action_mappings = mapping_context_data[mapping_context]["InputActions"]

    if not unreal.EditorAssetLibrary.does_asset_exist(f"{mapping_context_path}{mapping_context_name}"):
        input_mapping_context = unreal.AssetTools.create_asset(asset_tools, asset_name = mapping_context_name, package_path = mapping_context_path, asset_class = unreal.InputMappingContext, factory = unreal.InputMappingContext_Factory())
        unreal.EditorAssetLibrary.save_asset(f"{mapping_context_path}{mapping_context_name}")

    # for input_action in mapping_context_input_action_mappings:
    #     input_action_name = mapping_context_input_action_mappings[input_action]["InputActionName"]

    #     # Create input action mappings
    #     input_action = unreal.AssetTools.create_asset(asset_tools, asset_name = input_action_name, package_path = mapping_context_path, asset_class = unreal.InputAction, factory = unreal.InputAction_Factory())
    #     unreal.EditorAssetLibrary.save_asset(input_action)

blueprint_data = config_data["Blueprints"]
for blueprint in blueprint_data:
    blueprint_name = blueprint_data[blueprint]["Name"]
    blueprint_path = blueprint_data[blueprint]["Path"]
    blueprint_parent_class = blueprint_data[blueprint]["ParentClass"]

    if not unreal.EditorAssetLibrary.does_asset_exist(f"{blueprint_path}{blueprint_name}"):
        blueprint_class = unreal.AssetTools.create_asset(asset_tools, asset_name = blueprint_name, package_path = blueprint_path, asset_class = unreal.Blueprint, factory = unreal.BlueprintFactory())
        unreal.BlueprintEditorLibrary.reparent_blueprint(blueprint = blueprint_class, new_parent_class = unreal.Character)
        unreal.EditorAssetLibrary.save_asset(f"{blueprint_path}{blueprint_name}")