import json
from pathlib import Path
from typing import TypeVar, Generic

from pydantic import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)


class Table(Generic[ModelType]):
    """
    Pure data container representing a table
    """

    def __init__(self, model: type[ModelType], table_name: str):
        self.table_name = table_name
        self.model = model
        self.records: list[ModelType] = []
        self.next_id = 1


class JsonDB:
    """
    Database with all data operations
    """
    BASE_DIR = r"C:\Users\New\Desktop\kai\vs\chatdcp\src\database\tables"

    def __init__(self, model: type[ModelType], table_name: str):
        self.path = Path(f"{self.BASE_DIR}/{table_name}.json")
        self.table = Table(model, table_name)
        self._load()

    def _load(self):
        if not self.path.exists():
            self.create_table_json_file()
            return

        with open(self.path) as f:
            data = json.load(f)
            self.table.records = [self.table.model(**item) for item in data['items']]
            self.table.next_id = data['next_id']

    def create_table_json_file(self):
        with open(self.path, 'w') as f:
            json.dump({'items': [], 'next_id': 1}, f, indent=2)

    def save(self):
        """
        Сохраняет данные, гарантируя наличие id
        """
        items = []
        for item in self.table.records:
            item_data = item.model_dump()

            if hasattr(item, 'id'):
                item_data['id'] = item.id
            items.append(item_data)

        data = {
            'items': items,
            'next_id': self.table.next_id
        }

        with open(self.path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)

    def insert(self, item: ModelType) -> ModelType:
        table = self.table
        item_data = item.model_dump()
        item_data['id'] = table.next_id
        table.next_id += 1

        new_item = table.model(**item_data)
        table.records.append(new_item)
        self.save()
        return new_item

    def get_by_id(self, id_: int) -> ModelType | None:
        """
        Возвращает объект по ID или None если не найден
        """
        for item in self.table.records:
            if hasattr(item, 'id') and item.id == id_:
                return item
        return None

    def delete(self, id_: int) -> bool:
        table = self.table
        for i, item in enumerate(table.records):
            if item.id == id_:
                del table.records[i]
                self.save()
                return True
        return False

    def get_all(self) -> list[ModelType]:
        items: list[ModelType] = []

        for item in self.table.records:
            items.append(item)

        return items