from file_system_component import FileSystemComponent

class Directory(FileSystemComponent):
    """Represents a directory in the file system.
    
    This class serves as the 'Composite' in the Composite pattern.
    """
    
    def __init__(self, name):
        # TODO: Call parent constructor with name using super()
        # TODO: Initialize empty list _components to store child components
        super().__init__(name)
        self._components = []
    
    def get_size(self):
        # TODO: Return the sum of sizes of all components in _components
        # TODO: Use sum() with generator expression: component.get_size() for each component
        sizes = []
        for i in self._components:
            sizes.append(i.get_size())
        return sum(sizes)
    
    def display(self, indent=0):
        # TODO: Create result list starting with directory header
        # TODO: Header format: " " * indent + f"Directory: {self.name} ({self.get_size()} KB)"
        # TODO: For each component in _components, add component.display(indent + 2) to result
        # TODO: Join all result strings with "\n" and return
        result_list = []
        result_list.append(" " * indent + f"Directory: {self.name} ({self.get_size()} KB)")
        for i in self._components:
            result_list.append(i.display(indent + 2))
        return str.join("\n", result_list)
    
    def add(self, component):
        # TODO: Check if any component in _components has the same name as the new component
        # TODO: If duplicate name found, raise ValueError: f"Component with name '{component.name}' already exists"
        # TODO: If no duplicate, append component to _components list
        names = []
        for i in self._components:
            names.append(i.name)

        if component.name in names:
            raise ValueError(f"Component with name '{component.name}' already exists")
        else:
            self._components.append(component)
    
    def remove(self, component):
        # TODO: Check if component exists in _components list
        # TODO: If found, remove it from _components
        # TODO: If not found, raise ValueError: f"Component {component.name} not found"
        if component in self._components:
            self._components.remove(component)
        else:
            raise ValueError(f"Component {component.name} not found")
    
    def get_component(self, name):
        # TODO: Iterate through _components list
        # TODO: For each component, check if component.name equals the search name
        # TODO: Return the component if found, otherwise return None
        for i in self._components:
            if i.name == name:
                return i
        return None
    
    def find_component_recursive(self, name):
        """Recursively searches for a component with the given name."""
        # TODO: First check direct children using get_component(name)
        # TODO: If component found, return it
        # TODO: Then check in subdirectories: iterate through _components
        # TODO: For each component that is isinstance(component, Directory):
        # TODO:   Call component.find_component_recursive(name)
        # TODO:   If found (not None), return the found component
        # TODO: Return None if not found anywhere
        return_comp = self.get_component(name)
        if return_comp:
            return return_comp
        for component in self._components:
            if isinstance(component, Directory):
                rec_comp = component.find_component_recursive(name)
                if rec_comp:
                    return rec_comp
        return None