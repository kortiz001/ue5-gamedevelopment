import unreal
from unreal import AnimToTextureBPLibrary
import yaml

class Common():
    def __init__(self, name: str) -> None:
        self.name=name

    def load_config_file(file_path: str):
        with open(file_path, 'r') as file:
            config_data = yaml.safe_load(file)

        return config_data

    def create_static_mesh_from_skeletal_mesh(asset_path: str, static_mesh_path: str):
        # Load the asset
        asset = unreal.EditorAssetLibrary().load_asset(asset_path)

        # Convert the skeletal mesh to static mesh
        static_mesh = AnimToTextureBPLibrary.convert_skeletal_mesh_to_static_mesh(asset, static_mesh_path, 0)

        return static_mesh