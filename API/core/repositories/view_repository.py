from core.repositories.schema_repository import SchemaRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.view import View

class ViewRepository:
    def __init__(self):
        self.db_repo = DatabaseRepository()
        self.schema_repo = SchemaRepository()

    def _find_schema_and_db_by_view(self, view_name: str):
        for db in self.db_repo.get_all():
            for schema in db.children:
                if type(schema).__name__ == "Schema":
                    for child in schema.children:
                        if isinstance(child, View) and child.name == view_name:
                            return schema, db
        return None, None

    def get_all(self):
        views = []
        for db in self.db_repo.get_all():
            for schema in db.children:
                if type(schema).__name__ == "Schema":
                    for child in schema.children:
                        if isinstance(child, View):
                            views.append(child)
        return views

    def get_by_name(self, name: str):
        for view in self.get_all():
            if view.name == name:
                return view
        return None

    def save(self, schema_name: str, view: View):
        # We need to find schema to save the view in it
        for db in self.db_repo.get_all():
            schema = self.schema_repo.get_by_name(db.name, schema_name)
            if schema:
                if view not in schema.children:
                    schema.add_child(view)
                self.db_repo.save(db)
                return view
        return None

    def delete(self, name: str):
        schema, db = self._find_schema_and_db_by_view(name)
        if schema:
            view = self.get_by_name(name)
            if view:
                schema.children.remove(view)
                self.db_repo.save(db)
                return True
        return False
