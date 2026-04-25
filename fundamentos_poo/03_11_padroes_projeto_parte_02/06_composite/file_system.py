from directory import Directory

class FileSystem:
    """Represents the overall file system.
    
    This class serves as a facade for working with the file system components.
    """
    
    def __init__(self):
        # TODO: Create root directory with name "root"
        # TODO: Store it as self.root
        self.root = Directory("root")
    
    def _get_directory_from_path(self, path):
        """Helper method to navigate to a directory from a path."""
        # TODO: If path is empty or "/", return self.root
        # TODO: Split path by "/" and remove empty parts
        # TODO: Navigate through path parts starting from root
        # TODO: For each part except last, get component and verify it's a directory
        # TODO: Return (parent_directory, target_component) tuple
        # TODO: Raise ValueError if path not found or component is not directory
        if not path or path == "/":
            return (None, self.root)

        # remove vazios
        parts = [p for p in path.split("/") if p]

        current = self.root

        # percorre até o penúltimo
        for part in parts[:-1]:
            next_component = current.get(part)
            if next_component is None or not isinstance(next_component, Directory):
                raise ValueError(f"Diretório '{part}' não encontrado no caminho '{path}'")
            current = next_component

        target_name = parts[-1]
        target_component = current.get(target_name)

        return (current, target_component)

    
    def add_to_path(self, path, component):
        """Adds a component at the specified path."""
        # TODO: If path is empty or "/", add component to root directory
        # TODO: Otherwise, get parent directory from path
        # TODO: Add component to parent directory
        if not path or path == "/":
            self.root.add(component)
            return

        parent, target = self._get_directory_from_path(path)

        # se target existe e é diretório, adiciona dentro dele
        if target and isinstance(target, Directory):
            target.add(component)
        else:
            # caso path seja tipo /a/b (onde b ainda não existe)
            parent.add(component)
    
    def remove_from_path(self, path):
        """Removes a component at the specified path."""
        # TODO: Check if trying to remove root directory (raise ValueError)
        # TODO: Get parent directory and target component from path
        # TODO: If component exists, remove it from parent
        # TODO: Otherwise raise ValueError for path not found
        if not path or path == "/":
            raise ValueError("Não é possível remover o diretório root")

        parent, target = self._get_directory_from_path(path)

        if target is None:
            raise ValueError(f"Caminho '{path}' não encontrado")

        parent.remove(target.name)
    
    def get_from_path(self, path):
        """Retrieves a component at the specified path."""
        # TODO: If path is empty or "/", return root directory
        # TODO: Otherwise, use _get_directory_from_path to get component
        # TODO: Return the component
        if not path or path == "/":
            return self.root

        parent, target = self._get_directory_from_path(path)

        if target is None:
            raise ValueError(f"Caminho '{path}' não encontrado")

        return target
    
    def display(self):
        """Displays the entire file system."""
        # TODO: Return the result of calling display() on root directory
        return self.root.display()
    
    def get_total_size(self):
        """Returns the total size of all files in the system."""
        # TODO: Return the result of calling get_size() on root directory
        return self.root.get_size()