import os
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .IProjectRepository import IProjectRepository


class XMLProjectRepository(IProjectRepository):
    def create(self, name: str, url: str):
        pass
