import unittest
from unittest.mock import Mock
from src.Project.Application.CreateUserProjectAction import CreateUserProjectAction
from src.Project.Domain.IProjectRepository import IProjectRepository


class TestCreateUserProjectAction(unittest.TestCase):
    def test_run(self):
        # Create a mock repository
        repository = Mock(IProjectRepository)

        # Create an action
        action = CreateUserProjectAction(repository, "My Project", "http://example.com")

        # Run the action
        action.run()

        # Check that the repository's create method was called with the correct arguments
        repository.create.assert_called_with("My Project", "http://example.com")
