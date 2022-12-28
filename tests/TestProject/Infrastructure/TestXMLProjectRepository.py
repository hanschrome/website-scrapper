import unittest
import os
import xml.etree.ElementTree as ET
from src.Project.Infrastructure.XMLProjectRepository import XMLProjectRepository


class TestXMLProjectRepository(unittest.TestCase):
    def test_create(self):
        # Create a repository instance
        repository = XMLProjectRepository()

        # Create a project
        repository.create("My Project", "http://example.com")

        # Check that the directory and XML file were created
        self.assertTrue(os.path.exists(os.path.join("storage/projects", "My Project")))
        self.assertTrue(os.path.exists(os.path.join("storage/projects", "My Project", "project.xml")))

        # Check the contents of the XML file
        tree = ET.parse(os.path.join("storage/projects", "My Project", "project.xml"))
        root = tree.getroot()
        self.assertEqual(root.find("name").text, "My Project")
        self.assertEqual(root.find("url").text, "http://example.com")

        # Clean up
        os.remove(os.path.join("storage/projects", "My Project", "project.xml"))
        os.rmdir(os.path.join("storage/projects", "My Project"))
