import os
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .IProjectRepository import IProjectRepository


class XMLProjectRepository(IProjectRepository):
    def create(self, name: str, url: str):
        # Check if a folder with the given name already exists
        if os.path.exists(name):
            raise Exception("A folder with that name already exists.")

        # Create the directory
        os.mkdir(name)

        # Create the XML file
        root = Element("project")
        name_element = SubElement(root, "name")
        name_element.text = name
        url_element = SubElement(root, "url")
        url_element.text = url
        tree = ElementTree(root)
        tree.write(os.path.join(name, "project.xml"))
