

class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = [
            "JavaScript",
            "HTML", 
            "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a web page...")
        return "page == '<h1>Hello, World</h1>'"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = [
            "Python", 
            "SQL",
            "Django"]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "address == 'http://127.0.0.1:8000'"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = [
            "Java", 
            "Android Studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "app == 'Ads every three swipes'"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = FrontendDeveloper.skills + BackendDeveloper.skills

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_awesome_web_page()
        self.create_powerful_api()
