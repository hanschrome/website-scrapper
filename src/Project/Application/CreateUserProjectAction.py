from src.Project.Infrastructure.IProjectRepository import IProjectRepository


class CreateUserProjectAction:

    def __init__(self, project_repository: IProjectRepository, name: str, url: str):
        self.project_repository = project_repository
        self.name = name
        self.url = url

    def run(self):
        self.project_repository.create(self.name, self.url)
