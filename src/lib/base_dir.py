import os.path

def _base_dir(*files):
    return  os.path.realpath(os.path.join(os.path.dirname(__file__), *files))

def base_dir(*files):
    return _base_dir("..", *files)


class Assets:
    @staticmethod
    def assets_dir(*files):
        return base_dir("assets", *files)

    @staticmethod
    def icons(*files):
        return Assets.assets_dir("icons", *files)

    @staticmethod
    def themes(*files):
        return Assets.assets_dir("themes", *files)
