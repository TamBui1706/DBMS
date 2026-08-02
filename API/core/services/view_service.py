from Classes.DatabaseObjectManagement.view import View
from core.repositories.view_repository import ViewRepository

class ViewService:
    def __init__(self):
        self.repository = ViewRepository()

    def create_view(self, schema_name: str, name: str, query_definition: str):
        existing = self.repository.get_by_name(name)
        if existing:
            return None
        view = View(name=name, queryDefinition=query_definition)
        saved = self.repository.save(schema_name, view)
        return self._map_to_dto(saved) if saved else None

    def list_views(self):
        views = self.repository.get_all()
        return [self._map_to_dto(v) for v in views]

    def get_view(self, name: str):
        view = self.repository.get_by_name(name)
        return self._map_to_dto(view) if view else None

    def update_view(self, name: str, query_definition: str):
        view = self.repository.get_by_name(name)
        if not view:
            return None
        view.queryDefinition = query_definition
        # Find schema containing this view to update it
        schema, db = self.repository._find_schema_and_db_by_view(name)
        if schema:
            self.repository.save(schema.name, view)
        return self._map_to_dto(view)

    def delete_view(self, name: str):
        return self.repository.delete(name)

    def _map_to_dto(self, view: View) -> dict:
        return {
            "name": getattr(view, "name", ""),
            "query_definition": getattr(view, "queryDefinition", "")
        }
